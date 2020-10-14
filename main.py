import csv
import time
import projector_screen
import sorting_algorithms
from counters import Counter
from random import shuffle


def print_list(projector_screens):
    for i in range(len(projector_screens)):
        print(projector_screens[i])


if __name__ == '__main__':

    projector_screens = []
    with open('projector_screens.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            projector_screens.append(projector_screen.ProjectorScreen(row[0], row[1], row[2], row[3]))

    # Insertion Sort
    print("_____________INSERTION________________")
    insertion_sort_time_start = time.time()
    sorting_algorithms.insertion_sort_by_height_desc(projector_screens)
    insertion_sort_time_end = time.time() - insertion_sort_time_start
    print_list(projector_screens)
    print(insertion_sort_time_end)
    print(Counter.insertion_swap_count)
    print(Counter.insertion_compare_count)

    shuffle(projector_screens)

    # Merge Sort
    print("_______________MERGE_________________")
    merge_sort_time_start = time.time()
    sorting_algorithms.merge_sort_by_width_desc(projector_screens)
    merge_sort_time_end = time.time() - merge_sort_time_start
    print_list(projector_screens)
    print(merge_sort_time_end)
    print(Counter.merge_swap_count)
    print(Counter.merge_compare_count)

