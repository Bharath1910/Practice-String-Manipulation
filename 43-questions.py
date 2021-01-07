#1.Write a program in python to check if a Substring is Present in a Given String.
mainstr = input("enter: ")
substr = input("enter: ")

if (mainstr.find(substr) == -1):
    print("NO")

else:
    print("YES")


#2.Write a program in python to check if two strings are anagram or not.
str1 = input("enter: ")
str2 = input("enter: ")
if (sorted(str1) == sorted(str2)):
    print("They are anagram")

else:
    print("They are not anagram")

#3.Write a program in python to count and display vowels in a string.
string=input("Enter string:")
vowels=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
print("Number of vowels are: {}".format(vowels))

#4.Write a program in python to find all duplicate characters in string.

#5.Write a program in python to reverse words in a given String in Python.
print(input("enter: ")[::-1])

#6.Python treats a string as special kind of tuple,if yes,prove it.
#idk

#7. Output = Computer Science 

#8. Output = 5

#9. Output = Computer

#10. Write a Python program to calculate the length of a string
string = input("enter: ")
print(len(string))

#11.Write a Python program to count the character frequency in a string
#idk

#12.Write a Python function that takes a list of words and returns the length of the longest one.
str1 = input("Enter 1st word: ")
str2 = input("Enter 2nd word: ")

if len(str1) > len(str2):
    print("the word '{}' is longer".format(str1))


elif len(str1) < len(str2):
    print("the word'{}' is longer".format(str2))

#13.Write a Python program to remove the nth index character from a nonempty string

word = input("Enter: ")
which = int(input("Enter which number of elements to remove? "))

first = word[:which]
last = word[which+1:]
print(first + last)

#14.Write a Python program to change a given string to a new string where the first and last chars have been exchanged
str1 = input("Enter: ")
print(str1[-1:] + str1[1:-1] + str1[:1])

#15.Write a Python program to count the occurrences of each word in a given sentence
str1 = input("Enter: ")
counts = dict()
words = str1.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)

#16.Write a Python program to remove the characters which have odd index values of a given string
str1 = input("Enter: ")
result = "" 
for i in range(len(str1)):
    if i % 2 == 0:
        result = result + str1[i]
print(result)

#17.Write a Python script that takes input from the user and displays that input back in upper and lower cases
str1 = input("Enter: ")

print(str1.upper())
print(str1.lower())

#18.Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form
items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

#19.Write a Python function to insert a string in the middle of a string
def insert_sting_middle(str, word):
	return str[:2] + word + str[2:]

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))

#20.Write a Python program to sort a string lexicographically
#idk

#21.Write a Python program to remove a newline in Python
str1 = '''replace this string with a multiline string'''
print(str1.replace("\n"," "))

#22.Write a Python program to check whether a string starts with specified characters
str1 = input("Enter: ")
which = input("Enter the first word you need to check: ")

if str1[0] == which:
    print("YES")

else:
    print("NO")

#23.Write a Python program to lowercase first n characters in a string
str1 = input("Enter: ")
fir = int(input("Enter the first n numbers: "))

print(str1[:fir].lower()+str1[fir+1:])

#24.Output - No output.. since the string "python" has no characters of "i"

#25.Output - Error, Since the range function only accept integer values

#26.Output - PYTHON

#27.Output - python /n python /n python /n python /n python /n python

#28. Write a Python program to Check Whether a String is Palindrome or Not
str1 = input("Enter: ")

if str1[::-1] == str1:
    print("YES")

else:
    print("NO")

#29.Write a Python program to Remove Punctuations From a String
str1 = input("Enter: ")
print(str1.replace(',',' '))


#30.Write a Python program to Sort Words in Alphabetic Order of a string
str1 = input("Enter: ")

lis = []
for i in str1:
    lis.append(i)

print(sorted(lis))

#31.Yes

#32.Output - aeioubcd

#33.Output - Xyz DEF

#34.Output - *       python       *

#35.Output - 5

#36.Output - Hello python and java

#37.Output - True

#38.Output - False

#39.Write a program that asks the user to enter a string. The program should then print the following:
str1 = input("Enter: ") 
print("The total number of characters in the string is: {}".format(len(str1)))
print(" ")
print("The string repeated 10 times is:  {}".format(str1*10))
print(" ")
print("The first character of the string is:  {}".format(str1[0]))
print(" ")
print("The first three characters of the string is:  {}".format(str1[:3]))
print(" ")
print("The last three characters of the string is:  {}".format(str1[3:]))
print(" ")
print("The string backwards is:  {}".format(str1[::-1]))
print(" ")
print("The string with its first and last characters removed is:  {}".format(str1[1:] + str1[:-1]))
print(" ")
print("The string in all caps is:  {}".format(str1.upper()))
print(" ")
print("The string with every a replaced with an e is:  {}".format(str1.replace('a','e')))
print(" ")
print("The string with every letter replaced by a space is")
for i in range(len(str1)):
    print(" ")

#40.Write a program that, given a string that contains a decimal number, prints out the decimal part of the number. For instance, if given 5.74159, the program should print out .74159
str1 = input("Enter: ")
print('.' + str1.split(".")[1])

#41.Write a program that asks the user to enter two strings of the same length. The program should then check to see if the strings are of the same length. If they are not, the program should print an appropriate message and exit. If they are of the same length, the program should alternate the characters of the two strings. For example, if the user enters xyz and ABC the program should print out AxByCz.
str1 = input("Enter 1st string: ")
str2 = input("Enter 2nd string with same length as 1st string: ")

if len(str1) != len(str2):
    print("enter 2nd string with same length as 1st string ")

else:
    x = list(zip(str1,str2))
    for a,b in x:
        print(a,b,end=' ')

#42.Write a program that asks the user to enter their name in lowercase and then capitalizes the first letter of each word of their name
str1 = input("Enter your name in lowercase: ")
print(str1.title())

#43.Write a program that asks the user to enter a string, then prints out each letter of the string doubled and on a separate line
str1 = input("Enter: ")

for i in str1:
    print(i*2)
    

