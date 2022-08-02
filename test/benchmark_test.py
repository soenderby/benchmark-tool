from src.benchmark import Benchmark
import math


def test_can_measure_execution_time():
    benchmark = Benchmark()
    benchmark.start()
    assert benchmark.benchmark == 0
    benchmark.stop()
    assert benchmark.benchmark != 0


def test_running_benchmark_has_small_impact():
    """Check that starting and stopping immediately is equal to 0 to at least 5 decimal points"""
    benchmark = Benchmark()
    benchmark.start()
    benchmark.stop()
    assert math.isclose(benchmark.benchmark, 0.000001, abs_tol=1e-5)
