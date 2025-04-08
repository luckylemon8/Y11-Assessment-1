import random  

words = ["zebra", "cow", "cloud", "darkness", "scarecrow", "dollop"]  
hangman = random.choice(words)  
blanks = "_" * len(hangman) 

tries = 6 

while tries > 0 and "_" in blanks:  
    print("Current word:", " ".join(blanks))  
    guess = input("Guess a letter: ").lower()  

    if guess in hangman:  
        blanks = "".join([guess if hangman[i] == guess else blanks[i] for i in range(len(hangman))])  
    else:  
        tries -= 1  
        print(f"Incorrect! You have {tries} tries left.")  

if "_" not in blanks:  
    print(f"Congratulations! You've guessed the word: {hangman}")  
else:  
    print(f"Sorry, you've run out of tries. The word was: {hangman}") 








