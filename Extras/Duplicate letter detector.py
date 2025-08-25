#Duplicate letter detector

def duplicate_letter_detctor(string):
    if len(string) == len(set(string)):
        return "No Duplicates"
    else:
        return "Duplicates found"

string = input("Enter a string:")
print("The result:",duplicate_letter_detctor(string))


