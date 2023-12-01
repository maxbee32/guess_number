# Caesar Cipher 
# This can that take text as input, 
# replaces each letter with another letter, and outputs the “encoded” message.

shift = 3

encryption =  ""

new_word = input("Please enter a new word \n")

for char in new_word:
    # check if character is an uppercase letter
    if char.isupper():
        # find the position in 0-25
      c_unicode = ord(char)
        
      c_index = ord(char) - ord("A")
        
         # perform the shift
      new_index = (c_index + shift) % 26
        
        # convert to new character
      new_unicode = new_index + ord("A")
        
      new_character = chr(new_unicode)
        
        # append to encrypted string
      encryption = encryption + new_character
  
    else:
        c_unicode = ord(char)
        
        c_index = ord(char) - ord("a")
        
         # perform the shift
        new_index = (c_index + shift) % 26
        
        # convert to new character
        new_unicode = new_index + ord("a")
        
        new_character = chr(new_unicode)
        # since character is not uppercase, leave it as it is
        encryption += new_character
        
            
         
print(f'Plain Text: {new_word} ')

print(f'Encrypted Text: {encryption}')


