import random

#total_list = [2,2,2,7,23,1,44,44,3,2,10,7,4,11]
total_list = []
for i in range(random.randint(0,50)):
    total_list.append(random.randint(0,25))

result_list = total_list.copy()
#tmp_list = []
#for i in range(len(total_list)):
 #   result_list.append(0)

print(total_list)
#print(result_list)
total_list.sort()

print(total_list)

count = 0
a = 0

for i in range(len(total_list)-1):
    count = total_list.count(total_list[i])
    print(count)
    if count != 0:
        a = total_list[i]
        for j in range(count-1):
            result_list.remove(a)
print(result_list)


#for i in range(len(total_list)):
 #   a = total_list[i]
  #  print(f"a  {a}")
   # if i < (len(total_list)):
    #    tmp_list = total_list[:i]+total_list[i+1:]
     #   print(f"tmp_list {tmp_list}")
      #  for j in range(len(tmp_list)):
       #     if a == tmp_list[j]:
        #        result_list[i] = 1
    #if i == (len(total_list)):
     #   print(f"a  {a}")
      #  tmp_list = total_list[:i]
       # print(f"tmp_list {tmp_list}")
        #for j in range(len(tmp_list)):
         #   if a == tmp_list[j]:
          #      result_list[i] = 1
#print(f"len of  {len(result_list)}")
#print(f"result_list {result_list}")
#print(f"total_list {total_list}")

#result_list2 = []
#for i in range(len(total_list)):
 #   if result_list[i] == 0:
  #      result_list2.append(total_list[i])
#print(f"Итого {result_list2}")

