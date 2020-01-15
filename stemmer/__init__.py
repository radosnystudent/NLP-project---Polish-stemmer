# -*- coding: utf-8 -*-

# if line 'from nltk import word_tokenize' generates error about pickle
# first uncomment and run 2 lines below
# import nltk
# nltk.download('punkt')

from rules import Ruler
import re, os
from nltk import word_tokenize

class Stemmer:

    def __init__(self):
        self.word_blacklist = _read_file(['word_blacklist.txt', 'names.txt'])
        self.final_text = str()

    def stemming(self, string : str):
        self.final_text = ''
        words = self._prepare_words(string)
        for word in words:
            self.final_text += _stemming(word)
        return self.final_text


    def _prepare_words(self, string : str):
        """
        function use nltk tokenize to separate words from sentence and make a list
        then all items from list that are not words (digits, comas, etc.) and words that
        are on blacklist are removed from list
        """
        all_words = word_tokenize(string, language='polish')
        words = list()

        for word in all_words:
            if word not in self.word_blacklist and word.isalpha():
                words.append(word)
        return words


def _read_file(files : list):
    """
    function read .txt files that contains words that cannot 
    (or can, but I don't know how :D) be stemmed
    and returns it as list
    """
    arr = list()
    for file in files:
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(THIS_FOLDER, file)

        with open(filename, 'r') as file:
            for line in file:
                arr.append(line.strip())
    return arr

def _stemming(word : str):
    """
    main function in my algorithm based on Porter's algorithm

    *** I assumed that if word is shorter than 4 letters it's stem already (or cannot be stemmed) ***

    main loop runs as long as algorithm is making changes to the word
        1) set flag to false
        2) take every rule (all parts of speech (divided to suffixes and prefixes e.g. noun suffix, verb prefix etc.))
        3) if word's length is smaller than 4 break loop
           if not:
               3.1) both check_suffix_rule and check_prefix_rule returns word after cuts and suffixes/prefixes that were cutted
               3.2) if returned word isn't the same as given (something was cut off) and isn't none:
                    - append [rule, word that was given, returned one, all cutted suffixes/prefixes]
                    - word is changed to the word that was returned from function
                    - if rule isnt applies to prefix or 'nie' wasnt cut off increment steps
                        (that is because there are some special cases e.g when prefix po- was cut off from word 'poważnie', word 'ważnie' 
                        still has suffix -nie to cut but stem after cutting -nie will be 3 letters long. It's special case 
                        that I have to deal with in that way that I hold stepsDone on 0. Then I can force the rule, 
                        that allow algorithm to cut suffix from word and create stem that is 3 not 4 letters long. )
        4) if word's length is smaller than 5 or there were no changes check once more rule called 'general suffix' and break loop
    return results created in another function
    """
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
    """
    function create text contains:
    1) starting word
    2) part of the speech
    3) steps done to get stem 
    4) stem
    (steps 2 and 3 are optionals - e.g. when word is a stem)
    """
    
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
