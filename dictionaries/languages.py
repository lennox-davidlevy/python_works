# favorite_languages = {
# "jen": "python",
# "john": "python",
# "jack": "go",
# "johnny": "c++",
# "betty": "javascript",
# "tina": "Java",
# "tracey": "mind-grapes",
# "boob": "python",
# "hool": "c",
# "robby": "go",
# "profla": "c++",
# "babab": "javascript",
# "frroola": "Java",
# "jenna": "mind-grapes",
# }
# some_people = ["jim", "jack", "tina", "johnny", "bob"]
# for name in some_people:
# if name in favorite_languages:
# print(f"Thank you {name.title()} for taking the poll!")
# else:
# print(f"Please, {name.title()}, take our poll!")


# def return_favorite_language(name):
#    name = name.lower()
#    language = favorite_languages.get(name, "not available").title()
#    message = f"{name.title()}'s favorite language is {language}!"
#    return message
#
#
# print(return_favorite_language("jimbo"))

# for key, value in favorite_languages.items():
#    print(f"name: {key}, favorite language: {value}")
# for name, language in favorite_languages.items():
#    print(f"{name.title()}'s favorite language is {language.title()}")

# looping through keys is default behavior, but .keys() can also be used
# for name in favorite_languages:
#    print(name)
# for name in favorite_languages.keys():
#    print(name)

# friends = ["john", "tina"]
# for name in favorite_languages:
#    print(f"Hi {name.title()}")
#    if name in friends:
#        language = favorite_languages[name].title()
#        print(f"\t{name.title()} I see you love {language.title()}!")
#
# if "erin" not in favorite_languages.keys():
#    print(f"Erin, please take our poll!")
# for name in sorted(favorite_languages.keys()):
#    print(name)
# print(f"The following languages have been mentioned:")
# will repeat, use set instead
# for language in favorite_languages.values():
#    print(language.title())
# for language in set(favorite_languages.values()):
#    print(language.title())

new_favorite_languages = {
    "jen": ["python", "javascript"],
    "john": ["python", "go", "javascript"],
    "jack": ["go"],
    "johnny": ["c++", "swift,"],
}
# for name, languages in new_favorite_languages.items():
#    print(f"\n{name.title()}'s favorite language(s) are:")
#    for idx, language in enumerate(languages):
#        print(f"\t{idx + 1}: {language.title()}")
new_dictionary = {1: "value", 2: "value", 3: "value", 4: "value"}
# traverse dictionary, first value is key, next is value, must use items() method on dictionary
for key, value in new_dictionary.items():
    print(f"key: {key}")
    print(f"value: {value}")
