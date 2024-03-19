import random
import time
import matplotlib.pyplot as plt

def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

def partition(nums, low, high):

    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):

    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


sort_functions = [heap_sort, merge_sort, quick_sort]
N_values = [100, 1000, 3000, 5000, 7000, 10000, 20000, 50000]

sort_times = {heap_sort: [], merge_sort: [], quick_sort: []}

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