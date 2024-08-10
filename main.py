def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        number_words = count_words(file_contents)
        number_char = count_char(file_contents)
        dick_list = dick_lister(number_char)
        sorted_dicks = dick_sorter(dick_list)
        report = reporter(number_words, sorted_dicks)
        print(report)


def count_char(book):
    lower_book = book.lower()
    lower_words = lower_book.split()
    char_dict = {
 'a': 0,
 'b': 0,
 'c': 0,
 'd': 0,
 'e': 0,
 'f': 0,
 'g': 0,
 'h': 0,
 'i': 0,
 'j': 0,
 'k': 0,
 'l': 0,
 'm': 0,
 'n': 0,
 'o': 0,
 'p': 0,
 'q': 0,
 'r': 0,
 's': 0,
 't': 0,
 'u': 0,
 'v': 0,
 'w': 0,
 'x': 0,
 'y': 0,
 'z': 0,
 '.': 0
}
    for key in char_dict:
        for word in lower_words:
            if key in word:
                char_dict[key] += 1
    return char_dict

def dick_lister(dict):
    new_list = []
    pairs = dict.items()
    for p in pairs:
        if p[0].isalpha():
            new_list.append({"letter": p[0], "num": p[1]})
    return new_list


def sort_on(dict):
    return dict["num"]

def dick_sorter(shit):
    shit.sort(reverse=True, key=sort_on)
    return shit


        
def count_words(book):
    count = 0
    words = book.split()
    for word in words:
        if word != ".":
            count += 1
    return count

def reporter(count, shit):
    report = f"--- Begin report of books/frankenstein.txt ---\n{count} words found in the document\n\n"
    for s in shit:
        report += f"The {s.get('letter')} character was found {s.get('num')} times\n"
    report += "--- End report ---"
    return report



main()
