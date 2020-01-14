# -*- coding: utf-8 -*-
from rules import Ruler
import re

def stemming(word : str):
    if not word or not _checkWord(word):
        return u'Błędne dane'

    ruler = Ruler()
    word = word.lower()
    steps = list()
    changed = True

    all_checks = ruler.returnKeys()
 
    while changed:
        changed = False
        for rule in all_checks:
            if len(word) > 4:
                check, changes = ruler.checkRule(word, rule)
                if check != word and check:
                    steps.append([rule, word, check, changes])
                    word = check
                    changed = True
            else:
                break
        if not changed or len(word) <= 4:
            break

    return _prepareResults(steps, word)


def _prepareResults(steps : list, word : str):
    results = str()
    i = 1
    results += f'word: {word}\npart of speech: {steps[0][0]}\n'
    for step in steps:
        results += f'step {str(i)})\n'
        results += f'rule: {step[0]}\nword: {step[1]} -> {step[2]}\n'
        results += f'cutted: {step[3]}\n------------\n'
        i += 1
    results += f'\nstem: {word}'
    return results

def _checkWord(word : str):
    if len(word.split(" ")) > 1:
        return False
    if not word.isalpha():
        return False
    return True

'''
    'plural suffix',
    'diminutive suffix',
    'nouns suffix',
    'verbs suffix',
    'verbs prefix',
    'numerals suffix',
    'infinitive suffix',
    'adjective prefix',
    'adjective suffix',
    'adverbs prefix',
    'adverbs suffix',
    'general suffix'

'''