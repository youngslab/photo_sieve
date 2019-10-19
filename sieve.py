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

def get_relpath(base, target):
    return target.replace(base, '')

def get_dirpath(filepath):
    return os.path.dirname(filepath)

def get_filename(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]


def expand_directories(d1, d2) :
    tokens1 = d1.split(os.sep)
    tokens2 = d2.split(os.sep)
    return os.sep + os.path.join(*tokens1, *tokens2) + os.sep



def sieve_get_output_dir(out, selected_filepath, selected_dirpath) :
    # customer selected filepath + slected dir => relative path
    dirpath = get_dirpath(selected_filepath)
    expanding_dirpath = get_relpath(selected_dirpath, dirpath)
    # output dirpath + relative path => target dir
    return expand_directories(out, expanding_dirpath)


def sieve(org, sel, out):

    ofs = generate_files(org)
    sfs = generate_files(sel)
    # filter out filder alreday exists
    sfs = [ sf for sf in sfs if not is_child(out, sf) ]

    missed = []
    count = 0
    total = len(sfs)

    for sf in sfs:
        # get selected file name only.
        filename = get_filename(sf)

        # 2. serach the file name in original files.
        found, filepath = search(ofs, filename)
        if found:
            # Create an output directory
            output_dirpath = sieve_get_output_dir(out, sf, sel)
            create_directory_if_not_exist(output_dirpath)
            # Copy the filepath to output directory
            shutil.copy2(filepath, output_dirpath)
            count+=1
        else:
            # Add missing file list to report later.
            missed.append(filename)

    return count, total, missed




if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR - Invalid arguments. Please read \'README\'")
        exit(-1)

    origin_dir = sys.argv[1]
    select_dir = sys.argv[2]
    output_dir = select_dir + os.sep + "raw"

    count, total, missed = sieve(origin_dir, select_dir, output_dir)

    print(" Done - {}(raw) of {}(selected) are copied".format(count, total))
    if len(missed) != 0:
        print(" missing files are \n {}".format(missed))
