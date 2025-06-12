def bubble_sort(numbers_list):
    nums=len(numbers_list)
    for i in range (nums-1):
        for j in range(0,nums-i-1):
            if numbers_list[j]>numbers_list[j+1]:
                numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
    return numbers_list

def count_positive(numbers_list):
    positive_count=sum(1 for nums in numbers_list if nums>0)
    return positive_count

def count_negative(numbers_list):
    negative_count=sum(1 for nums in numbers_list if nums<0)
    return negative_count

ui=input("Enter numbers seperated by space: ")
numbers_list = list(map(int, ui.split()))
sort_numbers= bubble_sort(numbers_list[:])

positive_count=count_positive(numbers_list)
negative_count=count_negative(numbers_list)

print("Sorted list:", sort_numbers)
print("Count of positive numbers:", positive_count)
print("Count of negative numbers:", negative_count)

