Remarks for building the JALV2 compiler under Windows
-----------------------------------------------------
Use Visual Studio (2017) to build the solution provided in jal. 
The solution can be build for release (jalv2) or debug (jalv2d) but this version is no longer released.
There are two platforms on which the solution can be built (see Configuration Manager under Build):
1) 32-bit, solution x86 using platform win32 (jalv2)
2) 64-bit, solution x64 using platform x64 (jalv2_64)
Make sure that the chosen solution and the platform match.
In both cases a jalv2 version is created which name is used for the 32 bit version as default. 
The 64-bit version must be renamed to jalv2_64.

Remarks for building the JALV2 compiler under Linux
---------------------------------------------------
Standard make the project with 'make project jal'. This will make the native
version of the JAL compiler (jalv2-native), depending on your OS.

There are two Linux scripts:
1) make_32 will make the 32 bit version of the compiler (jalv2-i686)
2) make_64 will make the 64 bit version of the compiler (jalv2-x86-64)

Due to some makefile problems the original Makefile.inc has been adapted as follows:
*) The -Werror has been commented out because of compile errors
The generated compile errors do not seem to have a negative effect on the operation of the compiler.

All created compiler versions (Windows and Linux) should be stored in the 'bin' directory.
