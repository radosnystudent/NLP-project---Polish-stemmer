# -*- coding: utf-8 -*-

from rules import Ruler
import re, os
#import nltk
#nltk.download('punkt')
from nltk import word_tokenize


class Stemmer:

    def __init__(self):
        self.word_blacklist = _read_file('word_blacklist.txt')
        self.final_text = str()

    def stemming(self, string : str):
        words = self._prepare_words(string)

        for word in words:
            self.final_text += _stemming(word)
        return self.final_text


    def _prepare_words(self, string : str):
        all_words = word_tokenize(string)
        words = list()

        for word in all_words:
            if word not in self.word_blacklist and word.isalpha():
                words.append(word)
        return words


def _read_file(file : str):
    arr = list()
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(THIS_FOLDER, file)

    with open(filename, 'r') as file:
        for line in file:
            arr.append(line.strip())
    return arr

def _stemming(word : str):
    originalWord = word
    ruler = Ruler()
    word = word.lower()
    steps = list()
    changed = True
    stepsDone = 0
    all_checks = ruler.return_keys()
    
    if len(word) < 4:
        return _prepareResults([],word, originalWord)

    while changed:
        changed = False
        for rule in all_checks:
            if len(word) >= 4:
                if 'suffix' in rule:
                    check, changes = ruler.check_suffix_rule(word, rule, stepsDone)
                elif 'prefix' in rule:
                    check, changes = ruler.check_prefix_rule(word, rule)
                if check != word and check:
                    if type(changes) is list:
                        changes_str = ','.join(changes)
                    else:
                        changes_str = changes
                    steps.append([rule, word, check, changes_str])
                    word = check
                    changed = True
                    if 'nie' not in changes_str and 'prefix' not in rule:
                        stepsDone += 1
            else:
                break

        if not changed or len(word) <= 4:
            check, changes_str = ruler.check_suffix_rule(word, 'general suffix', stepsDone)
            if check != word and check:
                steps.append([rule, word, check, changes])
                word = check
            break

    return _prepareResults(steps, word, originalWord)

def _prepareResults(steps : list, word : str, originalWord : str):
    
    '''
    function create text contains:
    - starting word
    - part of the speech
    - steps done to get stem 
    - stem
    '''
    
    results = f'word: {originalWord}\n'
    i = 1
    separator = '-'*70
    result_separator = '-'*144
    if steps:
        partOfSpeech = steps[0][0].replace('suffix', '').replace('prefix','')
        if 'general' in partOfSpeech:
            partOfSpeech = 'noun'
        results += f'part of speech: {partOfSpeech}\n{separator}\n'
    for step in steps:
        results += f'step {str(i)})\n'
        results += f'rule: {step[0]}\nchanged: {step[1]} -> {step[2]}\n'
        results += f'cutted: {step[3]}\n{separator}\n'
        i += 1
    results += f'stem: {word}\n{result_separator}\n'
    return results
