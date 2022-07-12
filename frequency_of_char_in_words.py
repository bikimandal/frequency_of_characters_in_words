import string

                        #DEFINING_FUNCTION#

def frequency_counter_all_char(the_input):
    result = []
    copy_user_input = the_input
    for each_char in the_input:
        i=0
        j=0
        if each_char in string.ascii_lowercase:
            for char in copy_user_input:
                if each_char == char:
                    i += 1
            print(f"{each_char} = {i}")
            result.append(each_char)
            result.append(i)
        elif each_char in string.ascii_uppercase:
            for char in copy_user_input:
                if each_char == char:
                    j += 1

            print(f"{each_char} = {j}")
            result.append(each_char)
            result.append(j)
    return result

def frequency_counter_specifying_char_and_words(sentence, character):
    sentence = sentence.lower()
    character = character.lower()
    copy_of_sentence = sentence
    for char in sentence:
        i=0
        
        for char2 in copy_of_sentence:
            if char == char2:
                i += 1
        return i

                             #MAIN_PROGRAM#             

# user_input = input("Enter a word: ")
# print(frequency_counter_all_char(user_input)) 


x = input("Enter the word ")
y = input("Enter the character ")
print(frequency_counter_specifying_char_and_words(x,y))




