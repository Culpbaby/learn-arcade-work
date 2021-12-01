my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]

def selection_sort(my_list):
    """ Sort a list using the selection sort """

    # Loop through the entire array
    total = 0
    for cur_pos in range(len(my_list)):
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos
        total += 1

        # Scan left to right (end of the list)
        print(total)
        for scan_pos in range(cur_pos + 1, len(my_list)):
            total = 0
            # Is this position smallest?
            if my_list[scan_pos] < my_list[min_pos]:
                total += 1

                # It is, mark this position as the smallest
                min_pos = scan_pos
        print(total)
        # Swap the two values
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp