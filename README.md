django-paf-upload-script
========================

Python script to push the royalmail PAF file to a django database

set up:
Update the paths to your directory structure.
This was run on a debian server.

usage:
From the commandline type:

python csv_load.py


incase of seeing 'killed' which means you ran out of memory.
record the final number shown on the terminal before killed e.g. 632823
load the file into vi and delete all the lines which are already in the database and run again.
e.g.
vi "CSV PAF.csv"
:632823
dgg
:wq

