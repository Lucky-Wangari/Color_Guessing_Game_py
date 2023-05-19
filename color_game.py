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
            print("Type {code_length} colors")
            continue
        for color in guess:
            if color not in colors:
                print(f"Invalid color: {color}. try again")
                break
        else:
            break
        
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
            
    for guess_color, real_color in zip(guess,real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
           incorrect_pos += 1
           color_counts[guess_color]
    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to the game, you have {trials} to the guess code..")
    print("The valid colors are", *colors)
    
    code = guess_the_code()
    for attempts in range(1, trials+ 1):
        guess = guess_the_code()
        correct_pos , incorrect_pos = check_code(guess, code)
        
        if correct_pos == code_length:
            print(f"You guessed thr code in {attempts} tries")
            break
        print(f"Correct positions: {correct_pos} | Incorrect Position: {incorrect_pos}")
    else:
        print("You ran out of trials, the code was:", *code)
        
if __name__ == "__main__":
    game()