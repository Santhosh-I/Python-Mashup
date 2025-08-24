#Duplicate word detector

def duplicate_word_detctor(string):
    if len(string) == len(set(string)):
        return "No Duplicates"
    else:
        return "Duplicates found"

string = input("Enter a string:")
print("The result:",duplicate_word_detctor(string))

