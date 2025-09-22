Name = input("Enter your name:")
Marks = int(input("Enter your mark:"))

if Marks >= 50:
    print(f"{Name} has passed with {Marks}% marks")
else:
    print(f"{Name} has failed with {Marks}% marks")