import time

print(time.asctime((time.localtime(time.time()))))
for i in range(0,10):
    print(i)
    time.sleep(1)