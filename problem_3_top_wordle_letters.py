import requests  

# Function to get the list of valid Wordle words  
def get_valid_wordle_words():  
    str_words = []  
    words_text = requests.get("https://raw.githubusercontent.com/tabatkins/wordle-list/refs/heads/main/words").content  
    words = words_text.split()  
    for word in words:  
        str_words.append(str(word.decode('ascii')))  
    return str_words  

# all_words will contain a list of all valid words that you can use  
all_words = get_valid_wordle_words()  

def is_valid_word(word):  
    "Check if the word is valid." 
    return word in all_words  

def main(): 
    print("You have 6 attempts to guess a valid 5-letter word.")  
    # Randomly select a word from the list for the user to guess  
    import random  
    target_word = random.choice(all_words)  
    attempts = 6  
    while attempts > 0:  
        guess = input("5-letter guess: ") 
        if len(guess) != 5:  
            print("Word is not five letters.")   
        if not is_valid_word(guess):  
            print("Invalid word.")   
        if guess == target_word:  
            print("You got the word!")  
        feedback = []  
        for i in range(5):  
            if guess[i] == target_word[i]:  
                feedback.append('🟩') 
            elif guess[i] in target_word:  
                feedback.append('🟨')
            else:  
                feedback.append('⬜') 
        print(feedback)  
        attempts -= 1  
        print(f"{attempts} attempts left.")  
    if attempts == 0:  
        print(f"The word was '{target_word}'.")  

if __name__ == "__main__":  
    main()  