# A Zig Zag That Ends Only When User Stops Execution

import time, sys

indent = 0 
indentIncreasing = True 

try:
    while 1:
        print(' ' * indent, end = '')
        print('********')
        time.sleep(.10)

        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False
        if not indentIncreasing:
            indent -= 1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
