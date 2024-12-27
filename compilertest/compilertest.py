#!/usr/bin/env python3
"""
Title: Test the compiler output by compiling and verifying various sample programs.

Author: Rob Jansen, Copyright (c) 2018..2024, all rights reserved.

Adapted-by:

Compiler: N/A

This file is part of jallib (https://github.com/jallib/jallib)
Released under the ZLIB license (http://www.opensource.org/licenses/zlib-license.html)

Description:  This script compiles sample files using various compilers and verifies the results.
              It has two options for use:
                1) It creates (parameter 'create') a baseline  of hex files to compare compiler outputs.
                   The given 'baseline_compiler' is used to create the baseline. The baseline hex files are stored in
                   the directory 'Baseline'
                2) It verifies (parameter 'verify') the baselined hex files with hex files created with new compiler
                   versions. These compilers must be present in the directory 'Compiler'. All used compiler versions
                   must carry a unique name.
               In order to use the script, all sample files that compile without any errors have to be placed in the
               'Sample' directory.
               Results of the verification activity is stored in the file 'Testresults.txt' in the directory 'Log'.
               All compiled hex files are stored in the directory 'Output' carrying the name of the compiler.

Notes:  It has some hard coded platform paths in it so change them to your own needs.
"""

import os
import sys
import subprocess
import shutil
import platform

scriptversion   = "1.0"
scriptauthor    = "Rob Jansen"

platform_name = platform.system()

if (platform_name == "Linux"):
    base = os.path.join("/", "home", "rob", "Documents", "Compilertest")
    devdir = os.path.join("/", "home", "rob", "Documents", "Jallib", "lib")
    cmpdir = os.path.join(base, "Compiler_Linux")
    baseline_compiler = "Baseline"
elif (platform_name == "Windows"):
    base = os.path.join("D:\\", "PIC", "Compiler", "Compilertest")
    devdir = os.path.join("C:\\", "Jallib", "lib")
    cmpdir = os.path.join(base, "Compiler_Windows")
    baseline_compiler = "Baseline.exe"
elif (platform_name == "Darwin"):
    base = os.path.join("/", "Users", "rob", "Documents", "Compilertest")
    devdir = os.path.join("/", "Users", "rob", "Documents", "Jallib", "lib")
    cmpdir = os.path.join(base, "Compiler_Mac")
    baseline_compiler = "Baseline"
else:
    sys.write.stderr("Please add proper environment settings for this platform\n")

srcdir = os.path.join(base, "Sample")
logdir  = os.path.join(base, "Log")
basedir  = os.path.join(base, "Baseline")
outdir  = os.path.join(base, "Output")
createlog = os.path.join(logdir, "Create_results.txt")
verifylog = os.path.join(logdir, "Verify_results.txt")

if (os.path.exists(logdir) == False):
   os.makedirs(logdir)
if (os.path.exists(srcdir) == False):
   os.makedirs(srcdir)
if (os.path.exists(basedir) == False):
   os.makedirs(basedir)
if (os.path.exists(outdir) == False):
   os.makedirs(outdir)
if (os.path.exists(cmpdir) == False):
   os.makedirs(cmpdir)

""" 
Compare the given asm files and store each line that does not match 
in a logfile but skip the first few lines which contain compiler info.
"""
def compare_asm_files(basefile, newfile, errfile):
    fn = open(newfile, "r")
    fb = open(basefile, "r")
    fe = open(errfile, "w")
    # Skip the first 6 lines.
    for skip in range (0, 7):
        newl = fn.readline()
        basel = fb.readline()
    # If possible read a few lines since only one line could be different.
    baselist = []
    newlist = []
    index = 0
    # Read until the whole file is read.
    while (newl != "") and (basel != ""):
        newl = fn.readline()
        basel = fb.readline()
        newlist.append(newl)
        baselist.append(basel)
        index = index + 1
    # Now compare where there are differences.
    base_index = 0
    new_index = 0
    fe.write("For each difference five items are shown where the third item shows the item that differs.\n")
    fe.write("------------------------------------------------------------------------------------------\n")
    fe.write("Baseline                                                                                            New\n")
    fe.write("========                                                                                            ===\n")
    while (base_index < index) and (new_index < index):
        # Compare the lines but ignore labels since the numbering may change.
        if (newlist[new_index] != baselist[base_index]) and \
                ("l__" not in newlist[new_index]) and ("l__" not in baselist[base_index]):
            # Print one line before and after the mismatch.
            if (base_index > 2):
                base_print = base_index - 2
            else:
                base_print = base_index
            if (new_index > 2):
                new_print = new_index - 2
            else:
                new_print = new_index
            if (base_index < (index - 3)):
                end_base = base_index + 3
            else:
                end_base = base_index
            if (new_index < (index - 3)):
                end_new = new_index + 3
            else:
                end_new = new_index
            while (base_print != end_base) and (new_print != end_new):
                line = baselist[base_print]
                line = line.rstrip()
                # Make the line a certain length.
                line_length = len(line)
                while line_length < 100:
                    line = line + " "
                    line_length = line_length + 1
                fe.write(line)
                fe.write(newlist[new_print])
                base_print = base_print + 1
                new_print = new_print + 1
            fe.write("\n\n")

            # Try to sync again (try 10 lines), start with new.
            sync_index = new_index
            sync_count = 0
            synced = False
            while (sync_index < (index - 1)) and (sync_count < 10)\
                    and (synced == False):
                sync_index = sync_index + 1
                sync_count = sync_count + 1
                if (newlist[sync_index] == baselist[base_index]):
                    new_index = sync_index
                    synced = True

            # If not synced, try again with base.
            sync_index = base_index
            sync_count = 0
            while (sync_index < (index - 1)) and (sync_count < 10)\
                    and (synced == False):
                sync_index = sync_index + 1
                sync_count = sync_count + 1
                if (newlist[new_index] == baselist[sync_index]):
                    base_index = sync_index
                    synced = True

        base_index = base_index + 1
        new_index = new_index + 1

    fe.close()
    fb.close()
    fn.close()


