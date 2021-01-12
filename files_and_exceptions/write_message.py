filename = "programming.txt"

# open first argument is file we want to open
# second argument is 'w', for write mode, 'r' is for read mode
#'a' is for appened mode, and 'r+' for read and write mode
# no argument opens in read only mode
# python will write file if none exists in 'w' mode, but will erase the file
# if it already exists

# with open(filename, "w") as file_object:
#    file_object.write("i love programming.\n")
#    file_object.write("i love lili and lulu.\n")
# this appends txt document
with open(filename, "a") as file_object:
    file_object.write("i love gummies.\n")
    file_object.write("and i love you.\n")
