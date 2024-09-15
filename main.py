def main():
    book_path = "books/frankenstein.txt"
    book = read_book(book_path)
    word_count = count_words(book)
    char_count = count_characters(book)
    print_report(book_path, word_count, char_count)


def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()

    return file_contents


def count_words(book):
    word_list = book.split()
    
    return len(word_list)


def count_characters(book):
    lower_case_book = book.lower()
    char_counts = {}
    for char in lower_case_book:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    return char_counts


def convert_and_sort(char_count):
    list_of_char_counts = []
    for key, value in char_count.items():
        temp_dict = {"name": key, "count": value}
        list_of_char_counts.append(temp_dict)

    list_of_char_counts.sort(reverse=True, key=sort_on)
    return list_of_char_counts


def sort_on(dictionary):
    return dictionary["count"]


def print_report(book_path, word_count, char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    converted_char_count = convert_and_sort(char_count)

    for entry in converted_char_count:
        if entry["name"].isalpha():
            print(f"The {entry['name']} character was found {entry['count']} times")

    print("--- End report ---")


main()
