from rules import check_rule

word = input("Podaj wyraz w języku polskim:\n> ")
word = word.lower()

changed = True

all_checks = [
        'plural suffix',
        'diminutive suffix',
        'nouns suffix',
        'verbs suffix',
        'verbs prefix',
        'numerals suffix',
        'infinitive suffix',
        'adjective prefix',
        'adjective suffix',
        'adverbs suffix',
        'general suffix'
]

while changed:
    changed = False
    for rule in all_checks:
        if len(word) > 4:
            check, changes = check_rule(word, rule)
            if check != word and check:
                print(f'rule: {rule}\nword: {word} -> {check}\ncutted:'
                      f'{changes}\n------------')
                word = check
                changed = True
        else:
            break
    if not changed or len(word) <= 4:
        break


print(f'rdzeń: {word}')
