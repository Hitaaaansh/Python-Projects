import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
db=pandas.read_csv("nato_phonetic_alphabet.csv")
# print(db)

nato_dict={row.letter:row.code for (index,row) in db.iterrows()}
# print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def phonetic():

    user_word=input("Hey so whats your word for nato phonetic \n").upper()
    try:

        words_list=[nato_dict[letter] for letter in user_word]
        print(words_list)

    except KeyError:
        print("Sorry, Only alphabets")
        phonetic()

phonetic()
