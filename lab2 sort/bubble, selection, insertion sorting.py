import random
import time
import matplotlib.pyplot as plt
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

def selection_sort(nums):
     for i in range(len(nums)):
         lowest_value_index = i
         for j in range(i + 1, len(nums)):
             if nums[j] < nums[lowest_value_index]:
                 lowest_value_index = j
         nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

def insertion_sort(nums):
     for i in range(1, len(nums)):
         item_to_insert = nums[i]
         j = i - 1
         while j >= 0 and nums[j] > item_to_insert:
             nums[j + 1] = nums[j]
             j -= 1
         nums[j + 1] = item_to_insert

sort_functions = [bubble_sort, selection_sort, insertion_sort]
N_values = [100, 1000, 3000, 5000, 7000, 10000, 20000, 50000]

sort_times = {bubble_sort: [], selection_sort: [], insertion_sort: []}

for sort_function in sort_functions:
    print(f"Сортировка: {sort_function.__name__}")
    for N in N_values:
        random_list_of_nums = [random.randint(0, 1000) for _ in range(N)]
        start_time = time.time()
        sort_function(random_list_of_nums)
        end_time = time.time()
        sort_times[sort_function].append(end_time - start_time)
        print("Время сортировки для N = {}: {} секунд".format(N, end_time - start_time))
    print("\n")

plt.figure(num='Графики')
for sort_function, times in sort_times.items():
    plt.plot(N_values, times, label=f'{sort_function.__name__}')

plt.xlabel('Размер массива')
plt.ylabel('Время сортировки (секунды)')
plt.legend()
plt.show()