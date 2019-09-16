Echo off
Echo Bulding JAL 32-bit compiler for Windows

Echo Clean up old stuff
if exist libutils\.obj-i686 rmdir /s /q libutils\.obj-i686
if exist libutils\.dep rmdir /s /q libutils\.dep
if exist libcore\.obj-i686 rmdir /s /q libcore\.obj-i686
if exist libcore\.dep rmdir /s /q libcore\.dep
if exist libpic12\.obj-i686 rmdir /s /q libpic12\.obj-i686
if exist libpic12\.dep rmdir /s /q libpic12\.dep
if exist jal\.obj-i686 rmdir /s /q jal\.obj-i686
if exist jal\.dep rmdir /s /q jal\.dep
if exist ..\bin\jalv2.exe del /q ..\bin\jalv2.exe

Rem Build the compiler
Echo Building Libutils
cd libutils
mkdir .obj-i686
mkdir .dep
gcc -MMD -MF .dep/array.d -c -o .obj-i686/array.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g array.c
gcc -MMD -MF .dep/cache.d -c -o .obj-i686/cache.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g cache.c
gcc -MMD -MF .dep/codefile.d -c -o .obj-i686/cod_file.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g cod_file.c
gcc -MMD -MF .dep/mem.d -c -o .obj-i686/mem.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g mem.c
Echo creating libutils-i686.a
ar -r libutils-i686.a .obj-i686/array.o .obj-i686/cache.o .obj-i686/cod_file.o .obj-i686/mem.o
Echo Building Libcore
cd ..\libcore
mkdir .obj-i686
mkdir .dep
gcc -MMD -MF .dep/fp_op.d -c -o .obj-i686/pf_op.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pf_op.c
gcc -MMD -MF .dep/operator.d -c -o .obj-i686/operator.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g operator.c
gcc -MMD -MF .dep/vararray.d -c -o .obj-i686/vararray.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g vararray.c
gcc -MMD -MF .dep/expr.d -c -o .obj-i686/expr.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g expr.c
gcc -MMD -MF .dep/pf_src.d -c -o .obj-i686/pf_src.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pf_src.c
gcc -MMD -MF .dep/cmd_op.d -c -o .obj-i686/cmd_op.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g cmd_op.c
gcc -MMD -MF .dep/pf_cmd.d -c -o .obj-i686/pf_cmd.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pf_cmd.c
gcc -MMD -MF .dep/variable.d -c -o .obj-i686/variable.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g variable.c
gcc -MMD -MF .dep/cmdarray.d -c -o .obj-i686/cmdarray.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g cmdarray.c
gcc -MMD -MF .dep/pf_proca.d -c -o .obj-i686/pf_proca.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pf_proca.c
gcc -MMD -MF .dep/cmd.d -c -o .obj-i686/cmd.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g cmd.c
gcc -MMD -MF .dep/pf_token.d -c -o .obj-i686/pf_token.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pf_token.c
gcc -MMD -MF .dep/tag.d -c -o .obj-i686/tag.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g tag.c
gcc -MMD -MF .dep/cmd_brch.d -c -o .obj-i686/cmd_brch.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g cmd_brch.c
gcc -MMD -MF .dep/cmd_proc.d -c -o .obj-i686/cmd_proc.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g cmd_proc.c
gcc -MMD -MF .dep/cmddelay.d -c -o .obj-i686/cmddelay.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g cmddelay.c
gcc -MMD -MF .dep/pfile.d -c -o .obj-i686/pfile.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pfile.c
gcc -MMD -MF .dep/pf_block.d -c -o .obj-i686/pf_block.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pf_block.c
gcc -MMD -MF .dep/cmd_optm.d -c -o .obj-i686/cmd_optm.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g cmd_optm.c
gcc -MMD -MF .dep/vardef.d -c -o .obj-i686/vardef.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g vardef.c
gcc -MMD -MF .dep/cmd_lbl.d -c -o .obj-i686/cmd_lbl.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g cmd_lbl.c
gcc -MMD -MF .dep/cmd_log.d -c -o .obj-i686/cmd_log.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g cmd_log.c
gcc -MMD -MF .dep/value.d -c -o .obj-i686/value.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g value.c
gcc -MMD -MF .dep/cmd_asm.d -c -o .obj-i686/cmd_asm.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g cmd_asm.c
gcc -MMD -MF .dep/pf_proc.d -c -o .obj-i686/pf_proc.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pf_proc.c
gcc -MMD -MF .dep/pf_expr.d -c -o .obj-i686/pf_expr.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pf_expr.c
gcc -MMD -MF .dep/label.d -c -o .obj-i686/label.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g label.c
gcc -MMD -MF .dep/cmdassrt.d -c -o .obj-i686/cmdassrt.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g cmdassrt.c
gcc -MMD -MF .dep/valarray.d -c -o .obj-i686/valarray.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g valarray.c
gcc -MMD -MF .dep/exprnode.d -c -o .obj-i686/exprnode.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g exprnode.c
Echo creating libcore-i686.a
ar -r libcore-i686.a .obj-i686/expr.o .obj-i686/cmd_op.o .obj-i686/cmd_lbl.o .obj-i686/variable.o .obj-i686/pf_token.o .obj-i686/pf_src.o .obj-i686/cmddelay.o .obj-i686/pf_proca.o .obj-i686/cmd_brch.o .obj-i686/cmd_proc.o .obj-i686/tag.o .obj-i686/value.o .obj-i686/pf_op.o .obj-i686/pfile.o .obj-i686/cmd_log.o .obj-i686/vararray.o .obj-i686/cmd_asm.o .obj-i686/pf_proc.o .obj-i686/label.o .obj-i686/cmd_optm.o .obj-i686/valarray.o .obj-i686/exprnode.o .obj-i686/operator.o .obj-i686/cmdarray.o .obj-i686/pf_cmd.o .obj-i686/cmd.o .obj-i686/vardef.o .obj-i686/pf_block.o .obj-i686/pf_expr.o .obj-i686/cmdassrt.o
Echo Building Libpic12
cd ..\libpic12
mkdir .obj-i686
mkdir .dep
gcc -MMD -MF .dep/pic_code.d -c -o .obj-i686/pic_code.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic_code.c
gcc -MMD -MF .dep/pic_gop.d -c -o .obj-i686/pic_gop.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic_gop.c
gcc -MMD -MF .dep/pic.d -c -o .obj-i686/pic.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic.c
gcc -MMD -MF .dep/pic16.d -c -o .obj-i686/pic16.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic16.c
gcc -MMD -MF .dep/picdelay.d -c -o .obj-i686/picdelay.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g picdelay.c
gcc -MMD -MF .dep/pic12.d -c -o .obj-i686/pic12.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic12.c
gcc -MMD -MF .dep/pic_stvar.d -c -o .obj-i686/pic_stvar.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic_stvar.c
gcc -MMD -MF .dep/pic_daop.d -c -o .obj-i686/pic_daop.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic_daop.c
gcc -MMD -MF .dep/piccolst.d -c -o .obj-i686/piccolst.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g piccolst.c
gcc -MMD -MF .dep/pic_stk.d -c -o .obj-i686/pic_stk.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic_stk.c
gcc -MMD -MF .dep/pic_emu.d -c -o .obj-i686/pic_emu.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic_emu.c
gcc -MMD -MF .dep/pic_opfn.d -c -o .obj-i686/pic_opfn.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic_opfn.c
gcc -MMD -MF .dep/pic_wopt.d -c -o .obj-i686/pic_wopt.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic_wopt.c
gcc -MMD -MF .dep/pic_cmdo.d -c -o .obj-i686/pic_cmdo.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic_cmdo.c
gcc -MMD -MF .dep/picmovlpop.d -c -o .obj-i686/picmovlpop.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g picmovlpop.c
gcc -MMD -MF .dep/pic_inst.d -c -o .obj-i686/pic_inst.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic_inst.c
gcc -MMD -MF .dep/pic14.d -c -o .obj-i686/pic14.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic14.c
gcc -MMD -MF .dep/picbsrop.d -c -o .obj-i686/picbsrop.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g picbsrop.c
gcc -MMD -MF .dep/pic_op.d -c -o .obj-i686/pic_op.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic_op.c
gcc -MMD -MF .dep/pic14h.d -c -o .obj-i686/pic14h.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic14h.c
gcc -MMD -MF .dep/pic_var.d -c -o .obj-i686/pic_var.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic_var.c
gcc -MMD -MF .dep/pic_brop.d -c -o .obj-i686/pic_brop.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g pic_brop.c
Echo creating libpic12-i686.a
ar -r libpic12-i686.a .obj-i686/pic_gop.o .obj-i686/pic16.o .obj-i686/pic_daop.o .obj-i686/pic_stk.o .obj-i686/pic_op.o .obj-i686/pic_brop.o .obj-i686/pic_code.o .obj-i686/pic_opfn.o .obj-i686/picmovlpop.o .obj-i686/pic_emu.o .obj-i686/pic_var.o .obj-i686/picdelay.o .obj-i686/pic12.o .obj-i686/pic_cmdo.o .obj-i686/pic_stvar.o .obj-i686/pic_inst.o .obj-i686/pic.o .obj-i686/piccolst.o .obj-i686/pic14.o .obj-i686/picbsrop.o .obj-i686/pic_wopt.o .obj-i686/pic14h.o
Echo Building Jal
cd ..\jal
mkdir .obj-i686
mkdir .dep
gcc -MMD -MF .dep/jal_main.d -c -o .obj-i686/jal_main.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g jal_main.c
gcc -MMD -MF .dep/jal_blck.d -c -o .obj-i686/jal_blck.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g jal_blck.c
gcc -MMD -MF .dep/jal_vdef.d -c -o .obj-i686/jal_vdef.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g jal_vdef.c
gcc -MMD -MF .dep/jal_prnt.d -c -o .obj-i686/jal_prnt.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g jal_prnt.c
gcc -MMD -MF .dep/jal_op.d -c -o .obj-i686/jal_op.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g jal_op.c
gcc -MMD -MF .dep/jal_incl.d -c -o .obj-i686/jal_incl.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g jal_incl.c
gcc -MMD -MF .dep/jal_ctrl.d -c -o .obj-i686/jal_ctrl.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g jal_ctrl.c
gcc -MMD -MF .dep/jal_proc.d -c -o .obj-i686/jal_proc.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g jal_proc.c
gcc -MMD -MF .dep/jal_expr.d -c -o .obj-i686/jal_expr.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g jal_expr.c
gcc -MMD -MF .dep/jal_file.d -c -o .obj-i686/jal_file.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g jal_file.c
gcc -MMD -MF .dep/jal_asm.d -c -o .obj-i686/jal_asm.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g jal_asm.c
gcc -MMD -MF .dep/jal_tokn.d -c -o .obj-i686/jal_tokn.o -O2 -ansi -pedantic -W -Wall -Wshadow -Wcast-qual -Wcast-align -march=i686 -m32 -g jal_tokn.c
gcc -o ../../bin/jalv2-i686 .obj-i686/jal_op.o .obj-i686/jal_incl.o .obj-i686/jal_proc.o .obj-i686/jal_main.o .obj-i686/jal_blck.o .obj-i686/jal_vdef.o .obj-i686/jal_asm.o .obj-i686/jal_tokn.o .obj-i686/jal_ctrl.o .obj-i686/jal_prnt.o .obj-i686/jal_expr.o .obj-i686/jal_file.o ../libpic12/libpic12-i686.a ../libcore/libcore-i686.a ../libutils/libutils-i686.a -g -m32 -march=i686 -lm 
Echo Strip symbols from the object file to shrink size
cd ../../bin
strip jalv2-i686.exe
rename jalv2-i686.exe jalv2.exe
Echo All done!
Pause


