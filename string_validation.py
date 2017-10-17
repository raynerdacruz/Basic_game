user_input = " a3?"

new_string = ""

permitted_characters = " abcdefghijklmnopqrstuvwxyz"

for character in user_input: # get each character from the user_input string
    for char in permitted_characters: # get each character from the permitted characters


        if character == char:
            new_string += character
            break
        elif character != char and char == 'z':
            pass


print new_string



