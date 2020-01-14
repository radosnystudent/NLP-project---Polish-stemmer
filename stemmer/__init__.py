# -*- coding: utf-8 -*-

from rules import Ruler
import re


def stemming(word : str):
    originalWord = word
    if not word or not _checkWord(word):
        return u'Błędne dane'

    ruler = Ruler()
    word = word.lower()
    steps = list()
    changed = True
    stepsDone = 0
    all_checks = ruler.returnKeys()
    
    while changed:
        changed = False
        for rule in all_checks:
            if len(word) > 4:
                check, changes = ruler.checkRule(word, rule, stepsDone)
                if check != word and check:
                    steps.append([rule, word, check, changes])
                    word = check
                    changed = True
                    if changes != 'nie' and 'prefix' not in rule:
                        stepsDone += 1
            else:
                break

        if not changed or len(word) <= 4:
            check, changes = ruler.checkRule(word, 'general suffix', stepsDone)
            if check != word and check:
                steps.append([rule, word, check, changes])
                word = check
            break

    return _prepareResults(steps, word, originalWord)


def _prepareResults(steps : list, word : str, originalWord : str):
    results = str()
    i = 1
    partOfSpeech = steps[0][0].replace('suffix', '').replace('prefix','')
    separator = '-'*70
    results += f'word: {originalWord}\npart of speech: {partOfSpeech}\n{separator}\n'
    for step in steps:
        results += f'step {str(i)})\n'
        results += f'rule: {step[0]}\nchanged: {step[1]} -> {step[2]}\n'
        results += f'cutted: {step[3]}\n{separator}\n'
        i += 1
    results += f'\nstem: {word}'
    return results

def _checkWord(word : str):
    if len(word.split(" ")) > 1:
        return False
    if not word.isalpha():
        return False
    return True
