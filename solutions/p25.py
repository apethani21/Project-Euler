import time
from util import fibonacci

start_time = time.time()

k = 1
while len(str(fibonacci(k))) < 1000:
    k += 1

print(k+1)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))