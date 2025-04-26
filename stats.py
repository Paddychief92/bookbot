def count_words(text):
    words_list = text.split()
    num_words = len(words_list)
    return num_words


def count_characters(text):
    count = {}
    for t in text:
        if t.lower() in count:
            count[t.lower()] += 1
        else:
            count[t.lower()] = 1
    return count


def sorted_dic(dic):
    new_list = []
    for k in dic:
        new_dic = {"char": k, "num": dic[k]}
        new_list.append(new_dic)

    def sort_on(dic):
        return dic["num"]

    new_list.sort(reverse=True, key=sort_on)
    return new_list
