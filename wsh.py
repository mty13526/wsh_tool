import os
import sys

__author__='shira13526'

description='''
This is a simple tool to manage the Windows file system like a linux shell do.
Also it is my python practicing program.
TODO: 
    - Fix the logical bug caused by space and quotation mark
    - More avaliable linux command
'''

# All 'args' here is a argument list
def cd(args):
    os.chdir(args[0])

def pwd(args):
    print(os.getcwd())

def touch(args):
    for filename in args:
        with open(filename,'w') as f:
            f.write('')

def rm(args):
    for filename in args:
        os.remove(filename)

def mkdir(args):
    for filename in args:
        os.mkdir(filename)

def rmdir(args):
    for filename in args:
        os.rmdir(filename)

def mv(args):
    os.rename(args[0],args[1])

def ls(args):
    if len(args)==0:
        print(os.listdir())
    elif len(args)==1:
        print(os.listdir(args[0]))
    else:
        raise SyntaxError("\'ls\' except 1 argument, {0} are given".format(len(args)))
    
def ll(args):
    if len(args)==0:
        list=os.listdir()
    elif len(args)==1:
        list=os.listdir(args[0])
    else:
        raise SyntaxError("\'ls\' except 1 argument, {0} are given".format(len(args)))
    
    for name in list:
        if os.path.isdir(name):
            print("d {0}".format(name))
        elif os.path.isfile(name):
            print("f {0}".format(name))
        elif os.path.islink(name):
            print("l {0}".format(name))

def clear(args):
    os.system("cls")

def quit(args):
    exit(0)

command_list={
    "cd","pwd","touch","rm","mkdir","rmdir","mv","ls","ll","clear","quit"
}

if __name__ == '__main__':
    while(True):
        PS1='['+os.getcwd()+']'+"$ "
        str=input(PS1)
        str=str.strip().split()
        if len(str) == 0:
            continue
        if str[0] in command_list:
            exec=eval(str[0])
            str.pop(0)
            try:
                exec(str)
            except Exception as e:
                print("Error:",e)
        
    