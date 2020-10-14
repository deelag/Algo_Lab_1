from counters import Counter


def insertion_sort_by_height_desc(projector_screens):
    for i in range(1, len(projector_screens)):
        key = projector_screens[i]
        j = i
        while j > 0 and key.height > projector_screens[j - 1].height:
            projector_screens[j] = projector_screens[j - 1]
            Counter.insertion_compare_count += 2
            Counter.insertion_swap_count += 1
            j -= 1
        projector_screens[j] = key
        Counter.insertion_swap_count += 1


def merge_sort_by_width_desc(projector_screens):
    if len(projector_screens) > 1:
        mid = len(projector_screens) // 2
        left_part = projector_screens[mid:]
        right_part = projector_screens[:mid]

        merge_sort_by_width_desc(left_part)
        merge_sort_by_width_desc(right_part)

        i = j = k = 0
        while i < len(left_part) and j < len(right_part):
            Counter.merge_compare_count += 1
            if left_part[i].width > right_part[j].width:
                projector_screens[k] = left_part[i]
                Counter.merge_compare_count += 1
                Counter.merge_swap_count += 1
                i += 1
            else:
                projector_screens[k] = right_part[j]
                Counter.merge_swap_count += 1
                j += 1
            k += 1
        while i < len(left_part):
            projector_screens[k] = left_part[i]
            Counter.merge_compare_count += 1
            Counter.merge_swap_count += 1
            i += 1
            k += 1
        while j < len(right_part):
            projector_screens[k] = right_part[j]
            Counter.merge_compare_count += 1
            Counter.merge_swap_count += 1
            j += 1
            k += 1
