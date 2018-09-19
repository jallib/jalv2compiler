echo off
..\compilers\jalv24q6 10f222_blink_intosc.jal
rename 10f222_blink_intosc.hex 10f222_blink_intosc_jalv24q6_windows_32.hex
..\compilers\jalv25 10f222_blink_intosc.jal
rename 10f222_blink_intosc.hex 10f222_blink_intosc_jalv25_windows_32.hex
..\compilers\jalv25_64 10f222_blink_intosc.jal
rename 10f222_blink_intosc.hex 10f222_blink_intosc_jalv25_windows_64.hex
del *.o
del *.asm
del *.cod
