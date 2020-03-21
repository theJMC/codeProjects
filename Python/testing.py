import time
print('countdown')
t = input("Set Timer")
n = t - 1
for i in range(n):
    print(n)
    n = n - 1
    time.sleep(1)
print("Lets GOOOOOOOOO!")