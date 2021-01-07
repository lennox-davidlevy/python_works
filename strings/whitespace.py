first_name = "david"
last_name = "levy"

# f-string same as backticks in js
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}"
print(message)

# \n new line \t tab
message = "Languages:\n\tPython\n\tJavascript"
print(message)

# .rstrip() removes whitespace right, .lstrip left, .strip both
favorite_language_right = 'python   '
print(favorite_language_right.rstrip())
favorite_language_left = '    python'
print(favorite_language_left.lstrip())
favorite_language_both = '    python   ' 
print(favorite_language_both.strip())






