# 'open()' function takes one argument: name of file
with open("pi_digits.txt") as file_object:
    # open function returns an object representing the file
    # 'read()' stores content of object in a long string
    contents = file_object.read()
# The keyword 'with' closes the file once access to it is no longer needed
# 'read()' returns the string and an extra empty string at the end, that can
# be mitigated with 'rstrip()'
# print(contents.rstrip())

# with open("../strings/text.txt") as file_object:
#    for idx, line in enumerate(file_object):
#        print(f"Line {idx + 1}: {line.rstrip()}")

# filename = "../strings/text.txt"
#
# with open(filename) as file_object:
#    lines = file_object.readlines()
# test_string = ""
# for line in lines:
#    test_string += f" { line.strip() }"
# print(test_string)

filename = "one_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()
# print(f"{pi_string[:52]}...")
# print(len(pi_string))

birthday = input("enter your birthday, in the form of mddyy: ")
if birthday in pi_string:
    print("your birthday appears in the first million digits of pi!")
else:
    print("your birthday does not appear in pi, loser")
