import sys
import os
import shutil

arg_1 = sys.argv[1]#code filename
arg_2 = sys.argv[2]#txt filename
arg_3 = sys.argv[3]#choice of method
arg_4 = sys.argv[4]#number of threads

os.system(r'gcc' +' '+ arg_1 +' '+ '-o build -lm -fopenmp')
os.system(r'./build'+' '+arg_2 +' ' + arg_3 +' ' + arg_4)
if len(sys.argv)==6:
    arg_5 = sys.argv[5]#another txt filename
    os.system(r'python3 ..//..//plot_2.0.py'+' '+arg_2 + ' '+ '..//..//output/zemlyansky/'+arg_5)
else:
    os.system(r'python3 ..//..//plot.py'+' '+arg_2)
if arg_3 == 'e':
    shutil.copyfile(arg_2, r'..//..//output/zemlyansky/eiler_output.txt')
elif arg_3 == 'r':
    shutil.copyfile(arg_2, r'..//..//output/zemlyansky/runge_output.txt')
elif arg_3 == 'ne':
    shutil.copyfile(arg_2, r'..//..//output/zemlyansky/unsigned_eiler_output.txt')
