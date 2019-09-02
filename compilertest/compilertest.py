#!/usr/bin/env python3
"""
Title: Test the compiler output by compiling and verifying various sample programs.

Author: Rob Jansen, Copyright (c) 2018..2018, all rights reserved.

Adapted-by: Rob Jansen, Copyright (c) 2018..2018, all rights reserved.

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

scriptversion   = "0.1"
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
else:
    sys.write.stderr("Please add proper environment settings for this platform\n")

srcdir = os.path.join(base, "Sample")
logdir  = os.path.join(base, "Log")
basedir  = os.path.join(base, "Baseline")
outdir  = os.path.join(base, "Output")
difflog = os.path.join(logdir, "Testresults.txt")

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

def compare_files(basefile, newfile):
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
    for f in os.listdir(basedir):
        os.remove(os.path.join(basedir, f))
    cmdlist = [os.path.join(cmpdir, baseline_compiler), "-no-asm", "-no-codfile", "-s", devdir]
    smpcount = 0
    errcount = 0
    if os.path.exists(os.path.join(cmpdir, baseline_compiler)):
        print("Creating baseline hex files of samples using compiler", baseline_compiler)
        for f in os.listdir(srcdir):
            sample = f
            hexfile = sample[:-3] + "hex"  # .jal -> .hex
            # When the file is not a jal file do not try to compile it but remove it
            if (sample[-3:] != "jal"):
                os.remove(os.path.join(srcdir, sample))
                continue
            try:
                print("Compiling and baselining sample: ", smpcount, " for sample:", sample)
                sample = os.path.join(srcdir, sample)
                log = subprocess.check_output(cmdlist + [sample],
                                        stderr=subprocess.STDOUT,
                                        universal_newlines=True,
                                        shell=False)
                loglist = log.split()           # make it a list of strings
                numerrors = int(loglist[-4])    # get number of errors
                numwarnings = int(loglist[-2])  # and warnings
                if ((numerrors == 0) and (numwarnings == 0)):
                    smpcount += 1
                    if (os.path.exists(os.path.join(srcdir, hexfile))):
                        shutil.copy2(os.path.join(srcdir, hexfile), os.path.join(basedir, hexfile))
                        os.remove(os.path.join(srcdir, hexfile))
                else:
                    errcount += 1  # issue
                    print(sample, numerrors, "errors", numwarnings, "warnings")
            except subprocess.CalledProcessError as e:  # compilation failure
                errcount += 1  # error(s)
                print("Compiler reports returncode", e.returncode, "with sample", sample)
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

def verify_baseline():
    # Erase previous content.
    for f in os.listdir(logdir):
        os.remove(os.path.join(logdir, f))
    for f in os.listdir(outdir):
        os.remove(os.path.join(outdir, f))
    fl = open(difflog, "w")
    smpcount = 0
    errcount = 0
    # Compile all samples with various compilers and compare the output with the baseline. Exclude the
    # baseline compiler.
    for compiler in os.listdir(cmpdir):
        if (compiler != baseline_compiler):
            cmdlist = [os.path.join(cmpdir, compiler), "-no-asm", "-no-codfile", "-s", devdir]
#        cmdlist = [os.path.join(cmpdir, compiler), "-no-codfile", "-s", devdir]
            print("Compiling for", compiler)
            fl.write("Compiler results for " + compiler + "\n")
            fl.write("-----------------------------\n")
            for sample in os.listdir(srcdir):
                flog = sample[:-4] + "_" + compiler + ".txt"         # Add compiler name to the log textfile.
                hexfile = sample[:-3] + "hex"                        # .jal -> .hex
                newfile = sample[:-4] + "_" + compiler + ".hex"      # Add compiler name to the hexfile.
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
                                newfile = os.path.join(outdir,newfile)
                                shutil.copy(os.path.join(srcdir,hexfile), newfile)
                                fl.write("File: " + newfile + "\n")
                                if (compare_files(os.path.join(basedir, hexfile), newfile) == False):
                                    fl.write("   --> Error, hex files do not match. \n")
                                    print("   --> Error, hex files do not match.")
                                    errcount += 1
                                else:
                                    fl.write("   --> OK. \n")
                                    print("   --> OK.")
                                    os.remove(os.path.join(srcdir,hexfile))
                        else:
                            errcount += 1                                   # issue
                            with open(os.path.join(logdir,flog), "w") as fp:
                                fp.write(log)                                # store compiler output
                            fl.write("Error compiling: "+ newfile + "\n")
                            print(sample, numerrors, "errors", numwarnings, "warnings")
                            print("See", flog, "for compiler output")
                    except subprocess.CalledProcessError as e:            # compilation failure
                        errcount += 1                                      # error(s)
                        with open(os.path.join(logdir,flog), "w") as fp:
                            fp.write(e.output)                              # store compiler output
                        fl.write("Error compiling: " + newfile + "\n")
                        print("Compiler reports returncode", e.returncode, "with sample", sample)
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
       print("Specify CREATE or VERIFY as first argument")
       sys.exit(1)

    if (runtype == "CREATE"):
        create_baseline()
        sys.exit(1)
    elif (runtype == "VERIFY"):
        verify_baseline()
        sys.exit(1)
    else:
       print("Specify CREATE or VERIFY as first argument")



