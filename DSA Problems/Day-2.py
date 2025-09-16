List = list(map(int,input("Enter the list of numbers with space seperated:").split()))
Target = int(input("Enter Targer value:"))
if List[Target] in List:
    print(List[Target])
else:
    print("No Element Found")