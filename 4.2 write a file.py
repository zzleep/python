
text = "Oh no your text is overwritten"

with open('text.txt','a') as file: # Change the second argument to 'a' if you want to append instead of overwrite
    file.write(text)               # Change the second argument to 'w' if you want to overwrite
