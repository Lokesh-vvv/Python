#Sliceoperator Applications:

s='srilaxmi'
#Convert above string dtarting letter to upeercase]
output=s[0].upper()
print(output)

#Here logical think convert last letter of the string to uppercase

s='srilaxmi'
output=s[-1].upper()
print(output)


#Another logical quations convert the first letter and last letter of the string into capitol but this time it should be dynamic using length

s= 'srilaxmi'
output= s[0].upper()+s[1:8]+s[-1].upper()
print(output)

#Now dynamically with this we can provide any string it works dynamically

s="ramadecorations"

output=s[0].upper()+s[1:len(s)-1]+s[-1].upper()
print(output)




