import rules as rs

word = input("Podaj wyraz w języku polskim:\n> ")
word = word.lower()

changed = True

while changed:
    changed = False
    for rule in rs.rules.keys():
        if len(word) > 5:
            check, changes = rs.rules[rule](word)
            if check != word:
                if changes[1] == '':
                    str_changes = '-' + changes[0]
                else:
                    str_changes = changes[1] + '-\n' + '-' + changes[0]
                print(f'rule: {rule}\nword: {word} -> {check}\nchanges:\n{str_changes}\n------------')
                word = check
                changed = True
        else:
            break
    if not changed or len(word) <= 5:
        break
    
    
print(f'rdzeń: {word}')
