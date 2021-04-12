def reverse_words(sentence):
    str_arr = sentence.split(" ")
    str_arr = list(reversed(str_arr))
    reverse_str = ""

    for rev in str_arr:
        reverse_str += rev + " "

    return reverse_str


if __name__ == '__main__':
    word = "Hello World"
    print(word)
    print(reverse_words(word))
