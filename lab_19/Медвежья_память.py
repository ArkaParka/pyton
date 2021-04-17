def creating_combinations(passw_len, alph):
    new_passw = []
    passws = ['']
    for i in range(passw_len):
        for passw in passws:
            for letter in alph:
                new_passw += [passw + letter]
        passws = new_passw
        new_passw = []
    return passws


def output_combinations(passwords):
    passwords_length = range(len(passwords))
    for password, i in zip(passwords, passwords_length):
        if not all([letter in password for letter in alphabet]):
            del passwords[i]

    print(' '.join(passwords))


length = int(input('Enter length: '))
alphabet = input('Enter letters: ')
passwords = creating_combinations(length, alphabet)
output_combinations(passwords)
