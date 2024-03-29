# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
# import pandas as pd
#
# student_data_frame = pd.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pd.read_csv("nato_phonetic_alphabet.csv")
phone = {row.letter: row.code for (index, row) in data.iterrows()}
print(phone)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_word = True
while is_word:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phone[letter] for letter in word]
        print(output_list)
        is_word = False
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        is_word = True
