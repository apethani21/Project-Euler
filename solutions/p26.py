import time

start_time = time.time()

num = longest = 1
for n in range(3, 1000, 2):
    if not n%5:
        continue
    p = 1
    while (10**p)%n != 1:
        p += 1

    if p > longest:
        num, longest = n, p

print(num)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))