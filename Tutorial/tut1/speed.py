import time
counter = 0
begin = time.time()
N = 5000 # try adding a few more zero digitS at the back of this variable to make your computer hangs...
for i in range(N): # O(c * N*N) = O(cN^2), c is 'small' if you leave line 14 commented, but c is BIG if you uncomment it
    #print("i = %d" % i)
    #j = 1
    while j < N: # O(log N)
        j *= 2
    for j in range(N): # O(N) inner loop, that will be repeated N times in the outer loop
        counter += 1 # this operation is O(1), and fast, let's say 0.0000000001 s
        # but if you uncomment the next line, the same algorithm will be noticeably much slower
        #print(" counter = %d" % counter) # this I/O operation is 'heavy', let's say 0.01s per statement...
print("counter = %d, computed in = %f" % (counter, time.time()-begin)) # elapsed time in seconds
# the default setup of this starting SpeedTest.py should be around 2-3s