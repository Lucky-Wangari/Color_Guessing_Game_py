import random

colors = ["pink", "lilac", "purple", "white", "grey"]
trials = 10
code_length = 4


def find_code():
    code = []
    
    for _ in range(code_length):
        # the colors are limited to a length of 4
        color = random.choice(colors)
        # user to input random colors
        code.append(color)
        # the color input is made into a list
    return code

def guess_the_code():
    guess = input("guess: ").lower().split(" ")
    # the guesses will be turned to lower case and put in a list form
    # e.g split will output ["blue", "red", "black"]
    
    while True:
        if len(guess) != code_length:
            print(f"Type {code_length} colors")
            guess = input("guess: ").lower().split(" ")
            continue
        invalid_colors = [color for color in guess if color not in colors]
        if invalid_colors:
            print("Invalid colors:", ", ".join(invalid_colors))
            guess = input("guess: ").lower().split(" ")
            continue
        break
        
    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0
    
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
            
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1
            
    for guess_color in guess:
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1
            
    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to the game, you have {trials} tries to guess the code..")
    print("The valid colors are:", ", ".join(colors))
    
    code = find_code()
    for attempts in range(1, trials + 1):
        guess = guess_the_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == code_length:
            print(f"You guessed the code in {attempts} tries")
            break
        print(f"Correct positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
    else:
        print("You ran out of trials, the code was:", *code)

if __name__ == "__main__":
    game()
pink
    
#     Certainly! Here's an explanation of how the code works:

# 1. The code starts by importing the necessary `random` module and defining some variables:
#    - `colors`: A list of valid colors that can be used in the code.
#    - `trials`: The number of attempts the player has to guess the code.

#    - `code_length`: The length of the code to be guessed.

# 2. The `find_code()` function generates a random code by selecting colors from the `colors` list. It returns the generated code as a list.

# 3. The `guess_the_code()` function prompts the user to enter a guess. The input is converted to lowercase and split into a list of colors. 
# It then enters a loop to validate the guess:
#    - If the length of the guess is not equal to `code_length`, it prompts the user to enter the correct number of colors.
#    - It checks each color in the guess and if any color is not in the `colors` list, it informs the user and asks for a new guess.
#    - If the guess is valid, the loop breaks and the guess is returned as a list.

# 4. The `check_code()` function compares the guess with the actual code and determines the number of correct positions and incorrect positions:
#    - It initializes `color_counts` as an empty dictionary to keep track of color occurrences in the actual code.
#    - It iterates over the colors in the actual code and increments the count for each color in `color_counts`.
#    - It then compares the guess and the actual code color by color using the `zip()` function.
#    - For each matching color in both lists, it increments the count of correct positions and decreases the count for that color in `color_counts`.
#    - Finally, it compares the remaining colors in the guess with the counts in `color_counts` and increments the count of incorrect positions for each matching color.

# 5. The `game()` function is the main game loop:
#    - It provides an introductory message to the player, stating the number of tries available and the valid colors.
#    - It calls `find_code()` to generate a random code.
#    - It enters a loop that allows the player to make guesses within the available number of `trials`.
#    - In each iteration, it calls `guess_the_code()` to get the player's guess and then calls `check_code()` to determine the number of correct and incorrect positions.
#    - If the guess is completely correct (all positions are correct), it prints a success message and breaks out of the loop.
#    - If the player runs out of trials without guessing the code correctly, it prints the actual code.

# 6. Finally, the `if __name__ == "__main__":` block ensures that the `game()` function is only executed if the script is run directly (not imported as a module).

# Overall, the code implements a simplified version of a guessing game where the player tries to guess a randomly generated code using a limited number of attempts. The code validates the user's inputs, provides 
# feedback on the correctness of the guess, and terminates the game when the code is guessed correctly or the player runs out of trials.