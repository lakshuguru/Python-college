print('lakshanaa-20bit066')
s=set("aeiouAEIOU")
count=0
str=input("Enter a string:")
for i in str:
    if i in s:
        count+=1
print("The vowels present in the string is",count)
