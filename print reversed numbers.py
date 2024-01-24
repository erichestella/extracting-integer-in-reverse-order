#title of the code
print('\nEXTRACTING THE REVERSED NUMBERS.')

#for the numbers you want to type   
numeral = int(input('\nTYPE ANY NUMBERS: '))

#this is for to string the numbers you input 
define_numerical = str(numeral)

#it reversed the numbers you input
checking_digital = define_numerical([:: -1])
print('\nREVERSED NUMBERS :'," ".join(checking_digital), '\n')