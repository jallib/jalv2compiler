echo off
.\compilers\jalv24q6 18f14k50_blink_hs.jal
rename 18f14k50_blink_hs.hex 18f14k50_blink_hs_jalv24q6_windows_32.hex
..\compilers\jalv25 18f14k50_blink_hs.jal
rename 18f14k50_blink_hs.hex 18f14k50_blink_hs_jalv25_windows_32.hex
..\compilers\jalv25_64 18f14k50_blink_hs.jal
rename 18f14k50_blink_hs.hex 18f14k50_blink_hs_jalv25_windows_64.hex
del *.o
del *.asm
del *.cod
