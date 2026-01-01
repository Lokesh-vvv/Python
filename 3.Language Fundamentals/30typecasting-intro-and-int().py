#TypeCasting or corisson
#We have multiple function for converting one data type to another type. converting one data type tp another data type is called typescasting or corrosion

#Follwoing are the list of the functions for typecast

#int()

#float()

#complex()

#bool()

#str()

#Here We can specifically look for int()

#Converting float to int in the float value if we have 10.990 then it prints only value before the . post . it wont print the value

f = 10.990
i=int(f)
print(i)


# Converting complex to int

c = 10+20j # We can not convert the complex to int we get the typeError

i = int(c)

print(i)


# Converting bool to int() , As we know that internally bool types has valyes True = 1 and False = 0

b = True

i = int(b)

print (i)


bf = False

i = int(bf)

print(i)


# Convert STR to INT , yes it is possible if we have the string like this s = '20' this is consider as string but internally in python it consider as number (int) so we can convert to integer


s = '20'

i = int(s)

print(i)



print('#################################### NOT EXCEPT THE COMPLEX DATA TYPE WE CAN CONVERT TO MOST OF THE ALL FUNDAMENTAL DATA TYPES AS SHOWN ABOVE EXAMPLES')


