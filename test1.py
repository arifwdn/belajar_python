t = input()


def add_alpha(alpha):
    ok = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(alpha)):
        ok.append({alphabet[i]: int(alpha[i])})

    return ok


for i in range(int(t)):
    alphabet_value = input()
    alphabet_value = alphabet_value.split(' ')
    alphabet_value = add_alpha(alphabet_value)
    f = {'C'} in alphabet_value
    print(f)
