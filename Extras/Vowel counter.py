def Vowel_counter(string):
    words = 0
    vowel = "aeiouAEIOU"
    for i in string:
        if i in vowel:
            words+=1
    return words

string = input("Enter a Word:")  
print("No of vowels in words:",Vowel_counter(string))

letter = "hello"  #inbuilt word
print("No of vowels in words:",Vowel_counter(letter))    #print of inbuilt string  

    
#vowel seperator
def vowel_seperator(string1):
    vowel_words=[]
    vowel="aeiouAEIOU"
    for i in string1:
        if i in vowel:
            vowel_words+=i
    return vowel_words

string1 = input("Enter a word:")
print("The vowel words in the word is :",vowel_seperator(string1)) 

