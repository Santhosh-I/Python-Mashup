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

    
