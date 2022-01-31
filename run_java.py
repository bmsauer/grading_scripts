import os
import sys
import subprocess

from run_java_config import Config
from run_java_exceptions import *

def findmain(config, directory):
    contents = os.listdir(directory)
    for item in contents:
        if os.path.isdir(item):
            continue
        if config.MAINFILE_PATTERN not in item:
            continue
        contents = "";
        with open(os.path.join(directory, item), "r") as filein:
            contents = filein.read() 
        if config.MAINFILE_CONTENTS_PATTERN in contents:
            return item
    return ""
    
def get_submission_subdirs(base_directory):
    submission_subdirs = []
    for item in os.listdir(base_directory):
        if os.path.isdir(item):
            submission_subdirs.append(item)
    return submission_subdirs

def submission_print_header(submission_directory):
    print("=============" + item + "======================", flush=True)
    
def submission_find_mainfile(config, submission_directory):
    mainfile = findmain(config, submission_directory)
    if not mainfile:
        raise MainFileNotFoundError
    else:
        print("main file: " + mainfile, flush=True)
    return mainfile
    
def submission_compile(config, submission_directory, mainfile):
    os.chdir(submission_directory)
    try:
        print("Compiling... " + mainfile, flush=True)
        output = subprocess.check_output("javac " + mainfile, timeout=config.PROCESS_TIMEOUT)
    except subprocess.CalledProcessError as e:
        print(item + " : " + "Error compiling code.", flush=True)
        raise CompileProgramError
    except Exception as e:
        print(item + " : " + "Unknown error compiling code: " + str(e), flush=True)
        raise CompileProgramError
    finally:
        os.chdir("..")

def submission_run(config, submission_directory, mainfile):
    os.chdir(submission_directory)
    try:
        if config.PROCESS_INPUTFILE:
            try:
                inputfile = open("../m.txt", "r")
            except FileNotFoundError:
                print("Input file " + config.PROCESS_INPUTFILE + " not found, aborting.", flush=True)
                raise RunProgramError
        classname = mainfile.split(".")[0]
        print("Running... " + classname, flush=True)
        output = subprocess.check_output("java " + classname, stdin=inputfile, timeout=config.PROCESS_TIMEOUT)
        print(output)
    except subprocess.CalledProcessError as e:
        print("Error running code.", flush=True)
        raise RunProgramError
    except Exception as e:
        print("Unknown Error occurred (timeout?).", flush=True)
        raise RunProgramError
    finally:
        os.chdir("..")
        
def process_submission(config, submission_directory):
    
    submission_print_header(submission_directory)
    try:
        mainfile = submission_find_mainfile(config, submission_directory)
    except MainFileNotFoundError as e:
        print("main file not found for submission: " + submission_directory, flush=True)
        return
    try:
        submission_compile(config, submission_directory, mainfile)
    except CompileProgramError as e:
        print("Compiling failed, skipping submission...")
        return

    try:
        submission_run(config, submission_directory, mainfile)
    except RunProgramError as e:
        print("Running failed, skipping submission...")
        return

if __name__ == "__main__":
    config = Config()
    print("Java runner", flush=True)
    submission_dirs = get_submission_subdirs(config.SUBMISSION_BASE_DIRECTORY)
    for item in submission_dirs:
        process_submission(config, item)
    
    
    