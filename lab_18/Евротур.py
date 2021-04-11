import re

def possibility_of_meeting_a_letter(words):
    possibility = {}

    letters_count = 0
    for word in words:
        letters_count += len(word)
        for letter in word:
            if letter in possibility:
                possibility[letter] += 1
            else:
                possibility[letter] = 1

    for letter in possibility:
        possibility[letter] /= letters_count

    return possibility


def find_probability():
    known_words = ['hallo', 'klempner', 'das', 'ist', 'fantastisch', 'fluggegecheimen']

    stop_word = input('Введите стоп-слово: ')
    stop_word_length = len(stop_word)

    if not re.match(r'([a-z]+$)', stop_word):
        exit(-1)

    possibility = possibility_of_meeting_a_letter(known_words)
    probability = possibility[stop_word[0]]
    for letter in range(1, stop_word_length):
        probability *= possibility[stop_word[letter]]
    print('Вероятность =', probability)


find_probability()

