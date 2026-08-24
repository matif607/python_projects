import random
import string

from hangman_words import word_list

def get_valid_words(words):
  word = random.choice(words)
  while '_' in word or '-' in word or ' ' in word:
    word = random.choice(words)

  return word.upper()

def hangman():
  word = get_valid_words(word_list)
  word_letters = set(word)
  alphabet = set(string.ascii_uppercase)
  used_letters = set()

  lives = 6

  # getting user input
  while len(word_letters) > 0 and lives > 0:
    # letters used
    # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
    print(f"You have {lives} lives left. you have used these letters:", " ".join(used_letters))

    # what the current word is (ie W - R D)
    words_list = [letter if letter in used_letters else '-' for letter in word]
    print("current word:", " ".join(words_list))
    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
      
      else:
        lives -= 1
        print(f"You have {lives} lives left")
    
    elif user_letter in used_letters:
      print("letter already used. Guess another letter")
    
    else:
      print("letter in word. please guess again")


hangman() 


