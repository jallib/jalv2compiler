echo off
# Note: jalv24q6 does not support more than 32 banks (pragma numbanks)
..\compilers\jalv25 16f18446_blink_hs.jal
rename 16f18446_blink_hs.hex 16f18446_blink_hs_jalv25_windows_32.hex
..\compilers\jalv25_64 16f18446_blink_hs.jal
rename 16f18446_blink_hs.hex 16f18446_blink_hs_jalv25_windows_64.hex
del *.o
del *.asm
del *.cod
