import cProfile
from datetime import datetime
import pstats


class Benchmark:
    def __init__(self, app_id=None, benchmark_id=None, version=None):
        self.app_id = app_id
        self.benchmark_id = benchmark_id
        self.benchmark = 0
        self.version = version
        self.timestamp = None

        self.profile = cProfile.Profile()

    def start(self):
        self.timestamp = datetime.now()
        self.profile.enable()

    def stop(self):
        self.profile.disable()
        self.profile.create_stats()
        self.stats = pstats.Stats(self.profile)
        self.benchmark = self.stats.total_tt
