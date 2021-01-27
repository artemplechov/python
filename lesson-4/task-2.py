my_list = [2, 1, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list = []

my_list.sort()
print(f"my_list {my_list}")

count = 0

for i in range(len(my_list)-1):
    if my_list[i] != my_list[i+1]:
        result_list = my_list[:i]
    else:
        j = i
        k = i+1
        while my_list[j] == my_list[k] & k < len(my_list):
            count += 1
            k += 1
        result_list = result_list+my_list[j+count:]



print(result_list)