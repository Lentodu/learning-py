#while loop, run function until condition is false
# i = 0
# while i < 5:
#     i+=1
#     if i == 2:
#         #break #stop the loop
#         continue #continue to next iteration
#     print(i)
    
#for loop, run function for each item in the list
# nums = [1,2,3,4,5]

# for num in nums: #num is the variable that will hold each value in the list nums
# for num in range(1, 6): #range 1-6 will generate a list of numbers from 1 to 5
#     print(num)
#     # if num == 3:
#     #     break #stop the loop

# adjectives = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adjectives:
#     for j in fruits:
#         print(x, j) #red into fruits, big into fruits, tasty into fruits
        

nums = [2, 7, 11, 15]
target = 9
#mencari index kedua bilangan jika dijumlahkan jadi 10

# for i in nums:
#     for j in nums:
#         print("Loop dalam sebanyak", len(nums)) #menjalankan loop dalam ampe selesai baru balik ke loop luar
#     print(i)
#     print("Loop luar selesai")
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        result = nums[i] + nums[j]
        if result == target:
            print(i, j, result)