List = list(map(int,input("Enter the list of numbers with space seperated:").split()))
Target = int(input("Enter Targer value:"))

Length = len(List)

if Target<Length:
    print("Element",List[Target],"found at index",Target)
else:
    print("Element Not Found")