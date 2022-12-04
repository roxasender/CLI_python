from time import sleep
import sys

# use /r to reset the cursor to the beginning of the line and override it with new values
# ex: 20% -> /r (reset cursor) -> override 25% -> 25%

for i in range(21):
    sys.stdout.write('\r')
    # the exact output you're looking for:
    sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
    sys.stdout.flush()
    sleep(0.25)