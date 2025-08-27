
import sys
from stats import main
from stats import counting
from stats import sort_dictionaries

try:
    file_path = sys.argv[1]
except Exception as e:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
        
        




def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


numbers_counted = counting(get_book_text(file_path))
sorted_dictionaries = sort_dictionaries(numbers_counted)



print("============ BOOKBOT ============")
print(f"Analyzing book found at {file_path}...")
print("----------- Word Count ----------")
main(get_book_text(file_path))
print("--------- Character Count -------")
for lists in sorted_dictionaries:
   if lists["char"].isalpha():
    print(lists["char"] +": " + str(lists["num"]))
print("============= END ===============")