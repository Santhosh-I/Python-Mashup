Name = input("Enter your name:")
Marks = int(input("Enter your mark:"))

if Marks >= 50:
    print(f"{Name} has passed with {Marks}% marks")
else:
    print("%s has failed with %d% marks"%(Name,Marks))