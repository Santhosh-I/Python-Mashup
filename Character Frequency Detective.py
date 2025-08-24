#Duplicate word detector

def duplicate_word_detctor(string):
    if len(string) == len(set(string)):
        return "No Duplicates"
    else:
        return "Duplicates found"

string = input("Enter a string:")
print("The result:",duplicate_word_detctor(string))


#Character Frequency Detective

def Character_Frequency_Detective(string1):
    if len(string1)==len(set(string1)):
        return "None"
    else:
        no_duplicates = list(set(string1))
        return no_duplicates


print("The result:",Character_Frequency_Detective(string))

