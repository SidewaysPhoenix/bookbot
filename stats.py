def main(book_string):
    num_words = book_string.split()
    num_words = len(num_words)
    print(f"Found {num_words} total words")

def counting (book_string):
    lower_everything = book_string.lower()
    a1_to_z26 = {
    }
    for letter in lower_everything:
        if letter in a1_to_z26:
            a1_to_z26[letter] = a1_to_z26[letter] + 1
        else:
            a1_to_z26[letter] = 1  
    return a1_to_z26

def sort_dictionaries(dictionary):
    temp_list = []
    for letter in dictionary:
        temp_dictionary = {}
        number = dictionary[letter]
        temp_dictionary["char"] = letter 
        temp_dictionary["num"] = number
        temp_list.append(temp_dictionary)
    temp_list.sort(key=helper,reverse=True)
    return temp_list 


def helper(stuff_to_help):
    return stuff_to_help["num"]