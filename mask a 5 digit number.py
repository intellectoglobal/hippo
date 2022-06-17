
# def maska5digitnumber():
#     str = input("Enter the mobile number: ")
#     masked = len(str) - 5
#     slimstr = str[masked:]
#     print("Your masked card number is: ", end="")
#     print("x" * masked + slimstr)  
#     a = input("Enter the mobile number")
#     masked = len(a) - 5
#     slima = a[masked:]
#     print("Your masked card number is: ", end="")
#     print("y" * masked + slima)

# maska5digitnumber()



# num = input("Enter your mobile number: ")
# if num == 1:
#     print ("a")
# elif num == 2:
#     print ("b")
# else:
#     print("c")
    
# num = input("Enter your number: ")
# import string
# start = ''
# for i in range(0,10):
#     value = int(num[i])
#     x = string.ascii_lowercase[value]
#     start += x

# # print(start+ str(num[-5:]))
# print(start)




# num = input("enter your number: ")
# if num == 1:
#     print("a")
# elif num == 2:
#     print("b")
# elif num == 3:
#     print("c")
# elif num == 4:
#     print("d")
# elif num == 5:
#     print("e")
# elif num == 6:
#     print("f")
# elif num == 7:
#     print("g")
# elif num == 8:
#     print("h")
# elif num == 9:
#     print("i")
# elif num == 0:
#     print("j")




# input = input('Write Text: ')
# input = input.lower()
# output = []
# for character in input:
#     number = ord(character) - 96
#     output.append(number)
# print (output)

# c = input("enter your number: ")
# from ctypes.wintypes import CHAR
# import string
# # import this
# x = string.ascii_lowercase.index(c)
# print(x)

# def an():
#     word = input("enter your values: ")

#     for i in word:
#         if type(i) == int:
#             print(string.ascii_lowercase(i))
#         else:
#             print(ord(i) - 96)

# an()

# import string 
# dict = {}

# user_string = input("Enter a string: ")
# mask = ""

# for i, char in enumerate(string.ascii_lowercase):
#     print(i,char)
#     if i == 1:
#      print("a")


# s=input("Enter a value....")
# for i in s:
#     if i.isdigit():
#         print(str(chr(int(i)+97)),end="")
#     else:
#         print(ord(i),end="")

#Final output
