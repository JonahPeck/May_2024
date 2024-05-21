import random



word_list = ["ardvark", "camel", "bacon"]
chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)

print("chosen word is " + chosen_word)

for i in range(word_length):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

#change
print(" ")

for position in range(0, word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)


