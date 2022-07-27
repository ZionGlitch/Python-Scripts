passwords_file = open("Python-Scripts/Python Challenges/Python Hash/passwords.txt", "r")
passwords = passwords_file.read()

password_list = list(passwords)

masked_list = []
for x in password_list:
        if x.isupper():
            x = "?u"
        elif x.islower():
            x = "?l"
        elif x.isdigit():
            x = "?d"    
        masked_list.append(x)

masked_passwords = ''.join(masked_list)
masked_password_list = list(masked_passwords.split("\n"))

from collections import Counter
counted_masks = Counter(masked_password_list)
print("The top 3 Password Masks are: ")
print("------------------------------")
print(counted_masks.most_common(3))
