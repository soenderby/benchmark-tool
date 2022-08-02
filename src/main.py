from time import sleep
from benchmark import Benchmark


def fun():
    benchmark = Benchmark()
    benchmark.start()

    for i in range(0, 10):
        sleep(0.1)

    benchmark.stop()
    print("break")


if __name__ == "__main__":
    fun()
