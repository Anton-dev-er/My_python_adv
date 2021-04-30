import time


def count_time(f):
    def wrapper():
        start_time = time.time()
        f()
        final_time = time.time()
        print("Время работы програми:",final_time - start_time," c")
    return wrapper

@count_time
def test_f():
    a = [i for i in range(1,100_000_000)]

test_f()