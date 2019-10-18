#!/usr/bin/env python3

import os
import os.path
import sys
import shutil

def  generate_files ( dir):
    result = []
    for (subdir, _, fs) in os.walk(dir):
        for f in fs:
            filepath = subdir + os.sep + f
            result.append(filepath)
    return result

def create_directory_if_not_exist(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR - Invalid arguments. Please read \'README\'")
        exit(-1)

    origin_dir = sys.argv[1]
    select_dir = sys.argv[2]

    ofs = generate_files(origin_dir)
    sfs = generate_files(select_dir)
    # TODO: filter out unndessary files.

    # create output directory
    output_dir = select_dir + os.sep + "raw"
    create_directory_if_not_exist(output_dir)

    count = 0
    for sf in sfs:
        filename = os.path.splitext(os.path.basename(sf))[0]
        found = False
        for of in ofs:
            if filename in of:
                found =True
                shutil.copy2(of, output_dir)
                break
        # check wheter the selected file found in raw or not.
        if found:
            count+=1
        else:
            print(" Warnig - {} is not found ".format(filename))

    print(" Done - {}(raw) of {}(selected) are copied".format(count, len(sfs)))
