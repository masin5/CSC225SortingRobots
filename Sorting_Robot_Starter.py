"""CSC 225 — Sorting Robot Lottery, simplified edition.

Complete TimeSheet, choose_algorithms, and only your two randomly assigned sorts.
Each sorting function returns (sorted_original_list, number_of_value_comparisons).
Run: python3 Sorting_Robot_Starter.py
"""
import math
import random
from operator import concat


class TimeSheet:
    def __init__(self, algorithm):
        # TODO: store the name; initialize a list of comparison counts.
        self.algorithm = algorithm
        self.comparisons = []

    def add_run(self, count):
        # TODO: append a nonnegative integer comparison count.
        self.comparisons.append(count)

    def average(self):
        # TODO: mean; return None if the list is empty.
        if self.comparisons:
            return sum(self.comparisons) / len(self.comparisons)
        else:
            return None

    def median(self):
        # TODO: middle of a sorted copy, average two middles if even.
        # Return None if the list is empty.
        if not self.comparisons:
            return None

        values = sorted(self.comparisons)
        middle = len(values) // 2

        if len(values) % 2 == 1:
            return values[middle]

        return (values[middle - 1] + values[middle]) / 2

    def standard_deviation(self):
        # TODO: population standard deviation of the comparison counts.
        # Return None if empty; use self.average() to calculate the mean.
        # Do not use the statistics module.
        if not self.comparisons:
            return None
        mean = self.average()
        runSum = 0
        for start in range(len(self.comparisons)):
            runSum += (self.comparisons[start] - mean) ** 2
        final = math.sqrt(runSum / len(self.comparisons))
        return final


    def minimum(self):
        # TODO: return smallest count or None if empty.
        if not self.comparisons:
            return None
        return min(self.comparisons)

    def maximum(self):
        # TODO: return largest count or None if empty.
        if not self.comparisons:
            return None
        return max(self.comparisons)

def bubble_sort(values):
    # TODO if assigned: return (values, comparisons)
    comparisons = 0
    for i in range(len(values)):
        swapped = False
        for j in range(len(values) - 1 - i):
            comparisons += 1
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
        if not swapped:
            break
    return values, comparisons


def selection_sort(values):
    # TODO if assigned
    comparisons = 0
    for start in range(len(values)):
        min_index = start
        for end in range(start, len(values) - 1):
            comparisons += 1
            if values[min_index] > values[end]:
                min_index = end
        values[min_index], values[end] = values[end], values[min_index]
    return values, comparisons

def merge_sort(values):
    # TODO if assigned (you may use temporary lists)
    raise NotImplementedError


def quick_sort(values):
    # TODO if assigned; use last-element pivot
    raise NotImplementedError


def heap_sort(values):
    # TODO if assigned; max heap
    raise NotImplementedError


ALGORITHMS = {
    "Bubble": bubble_sort,
    "Selection": selection_sort,
    "Merge": merge_sort,
    "Quick": quick_sort,
    "Heap": heap_sort,
}


def choose_algorithms(seed):
    """Use random.Random(seed).sample(...) for two DISTINCT names."""
    algorithms = ["Bubble", "Selection", "Merge", "Quick", "Heap"]
    return random.Random(seed).sample(algorithms, 2)


NUMBER_OF_RUNS = 50
LIST_SIZE = 100


def make_test_lists(seed):
    """Create reproducible random lists; both methods receive identical inputs."""
    rng = random.Random(seed + 1000)
    return [[rng.randint(0, 999) for _ in range(LIST_SIZE)]
            for _ in range(NUMBER_OF_RUNS)]


def run_lab(seed):
    selected = choose_algorithms(seed)
    sheets = {name: TimeSheet(name) for name in selected}
    print(f"Seed: {seed} | Algorithms: {', '.join(selected)}")
    print(f"{'Run':>4} {'Method':12} {'Comparisons':>12}")
    for run_number, original in enumerate(make_test_lists(seed), start=1):
        for name in selected:
            values = original.copy()
            _, count = ALGORITHMS[name](values)
            sheets[name].add_run(count)
            print(f"{run_number:4d} {name:12} {count:12d}")
    print("\nCOMPARISON SUMMARIES")
    for name in selected:
        sheet = sheets[name]
        print(f"{name}: counts={sheet.comparisons}, average={sheet.average()}, "
              f"median={sheet.median()}, std_dev={sheet.standard_deviation()}, "
              f"min={sheet.minimum()}, max={sheet.maximum()}")


if __name__ == "__main__":
    seed = int(input("Enter your integer seed: "))
    run_lab(seed)
