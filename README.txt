GRADING SCRIPTS
These are ever evolving scripts to assist in grading.  They are generalized 
scripts that 

move_canvas_submissions_to_subfolder.py - run in a directory with a canvas
downloaded submissions.  Will move submissions to subfolders labeled with 
the student's name.

usage: python move_canvas_submissions_to_subfolder.py

configuration: configuration is hardcoded in this script.   Modify the 
script to change behavior.

notes: A rudimentary script that does some simple file manipulation.  Always
run from base directory of extracted Canvas submissions.

run_java.py, run_java_config.py, run_java_exceptions.py - walks through
directories created from move_canvas_submissions_to_subfolder.py and
compile and run the java program.  Can optionally pass input from stdin
from a file.  Dumps program and compiler output to stdout.  Used to quickly
assess submission quality before in depth grading.

usage: python run_java.py

configuration: modify run_java_config.py for your settings.  Descriptions of
variables in the source.

notes: slightly more robust than move_canvas_submissions_to_subfolder.py.  Will
eventually be extended to also allow for C.  Currently very procedural code, 
but may move to OOP as it becomes more complex.