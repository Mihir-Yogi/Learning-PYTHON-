import time

maxAttempt = 5
weit_time = 1
Attempt = 0

while Attempt < maxAttempt:
    print("Attempt : ", Attempt + 1 , "-Weite time : ",weit_time)
    time.sleep(weit_time)
    weit_time *= 2
    Attempt += 1
