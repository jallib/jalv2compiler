Remarks for building the JALV2 compiler under Windows
-----------------------------------------------------
Use Visual Studio (2017) to build the solution provided in jal. 
The solution can be build for release (jalv2) or debug (jalv2d) but this version is not released.
There are two platforms on which the solution can be built (see Configuration Manager under Build):
1) 32-bit, solution x86 using platform win32
2) 64-bit, solution x64 using platform x64
Make sure that the chosen solution and the platform match.
When doing a clean build make sure to copy the the compiler first from the bin directory. 
In both cases a jalv2 version is created which name is used for the 32 bit version as default. 
The 64-bit version is renamed to jalv2_64.

Remarks for building the JALV2 compiler under Linux
---------------------------------------------------
Standard make the project with 'make project jal'. This will make the 32-bit
version of the jal compiler (jalv2-i686).

There are two linux scripts:
1) make_32 will make the - default - 32 bit version of the compiler (jalv2-i686)
2) make_64 will make the 64 bit version of the compiler (jalv2-x86-64)
The scripts both start with 'make clean' so make sure to copy the compiler first from the bin directory

Due to some makefile problems the original Makefile.inc has been adapted as follows:
*) The -Werror has been commented out because of compile errors

The generated compile errors do not seem to have a negative effect on the operation of the compiler.


2018-09-19
Rob Jansen
