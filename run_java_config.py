class Config(object):
    #the base directory of submissions, should contain subfolders of individual
    #submissions.  relative to where the program is run
    SUBMISSION_BASE_DIRECTORY = "."
    #number of seconds to wait to consider a process frozen
    PROCESS_TIMEOUT = 10
    #files containing input to programs, or None if not necessary
    PROCESS_INPUTFILE = "../m.txt"
    #pattern of filename to be considered program mainfile
    MAINFILE_PATTERN = ".java"
    #pattern in contents of file to be considered program mainfile
    MAINFILE_CONTENTS_PATTERN = "public static void main"