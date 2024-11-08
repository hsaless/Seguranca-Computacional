from collections import Counter

def letter_counter(cipher_text):
    counter = ""
    for letter in cipher_text:
        if letter.isalpha():
            counter += letter.lower()
    return Counter(counter)

def find_key(cipher_text):
    frequency_pt = "aoesirndtmucplvgfbqhzjxkwy"
    most_likely_keys = []
    ordered_keys = []
    count = letter_counter(cipher_text)
    most_common_letters = [count.most_common(3)[0][0], count.most_common(3)[1][0], count.most_common(3)[2][0]]
    for i in range(3):
        for most_common_letter in most_common_letters:
            most_likely_keys.append((ord(most_common_letter) - ord(frequency_pt[i])) % 26)
        

    aux = Counter(most_likely_keys)
    print(aux)
    for key in aux.most_common():
        ordered_keys.append(key[0])
    return ordered_keys

def likely_messages(cipher_text):
    possible_messages = []
    keys = find_key(cipher_text)

    for k in keys:
        plain_text = ""
        for letter in cipher_text:
            if letter.isalpha():
                if letter.islower():
                    base = ord("a")
                    substitute = (((ord(letter) - base) - k) % 26) + base
                    plain_text += chr(substitute)
                else:
                    base = ord("A")
                    substitute = (((ord(letter) - base) - k) % 26) + base
                    plain_text += chr(substitute)
            else:
                plain_text += letter

        possible_messages.append((plain_text, k))

    return possible_messages




