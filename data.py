import pandas


class Data:
    def __init__(self, path):
        """
        Constructor of Data class parses csv file as dictionary.
        :param path: String of the path to the csv file.
        """
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def select_features(self, features):
        """
        This method updates the dictionary by the given features only.
        :param features: list of features.
        :return:
        """
        for key in list(self.data.keys()):
            if key not in features:
                self.data.pop(key)
