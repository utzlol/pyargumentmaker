import sys
def mkargv(argvoption, command):
    print(len(sys.argv))
    if len(sys.argv) > 2:   #To prevent more than two arguments
        print("Too many arguments")
    if len(sys.argv) > 1:
        if sys.argv[1] == argvoption:
            exec(command)
            
mkargv("yudha", "print('Hi')")