# Compare two hex files and return TRUE when they are the same.
def compare_hex_files(basefile, newfile):
    fn = open(newfile, "r")
    fb = open(basefile, "r")
    all_ok = True

    while (all_ok):  # all lines

        newl = fn.readline()
        if (newl == ""):  # EOF
            break

        basel = fb.readline()
        if (basel == ""):  # EOF
            break

        if (newl != basel):
            all_ok = False

    fb.close()
    fn.close()
    return all_ok


def create_baseline():
    # Remove previous baseline.
    for f in os.listdir(logdir):
        os.remove(os.path.join(logdir, f))
    for f in os.listdir(basedir):
        os.remove(os.path.join(basedir, f))
    fl = open(createlog, "w")
    cmdlist = [os.path.join(cmpdir, baseline_compiler), "-no-codfile", "-s", devdir]
    smpcount = 0
    errcount = 0
    if os.path.exists(os.path.join(cmpdir, baseline_compiler)):
        print("Creating baseline hex files of samples using compiler", baseline_compiler)
        for f in os.listdir(srcdir):
            sample = f
            asmfile = sample[:-3] + "asm"  # .jal -> .asm
            hexfile = sample[:-3] + "hex"  # .jal -> .hex
            # When the file is not a jal file do not try to compile it but remove it
            # Sleep needed when running under Virtual Box to prevent error that file does not exist.
            if (sample[-3:] != "jal"):
                os.remove(os.path.join(srcdir, sample))
                continue
            try:
                print("Compiling and baselining sample: ", smpcount, " for sample:", sample)
                fl.write("Compiling file " + sample + "\n   --> ")
                sample = os.path.join(srcdir, sample)
                log = subprocess.check_output(cmdlist + [sample],
                                        stderr=subprocess.STDOUT,
                                        universal_newlines=True,
                                        shell=False)
                loglist = log.split()           # make it a list of strings
                numerrors = int(loglist[-4])    # get number of errors
                numwarnings = int(loglist[-2])  # and warnings
                if ((numerrors == 0) and (numwarnings == 0)):
                    fl.write("OK \n")
                    smpcount += 1
                    if (os.path.exists(os.path.join(srcdir, hexfile))):
                        shutil.copy2(os.path.join(srcdir, hexfile), os.path.join(basedir, hexfile))
                        os.remove(os.path.join(srcdir, hexfile))
                        # Also copy the created asm file for later comparison.
                        shutil.copy2(os.path.join(srcdir, asmfile), os.path.join(basedir, asmfile))
                        os.remove(os.path.join(srcdir, asmfile))
                else:
                    errcount += 1  # issue
                    print(sample, numerrors, "errors", numwarnings, "warnings")
                    fl.write("Error. Compiler reports " + str(numerrors) + " errors and " + str(numwarnings) + " warnings.\n")
            except subprocess.CalledProcessError as e:  # compilation failure
                errcount += 1  # error(s)
                print("Compiler reports return code", e.returncode, "with sample", sample)
                fl.write("Error. Compiler reports return code" + str(e.returncode) + ".\n")
        if (smpcount== 0):
            print("No samples available to create baseline.")
        else:
            print("Samples compiled and baselined successfully: ", smpcount, ", failed: ", errcount)
        # Cleanup the last created hexfile in the sample directory in case of error.
        if (errcount != 0):
            if (os.path.exists(os.path.join(srcdir, hexfile))):
                os.remove(os.path.join(srcdir, hexfile))
    else:
        print("No baseline compiler found.")
    fl.close()

