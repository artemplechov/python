import random

#total_list = [2,2,2,7,23,1,44,44,3,2,10,7,4,11]
total_list = []
for i in range(random.randint(0,50)):
    total_list.append(random.randint(0,25))
result_list = []
tmp_list = []
for i in range(len(total_list)):
    result_list.append(0)

print(total_list)
print(result_list)
total_list.sort()

print(total_list)

count = 0
a = 0
#result_list = total_list
#for i in range(len(result_list)-3):
 #   if result_list[i] == result_list[i+1]:
  #      j = i
   #     while result_list[j] == result_list[i+1]:
    #        i += 1
     #       count += 1
      #  print(f"count {count}")
       # result_list = result_list[:j] + result_list[j+count+1:]
        #count = 0

for i in range(len(total_list)):
    a = total_list[i]
    print(f"a  {a}")
    if i < (len(total_list)):
        tmp_list = total_list[:i]+total_list[i+1:]
        print(f"tmp_list {tmp_list}")
        for j in range(len(tmp_list)):
            if a == tmp_list[j]:
                result_list[i] = 1
    if i == (len(total_list)):
        print(f"a  {a}")
        tmp_list = total_list[:i]
        print(f"tmp_list {tmp_list}")
        for j in range(len(tmp_list)):
            if a == tmp_list[j]:
                result_list[i] = 1
print(f"len of  {len(result_list)}")
print(f"result_list {result_list}")
print(f"total_list {total_list}")

result_list2 = []
for i in range(len(total_list)):
    if result_list[i] == 0:
        result_list2.append(total_list[i])
print(f"Итого {result_list2}")

