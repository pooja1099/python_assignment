#Python program to count vowel or consonant of the given string
str=input("enter a string: ");  #for input a string
v=0
c=0
for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           v=v+1;
    else:
        c=c+1;

print("The number of vowels:",v)
print("\nThe number of consonant:",c)