def verify_baseline():
    # Erase previous content.
    for f in os.listdir(logdir):
        os.remove(os.path.join(logdir, f))
    for f in os.listdir(outdir):
        os.remove(os.path.join(outdir, f))
    fl = open(verifylog, "w")
    smpcount = 0
    errcount = 0
    # Compile all samples with various compilers and compare the output with the baseline. Exclude the
    # baseline compiler.
    for compiler in os.listdir(cmpdir):
        if (compiler != baseline_compiler):
            cmdlist = [os.path.join(cmpdir, compiler), "-no-codfile", "-s", devdir]
            print("Compiling for", compiler)
            fl.write("Compiler results for " + compiler + "\n")
            fl.write("-----------------------------\n")
            for sample in os.listdir(srcdir):
                flog = sample[:-4] + "_" + compiler + ".txt"         # Add compiler name to the log textfile.
                hexfile = sample[:-3] + "hex"                        # .jal -> .hex
                asmfile = sample[:-3] + "asm"                        # .jal -> .asm
                newhexfile = sample[:-4] + "_" + compiler + ".hex"   # Add compiler name to the hexfile.
                newasmfile = sample[:-4] + "_" + compiler + ".asm"   # Add compiler name to the hex
                errfile = sample[:-3] + "txt"                        # In case we need to report an error.
                # When the file is not a jal file do not try to compile it but remove it
                if (sample[-3:] != "jal"):
                    os.remove(os.path.join(srcdir, sample))
                    continue
                if os.path.exists(os.path.join(basedir,hexfile)):    # A baseline hexfile must be present.
                    if os.path.exists(os.path.join(srcdir,flog)):
                        os.remove(os.path.join(srcdir,flog))
                    try:
                        print("Compiling and verifying sample:", smpcount, " for sample:", sample)
                        sample = os.path.join(srcdir, sample)
                        log = subprocess.check_output(cmdlist + [sample],
                                                  stderr=subprocess.STDOUT,
                                                  universal_newlines=True,
                                                  shell=False)
                        loglist = log.split()                              # make it a list of strings
                        numerrors = int(loglist[-4])                       # get number of errors
                        numwarnings = int(loglist[-2])                     # and warnings
                        if ((numerrors == 0) and (numwarnings == 0)):
                            smpcount += 1                                   # OK! (zero errors, zero warnings)
                            if os.path.exists(os.path.join(srcdir,hexfile)):
                                newhexfile = os.path.join(outdir,newhexfile)
                                shutil.copy(os.path.join(srcdir,hexfile), newhexfile)
                                # Also copy the asm file.
                                newasmfile = os.path.join(outdir, newasmfile)
                                shutil.copy(os.path.join(srcdir, asmfile), newasmfile)
                                fl.write("File: " + newhexfile + "\n")
                                if (compare_hex_files(os.path.join(basedir, hexfile), newhexfile) == False):
                                    fl.write("   --> Error, hex files do not match. \n")
                                    print("   --> Error, hex files do not match.")
                                    errcount += 1
                                    # Show where the differences are.
                                    compare_asm_files(os.path.join(basedir, asmfile), newasmfile,
                                                      os.path.join(logdir, errfile))
                                else:
                                    fl.write("   --> OK. \n")
                                    print("   --> OK.")
                                    os.remove(os.path.join(srcdir,hexfile))
                                    os.remove(os.path.join(srcdir,asmfile))
                        else:
                            errcount += 1                                   # issue
                            with open(os.path.join(logdir,flog), "w") as fp:
                                fp.write(log)                                # store compiler output
                            fl.write("Error compiling: " + sample + "\n")
                            print(sample, numerrors, "errors", numwarnings, "warnings")
                            print("See", flog, "for compiler output")
                    except subprocess.CalledProcessError as e:            # compilation failure
                        errcount += 1                                      # error(s)
                        with open(os.path.join(logdir,flog), "w") as fp:
                            fp.write(e.output)                              # store compiler output
                        fl.write("Error compiling: " + sample + "\n")
                        print("Compiler reports return code", e.returncode, "with sample", sample)
                        print("See", flog, "for details")
                        fl.write("\n")
                        print("")
                else:
                    fl.write("No baseline exists for " + hexfile + "\n")
                    print("No baseline available for", hexfile)
            if (smpcount == 0):
                print("No samples available to verify against baseline.")
                print("")
                fl.write("\n")
            else:
                print("Samples compiled and verified successfully:", smpcount, ", failed:", errcount)
                fl.write("Samples compiled and verified successfully: " + str(smpcount) +  ", failed: " + str(errcount) + "\n")
    fl.close()

# ======== M A I N ===============================================

if (__name__ == "__main__"):
    print("Test compiler version", scriptversion, "by", scriptauthor)
    if (len(sys.argv) > 1):
       runtype = sys.argv[1].upper()
    else:
       print("Specify CREATE or VERIFY as first argument.")
       sys.exit(1)

    print("Compiler results (.asm and .hex) will be in the Output directory.")
    if (runtype == "CREATE"):
        print("Creating baseline ASM and HEX files, stored in the Baseline directory.")
        print("Overall create results will be logged in the file Create_results.txt in the Log directory.")
        create_baseline()
        sys.exit(1)
    elif (runtype == "VERIFY"):
        print("Creating new ASM and HEX files and verifying HEX files with the baseline.")
        print("Overall create results will be logged in the file Verify_results.txt in the Log directory.")
        print("Differences in files (5 lines per difference)) will be stored as text file in the Log directory.")
        verify_baseline()
        sys.exit(1)
    else:
       print("Specify CREATE or VERIFY as first argument.")



