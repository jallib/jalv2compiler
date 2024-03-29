Remarks for building the JALV2 compilers
========================================

Building the JALV2 compilers for Windows
========================================
There are 2 ways to build the JAL compiler under Windows:
1) Using Visual Studio to build the solution provided in jal (jal.sln)
2) Using a separate compiler like the TDM-GCC compiler 

Using Visual Studio
-------------------
The solution can be build for release (jalv2) or debug (jalv2d) but this version is no longer released.
There are two platforms on which the solution can be built (see Configuration Manager under Build):
1) 32-bit, solution x86 using platform win32 (jalv2)
2) 64-bit, solution x64 using platform x64 (jalv2_64)
Make sure that the chosen solution and the platform match.
In both cases a jalv2.exe is created which name is used for the 32-bit Windows version as default. 
The 64-bit Windows version must be renamed to jalv2_64.

Using a separate compiler (TDM-GCC)
-----------------------------------
This option was chosen since it appeared that the 32-bit Windows compiler created under Visual Studio generated
non-constant output. In some cases the variables were not always assigned to the same data space. Although
the generated program was OK, it was decided to solve this problem by using another compiler.
The TDM-GCC compiler was used for this purpose.
Download TDM-GCC from:http://tdm-gcc.tdragon.net/download
The executable downloaded was: tdm64-gcc-5.1.0-2.exe
After installing the compiler it is in the search path so can be called from any location. Note that this
compiler is called gcc while the Linux compiler is cc.

Two Windows batch files are created one to crate thee 32-bit JAL Windows compiler and to create the 64-bit JAL Windows Compiler. 
The batch files are in the same location where the make scripts for Linux are stored, in the directory 'src'.
-) Make_32.bat will create the 32-bit Windows JAL compiler called jalv2-i686.exe but is renamed to jalv2.exe
-) Make_64.bat will create the 64-bit Windows JAL compiler called jalv2-x86-64.exe but is renamed to jalv2_64.exe

The is also a GitHub action to make the 64-bit Windows compiler, called: Windows Compile 64-bit. It uses
a separate batch file called make_64_github.bat due to other compiler settings.

Building the JALV2 compiler for Linux
=====================================
For this the available cc compiler in Linux Mint was used. Linux Mint 64-bit was running from a Virtual Box.
The compiler can also be created using other Linux OS-es like Ubuntu. 

Standard you can make the project with 'make project jal'. This will make the native
version of the JAL compiler (jalv2-native), depending on your OS.

There are two Linux scripts used for making the two version of the JAL Linux compiler:
1) 'bash make_32' or './make_32' in the src directory will create the 32-bit version of the 
    Linux compiler called jalv2-i686
2) 'bash make_64' or './make_64' in the scr directory will create the 64-bit version of the 
    Linux compiler called jalv2-x86-64

The is also a GitHub action to make the 64-bit Linux compiler, called: Linux Compile 64-bit. 

Building the JALV2 compiler for MacOS
=====================================
For this the available cc compiler in XCode was used. MacOS Big Sur 64-bit was running from a Virtual Box.

Standard you can make the project with 'make project jal'. This will make the native
version of the JAL compiler (jalv2-native), depending on your OS.

There is a Linux script used for making the JAL MacOS compiler:
-) 'bash make_osx' or ./make_osx' in the src directory will create the 64-bit version of the 
    MacOS Linux compiler called jalv2-osx

The is also a GitHub action to make the 64-bit MAC compiler, called: MAC Compile.

Other info
==========
The file 'jal_build.h' in the 'src' directory is automatically created under Linux but not under Windows. This file
contains the JAL compiler version and when it has been built. Under Windows it should be edited before building the
Windows compiler. An alternative way to deal with this is to first compile the Linux version, copy the newly created 
'jal_build.h' file to the 'src' directory and then compile the Windows version.

Since compiler version jalv25r6 all -Werrors where resolved for all compiler versions.

All created compiler versions (Windows,  Linux and MacOS) should be stored in the 'bin' directory.

2023-05-28
Rob Jansen

