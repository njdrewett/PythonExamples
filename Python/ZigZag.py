#ZigZag

import time, sys
indent = 0 # how many spaces to indent
indentIncreasing = True # Whether indent is increasing

try:
    while True:
        print(' ' * indent, end='')
        print('*******')

        time.sleep(0.1)

        if indentIncreasing:
            indent += 1
            if indent >= 20:
                # change the direction
                indentIncreasing = False
        else:
            indent -= 1
            if indent <= 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()


