import random
import string


# bubble sort

def bubble_sort(input_list):
    while True:
        is_sorted = True
        for i in range(len(input_list) - 1):
            j, k = input_list[i], input_list[i + 1]
            if j > k:
                is_sorted = False
                input_list[i], input_list[i + 1] = k, j
        
        if is_sorted:
            break
    
    return input_list


test_list = [n for n in range(20)]
random.shuffle(test_list)
print(test_list)

sorted_test_list = bubble_sort(test_list)
print(sorted_test_list)