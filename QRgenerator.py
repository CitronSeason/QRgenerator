import sys
import math

class pycolor:
    BLACK = "\033[30m"
    WHITE = "\033[37m"
    END = "\033[1m"

def retbin(bin):
    if bin == 1:
        return pycolor.WHITE + "x" + pycolor.END
    else:
        return pycolor.BLACK + "x" + pycolor.END

def printQR(str):
    size = math.floor(math.sqrt(len(str)))
    print("QR length:" , len(str) , " one side" , size)
    i=1
    for bit in str:
        x = retbin(1) if bit == "1" else retbin(0)
        sys.stdout.write(x)
        if i % size == 0:
            sys.stdout.write('\n')
        i += 1

        
printQR("1001010101010101110101001")
print('\n')