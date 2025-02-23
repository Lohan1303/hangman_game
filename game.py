import random as rd

def print_hangman(error, word):
    if error == 0:
        print(
            f'''
        -----------
        |         |
        |          
        |        
        |        
        |
        | {word}
            ''')
    elif error == 1:
        print(
            f'''
        -----------
        |         |
        |         O  
        |       
        |      
        |       
        | {word}
        ''')
    elif error == 2:
        print(
            f'''
        -----------
        |         |
        |         O  
        |         |
        |      
        |       
        | {word}
        ''')
    elif error == 3:
        print(
            f'''
        -----------
        |         |
        |         O  
        |        /|
        |      
        |       
        | {word}
        ''')
    elif error == 4:
        print(
            fr'''
        -----------
        |         |
        |         O  
        |        /|\
        |      
        |       
        | {word}
        ''')
    elif error == 5:
        print(
            rf'''
        -----------
        |         |
        |         O  
        |        /|\
        |        /
        |       
        | {word}
        ''')
    elif error == 6:
        print(
            rf'''
        -----------
        |         |
        |         O  
        |        /|\
        |        / \
        |       
        | {word}
        ''')
        print("You lose!")
    else:
        print("Error: Invalid error number")
        return
    
def random_word():
    words = [
    "Computador",
    "Inteligencia",
    "Aprendizado",
    "Tecnologia",
    "Automacao",
    "Linguagem",
    "Processamento",
    "Banco",
    "Dados",
    "Algoritmo"
    ]

    return rd.choice(words) 

def spaces(word):
    spaces = " ".join(["_" for _ in range(1, len(word) + 1)])
       
    return spaces
    
def start_game():
    
    print('''
    +---------------------------------------------+    
    |               Welcome to Hangman!           |
    +---------------------------------------------+    
        ''')
    
def change_space(word,letter,space_game):
    space_game = space_game.split(' ')
    aux = ''
    for i in range(len(word)):
        if word[i].upper() == letter.upper():
            aux += letter + ' '  
        elif space_game[i] != '_':
            aux += space_game[i] + ' '
        else:
            aux += '_ '
    
    
    return "".join(aux)
    
           

start_game()
word = random_word()
errors = 0
space_game = spaces(word)
letter_list = []
while True:

    print_hangman(errors, space_game)
    
    if '_' not in space_game:
        print("You win! Congratulations!")
        break
    
    letter = input("Enter a letter: ").upper()
    
    if len(letter) > 1:
        if letter == word.upper():
            print("You win! Congratulations!")
            break
        else:
            errors += 1
            print("Wrong word!") 
            continue
    
    if letter in letter_list:
        print("You already entered this letter")
        continue
    else:
        letter_list.append(letter)
    
    
    if letter not in word.upper():
        errors += 1
        if errors == 6:
            print_hangman(errors, space_game)
            print("The right word was:", word) 
            break
    else:   
        space_game = change_space(word,letter,space_game) 
    
    
            








