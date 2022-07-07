# For context: this is Challenge 1 of the Google Foobar Challenge - it is explained in more detail and provided with an alternative solution here: https://ourcodeworld.com/articles/read/1512/how-to-create-a-dictionary-of-the-reversed-alphabet-to-encode-and-decode-text-with-javascript 

def solution(x):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

#   List the entered encrypted code phrase as an array
    inputArray = list(x)
    
#   Define our solution Array (with reversed letters)
    solutionArray = []
    
#   Check for any non-lowercase characters, 
    for count, letter in enumerate(inputArray):
        if letter in alphabet:
            position_in_array = alphabet.index(inputArray[count])
            opposite_position = len(alphabet) - position_in_array - 1
            opposite_letter = alphabet[opposite_position]

            solutionArray.append(opposite_letter)
        else: 
            solutionArray.append(letter)

    return ''.join(solutionArray)

       
# To run, enter: solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
