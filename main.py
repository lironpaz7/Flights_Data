import sys
from data import Data
from flights import Flights

import statistics

S = {'D', 'A', 'T', 'S', 'C', 'I', 'E', 'N'}
DETAILS = {"Distance", "Flights", "Passengers", "Seats"}
STATISTICS_FUNCTIONS = [statistics.mean, statistics.median]


def main(argv):
    data = Data(argv[1])
    data.select_features(argv[2])
    flights_data = Flights(data.data)
    flights_data.filter_by_airport_names("Origin_airport", S)
    print("Question 1:")
    flights_data.print_details(DETAILS, STATISTICS_FUNCTIONS)
    flights_data.compute_empty_seats()
    unwanted_flights = flights_data.count_bad_flights(3000)
    answer = "Yes" if unwanted_flights > 3120 else "No"
    print()
    print("Question 2:")
    print(f"Number of unwanted flights: {unwanted_flights}")
    print(f"Will Mr & Mrs Smith be separated? {answer}")


if __name__ == "__main__":
    main(sys.argv)
