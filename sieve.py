#!/usr/bin/env python3

import os
import os.path
import shutil
import sys

def generate_files(dir):
    result = []
    for (subdir, _, fs) in os.walk(dir):
        for f in fs:
            filepath = subdir + os.sep + f
            result.append(filepath)
    return result


def create_directory_if_not_exist(dir):
    # XXX: debugging
    print("create_directory_if_not_exist({})\n".format(dir))
    if not os.path.exists(dir):
        os.mkdir(dir)


def is_child(dir, filepath):
    if dir in filepath:
        return True
    else:
        return False


def search(filepaths, name):
    for filepath in filepaths:
        if name in filepath:
            return True, filepath
    return False, ""


def get_relpath(base, target):
    return target.replace(base, '')


def get_dirpath(filepath):
    return os.path.dirname(filepath)


def get_filename(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]


def expand_directories(d1, d2):
    tokens1 = d1.split(os.sep)
    tokens2 = d2.split(os.sep)
    return os.path.join(*tokens1, *tokens2) + os.sep

# out_directory: output directory
# selected_filepath: selected filepath
# selected_root : selected root
def sieve_get_output_dir(out_directory, selected_filepath, selected_root):
    # degingging
    print("o: {}, sfile: {}, sdir: {}\n".format(out_directory, selected_filepath, selected_root))
    # customer selected filepath + slected dir => relative path
    dirpath = get_dirpath(selected_filepath)
    expanding_dirpath = get_relpath(selected_root, dirpath)
    # out_directoryput dirpath + relative path => target dir
    return expand_directories(out_directory, expanding_dirpath)


def sieve(org, sel, out):

    ofs = generate_files(org) # original
    sfs = generate_files(sel) # selected

    # filter out folder alreday exists
    sfs = [sf for sf in sfs if not is_child(out, sf)]

    missed = []
    count = 0
    total = len(sfs)

    for sf in sfs:
        # get selected file name only.
        filename = get_filename(sf)
        # XXX: debugging
        # print("")

        # 2. serach the file name in original files.
        found, filepath = search(ofs, filename)
        if found:
            # Create an output directory
            output_dirpath = sieve_get_output_dir(out, sf, sel)
            # XXX: Debugging
            print(" -- output dir: {}", output_dirpath)
            create_directory_if_not_exist(output_dirpath)
            # Copy the filepath to output directory
            shutil.copy2(filepath, output_dirpath)
            count += 1
        else:
            # Add missing file list to report later.
            missed.append(filename)

    return count, total, missed

# VERSION2

# find a file in path
def sieve_find(path, name):
    result = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if name in f:
                return os.path.join(root, f)
    return ""

# copy a file to tgt
def sieve_copy(src, tgt):
    if not os.path.exists(tgt):
        os.mkdir(tgt)
    return shutil.copy2(src, tgt)

def sieve2( raw_dir,enc_dir, out_dir):
    total = 0
    missed = []
    # iterate encoded files
    for (subdir, _, fs) in os.walk(enc_dir):
        if out_dir in subdir:
            continue

        for f in fs:
            total += 1
            # pick ENC
            enc_file =  os.path.join(subdir, f)

            # find RAW 
            raw_file = sieve_find(raw_dir, os.path.splitext(f)[0])
            if not raw_file:
                missed.append(enc_file)
                continue

            # make OUT 
            out_path = os.path.dirname(enc_file).replace(enc_dir, out_dir)

            # copy 
            sieve_copy(raw_file, out_path)
    return total, missed

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR - Invalid arguments. Please read \'README\'")
        exit(-1)

    origin_dir = sys.argv[1]
    select_dir = sys.argv[2]
    output_dir = os.path.join(select_dir, "raw")

    total, missed = sieve2(origin_dir, select_dir, output_dir)

    print(" Done - {}(raw) of {}(selected) are copied".format(total - len(missed), total))
    if len(missed) != 0:
        print(" missing files are \n {}".format(missed))
