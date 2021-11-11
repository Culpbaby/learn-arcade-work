import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():

    # Open file for reading
    dictionary_file = open("dictionary.txt")

    # List to store words.
    dictionary_list = []

    # Loop through each line in the file like a list.
    for line in dictionary_file:
        line = line.strip()

        # Add words to the list.
        dictionary_list.append(line)

    dictionary_file.close()

    print("--- Linear Search ---")

    # Open the book.
    book_file = open("AliceInWonderLand200.txt")

    line_number = 0

    for line in book_file:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            current_list_position = 0
            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != word.upper():
                current_list_position += 1

            if current_list_position == len(dictionary_list):
                print("Line", line_number, "possible misspelled word:", word)

    book_file.close()

    print("--- Binary Search ---")

    book_file = open("AliceInWonderLand200.txt")

    line_number = 0

    for line in book_file:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_list) + 1
            found = False
            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2
                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True
            if not found:
                print("Line", line_number, "possible misspelled word:", word)

    book_file.close()

main()
