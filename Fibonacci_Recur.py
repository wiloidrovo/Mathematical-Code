import time
t_start = time.time()

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence
n = 13
Fibonacci = fibonacci(n)
print(Fibonacci)
t_stop = time.time()
t_time = (t_stop - t_start)
print("time:", t_time)