#!/usr/bin/env python3



import os
import os.path
import sys
import shutil

def  generate_files (dir):
    result = []
    for (subdir, _, fs) in os.walk(dir):
        for f in fs:
            filepath = subdir + os.sep + f
            result.append(filepath)
    return result

def create_directory_if_not_exist(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

def is_child(dir, filepath) :
    if dir in filepath:
        return True
    else:
        return False

def search(filepaths, name):
    for filepath in filepaths:
        if name in filepath:
            return True, filepath
    return False,""

def sieve(org, sel, out):

    ofs = generate_files(org)
    sfs = generate_files(sel)
    # filter out filder alreday exists
    sfs = [ sf for sf in sfs if not is_child(out, sf) ]

    missed = []
    count = 0
    total = len(sfs)

    for sf in sfs:
        # get select file name only.
        filename = os.path.splitext(os.path.basename(sf))[0]

        # releative path
        # selected file : sel/yyy/xxxx.jpg
        # relative info : yyy
        # 1) remove basedir()

        # relative = os.path.(sf - org)
        # serach the file name in original files.
        found, filepath = search(ofs, filename)
        if found:
            # if found copy the filepath to outpu_dir
            count+=1
            shutil.copy2(filepath, output_dir)
        else:
            missed.append(filename)

    return count, total, missed




if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR - Invalid arguments. Please read \'README\'")
        exit(-1)

    origin_dir = sys.argv[1]
    select_dir = sys.argv[2]
    output_dir = select_dir + os.sep + "raw"
    create_directory_if_not_exist(output_dir)

    count, total, missed = sieve(origin_dir, select_dir, output_dir)

    print(" Done - {}(raw) of {}(selected) are copied".format(count, total))
    if len(missed) != 0:
        print(" missing files are \n {}".format(missed))
