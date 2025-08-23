numbers = input("Enter Numbers:")
even_sum =0

for i in numbers:
    num=int(i)
    if num%2==0:
        even_sum+=num
print("Sumof of Even numbers:",even_sum)
        