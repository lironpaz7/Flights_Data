import statistics


class Flights:

    def __init__(self, data):
        """
        Constructor of Flights class.
        :param data: dictionary.
        """
        self.data = data

    def filter_by_airport_names(self, airports, letters):
        """
        This method updates the dictionary by checking if the values in the list of airports starts with a letter
        from letters.
        :param airports: String of key.
        :param letters: Set of letters.
        :return:
        """
        for index in reversed(range(len(self.data[airports]))):
            value = self.data[airports][index]
            if value[0] not in letters:
                for key in self.data.keys():
                    self.data[key].pop(index)

    def print_details(self, features, statistic_functions):
        """
        This method prints the details.
        :param features: Set of keys.
        :param statistic_functions: List of methods from statistics.py .
        :return:
        """
        features = sorted(list(features))
        for feature in features:
            temp = []
            for method in statistic_functions:
                temp.append(str(method(self.data[feature])))
            print(f"{feature}: {', '.join(temp)}")

    def compute_empty_seats(self):
        """
        This method adds the key "Empty_seats" and assign values
        :return:
        """
        self.data.update({"Empty_seats": []})
        for index in range(len(self.data["Seats"])):
            self.data["Empty_seats"].append(int(self.data["Seats"][index] - self.data["Passengers"][index]))

    def count_bad_flights(self, num):
        """
        This method counts the number of bad flights.
        :param num: whole number.
        :return:
        """
        average = statistics.mean(self.data["Empty_seats"])
        unwanted_flights = 0
        for value in self.data["Empty_seats"]:
            if abs(average - value) >= num:
                unwanted_flights += 1
        return unwanted_flights
