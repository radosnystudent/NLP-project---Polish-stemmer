from rules import check_rule


def stemming(word):
    if not word:
        return u'Błędne dane'
    word = word.lower()
    steps = list()
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
                    steps.append([rule, word, check, changes])
                    print(f'rule: {rule}\nword: {word} -> {check}\ncutted:'
                          f'{changes}\n------------')
                    word = check
                    changed = True
            else:
                break
        if not changed or len(word) <= 4:
            break

    results = str()
    i = 1
    for step in steps:
        results += f'step {str(i)})\n'
        results += f'rule: {step[0]}\nword: {step[1]} -> {step[2]}\n'
        results += f'cutted: {step[3]}\n------------\n'
        i += 1
    results += f'\nstem: {word}'
    return results
