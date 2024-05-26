import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
word_list = ["ardvark", "camel", "bacon"]
chosen_word = random.choice(word_list)
lives = 6
display = []
word_length = len(chosen_word)

print("chosen word is " + chosen_word)

for _ in range(word_length):
    display += "_"
print(display)



#change
print(" ")
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(0, word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        else:
            lives -= 1
            print(stages[lives])
            if lives == 0:
                break
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
    
    if letter != guess:
        print(stages[lives])

print("You lose")  


dcdicvndivcndoisncos
doicneop