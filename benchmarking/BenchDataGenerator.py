import random

class BenchDataGenerator:
    """
    A class for generating test data for binary search tree performance evaluation.
    """

    def __init__(self, size, duplication_rate=0, duplicate_count=0, data_range=None):
        """
        :arg size (int): The number of elements to generate.
        :arg duplication_rate (float): The percentage of duplicate elements (0 to 1): no_duplicates / no_elements.
        :arg duplicate_count (int): The number of specific duplicate elements.
        """
        self.size = size
        self.duplication_rate = duplication_rate
        self.duplicate_count = duplicate_count
        self.data_range = (0, int(size * (1 - duplication_rate) + 1)) if data_range is None else data_range

        if duplication_rate > 0:
            max_unique_elements = self.data_range[1] - self.data_range[0] + 1
            unique_count = int(self.size * (1 - self.duplication_rate))
            if unique_count > max_unique_elements:
                raise ValueError("Duplication rate too high for the given data range. Possible value: %0.3f" % (max_unique_elements/size))

    def generate_random_data(self):
        """
        Generates a list of random integers with the specified duplication rate.

        Example:
        A duplication rate of 30% means that 30% of the total elements will be duplicates
        This is achieved by first filling 70% of the output list with unique elements,
        then the rest is sampled from elements already in the list

        :returns: A list of integers.
        """
        data = []
        # Create unique elements
        unique_count = int(self.size * (1 - self.duplication_rate))

        if unique_count > 0:
            # Sample from range
            unique_values = random.sample(range(*self.data_range),
                                          min(unique_count, self.data_range[1] - self.data_range[0]))
            data.extend(unique_values)

            # Choose k values from unique values population
            duplicate_values = random.choices(unique_values, k=self.size - unique_count)
            data.extend(duplicate_values)
        else:
            # If duplication rate is 100%, fill the list with a single random value
            duplicate_value = random.choice(range(*self.data_range))
            data = [duplicate_value] * self.size

        random.shuffle(data)
        return data

    def generate_data_with_duplicates(self):
        """
        Generates a list of integers with a specified number of duplicate elements.
        :returns: A list of integers.
        """
        if self.duplicate_count > self.size:
            raise ValueError("Duplicate count cannot exceed the size of the data.")

        data = random.sample(range(*self.data_range), self.size - self.duplicate_count)
        duplicates = random.choices(data, k=self.duplicate_count)
        data.extend(duplicates)

        random.shuffle(data)
        return data

    def generate_search_keys(self, data):
        """
        Generates a list of search keys from the given data.

        :arg:data (list): The list of data elements.

        :returns: A list of search keys.
        """
        return random.sample(data, len(data) // 2) #Generate half the size of the data list.