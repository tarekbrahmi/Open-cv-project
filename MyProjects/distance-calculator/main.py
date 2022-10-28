from DistanceCalculator import DistanceCalculator
from VideoStreamer import RealTimeVideoStreamer


def run_real_time_distance_calculator():
    distance_calculator = DistanceCalculator()
    RealTimeVideoStreamer(distance_calculator=distance_calculator).execute(
        applay_delay=True)


if __name__ == "__main__":
    run_real_time_distance_calculator()
