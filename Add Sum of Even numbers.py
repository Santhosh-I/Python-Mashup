#method 1 for user input
numbers = input("Enter Numbers:")
even_sum =0

for i in numbers:
    num=int(i)
    if num%2==0:
        even_sum+=num
print("Sumof of Even numbers:",even_sum)

#method 2 for Given input
def even_sum(numbers):
    total_num=0
    for num in numbers:
        if num%2==0:
            total_num+=num
    return total_num

numbers=[1,2,3,4,5,6,7,8,9,10]
print("sum of total numbers",even_sum(numbers))



        