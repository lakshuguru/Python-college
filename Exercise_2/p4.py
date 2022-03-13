print('lakshanaa_20BIT066 \n1.Soup and salad \n2. Pasta with meat sauce \n3. Chef special \n')
n = int(input("Which number would you like to order? \n" ))
if n < 3:
 a = int(input("How many items you need ? "))
if n==1:
 print('%d set of soup and salad coming up.....! ' %(a))
elif n==2:
 print('%d Pasta with meat sauce coming up.....! ' %(a))
elif n==3:
 print('%d Pasta with meat sauce coming up.....! ' %(a))
else:
 print('Invalid entry')