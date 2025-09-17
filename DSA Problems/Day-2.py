List = list(map(int,input("Enter the list of numbers with space seperated:").split()))
Target = int(input("Enter Targer value:"))

if Target in List:
    print("Element",Target,"found at index",List.index(Target))
else:
    print("Element Not Found")