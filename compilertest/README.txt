This script compiles sample files using various compilers and verifies the results.

It has two options for use:
1) It creates (parameter 'create') a baseline of hex files to compare compiler outputs.
   The given 'baseline compiler' is used to create the baseline. The baseline hex files are stored in 
   the directory 'Baseline'
2) It verifies (parameter 'verify') the baselined hex files with hex files created with new compiler
   versions. These compilers must be present in the directory 'Compiler'. All used compiler versions 
   must carry a unique name.
   
In order to use the script, the following muse be done:
a) Have the baseline compiler in the compiler directory (Windows, Linux and Mac have different directories).
   Also include all compilers that you want to use to verify in this directory. The name of the baseline compiler
   is fixed:
   -) For Windows Baseline.exe
   -) For Linux Baseline
   -) For Mac Baseline
   So in order to compile all sources with the right compiler, always rename it to this fixed name.
b) Store all sample files that compile without any errors in the 'Sample' directory.
c) Create the baseline by running the Python script with the parameter 'Create'. It will use the
   baseline compiler to create all hex files for the sample programs. All created hex files will be 
   stored in the directory 'Baseline'.
d) Verify the operation of the other compilers by running the Python script with the parameter 'Verify'
   All sample files will be re-compiled with all compilers in the compiler directory (excluding the
   Baseline compiler) and will compare all newly created hex files. They are stored in the 
   directory 'Output'. If there are differences, this will be mentioned. In the end the total result
   will be given about succesful and failed samples. 
   Results of the verification activity is stored in the file 'Testresults.txt' in the directory 'Log'.
e) When errora occur the produced asm files from the Baseline can be compared with the asm files in
   the Output directory.

======================================================================================
The script has some hard-coded paths in it so adapt them to your situation before use.
======================================================================================

Note that because of a bug fixes in the jal compiler, the baseline compiler version must be equal to or higher 
than or equal to jalv25r5.  

Rob Jansen
2021-10-02
