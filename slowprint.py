import sys
import time

for i in range(10, 30, 2):
    print(i)
    sys.stdout.flush()
    time.sleep(.1)