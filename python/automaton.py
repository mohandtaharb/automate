states = {'S', 'A,', 'B', 'B', 'D'}
final_states = {'d'}
symbols = {'0', 'b', '1'}
# 'Matrice' de transition
transitions = {
    'S': {
        '0': 'S',
        'b': 'A'
    },
    'A': {
        'b': 'B',   
    },
    'B': {
        '1': 'C',
    },
    'C': {
        '1': 'D'
    },
    'D': {
        '1': 'D'
    }
}

while True:
    # On met l'état initial à S
    current_state = 'S' 
    word = input("Entrez un mot : ")
    count = 0
    for c in word:
        if c not in symbols:
            print(f"Symbole {c} n'est pas dans l'alphabet. Le mot n'appartient pas au langage")
            exit()
        try:
            current_state = transitions[current_state][c]
        except KeyError:
            print(f"Symbole {c} inattendu à la position {count}. Le mot n'appartient pas au langage")
            exit()
        count += 1

    if current_state in final_states:
        print("Le mot appartient au langage")
    else:
        print("Le mot n'appartient pas au langage")