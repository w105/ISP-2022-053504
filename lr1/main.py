import operator
import re


def input_file():
    file = open('text.txt', 'r')
    text = file.read()
    print("\nEntered text:\n", text)
    file.close()
    return text


def task(text):
    text = text.lower().replace('?', '.').replace('\n', ' ').replace('!', '.').replace('...', '..')
    sentences = text.split('.')
    while "" in set(sentences):
        sentences.remove("")
    print("\nNumber of sentences:", len(sentences))

    arr_words = text.split()
    print("\nNumber of words: ", len(arr_words))
    print(exec(open("frequency.py").read()))
    print("Average number of words in sentence:", len(arr_words) // len(sentences))

    word = 0
    median_num = 0
    not_repeated = list(set(arr_words))
    dictionary = dict.fromkeys(not_repeated, 0)
    for arr in arr_words:
        dictionary[arr] += 1
    dictionary = dict(sorted(dictionary.items(), key=operator.itemgetter(1)))
    for i in set(dictionary.values()):
        median_num = list(dictionary.values()).count(i)
        if median_num > word:
            word = median_num
            median_num = i
    print("Median number of words:", median_num)

    print("\nDefault values are K = 10 and N = 4.")
    answer = input("Change them? (Yes/No)")
    if answer == "Yes":
        k = int(input("Enter K: "))
        n = int(input("Enter N: "))
    else:
        k = 10
        n = 4
    i = 0
    while k > 0 and i <= len(list(dictionary.values())) - 1:
        i += 1
        flag = list(dictionary.keys())[-i]
        if len(flag) != n:
            continue
        else:
            print(list(dictionary.values())[-i], " - ", list(dictionary.keys())[-i])
            k -= 1
    return sentences


def main():
    text = input_file()
    task(text)


if __name__ == "__main__":
    main()