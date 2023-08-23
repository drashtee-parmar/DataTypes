# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#Check the data type of two digit number
data_type = type(two_digit_number)

# print(data_type)

# Get the first and second digits using subscripting then convert string to in
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Adding two digits together
two_digit_number = first_digit + second_digit

print(two_digit_number)
