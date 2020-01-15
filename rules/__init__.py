# -*- coding: utf-8 -*-

import re
import os


class Ruler:

    def __init__(self):
        """
            the structure of dictionary - key (part of speech) : [list of  suffixes]
        """
        self._rules = _read_file('rules.txt')

    def check_suffix_rule(self, word : str, key : str, stepsDone : int):
        """
        first function takes all suffixes that match with given word, example: in adjective suffix we have -ny but also -czny
        if list isn't empty it takes longest suffix and cut it from word, then have two options:
            1) its first step, so stem can be three or more letters long
            2) its not first step, so stem can be four or more letters long
            (of course it's not working perfectly, but mostly it works well - that was the goal)
                if stem is long enough function returns stem and cutted suffix
                if not, suffix is removed from list, and function takes new best match
        if list is empty - return none
        """
        matched_suffixes = [s for s in self._rules[key] if word.endswith(s)]
        while matched_suffixes:
            if matched_suffixes:
                best_match = max(matched_suffixes, key=len)
                rs = re.sub(rf'{best_match}$', '', word)
                if stepsDone != 0:
                    if len(rs) >= 4:
                        return rs, best_match
                    else:
                        matched_suffixes.remove(best_match)
                else:
                    if len(rs) >= 3:
                        return rs, best_match
                    else:
                        matched_suffixes.remove(best_match)
        return None, None

    def check_prefix_rule(self, word : str, key : str):
        """
        first function check if there is suffix from this part of speech that match with given word
        if not returns none

        takes all prefixes and find the one that match with word 
            cut it, set new, cutted word as core on, because after cut word can have another prefix e.g.
            word - 'niepoważny' is adjective, so first we cut prefix nie-, but then we have to cut po-, because 
            after nie- was cutted, word 'poważny' is still adjective and po- needs to be cut

            if there's no prefixes that would match with word, function returns word and cutted prefixes
        if there were no prefixes returns none
        """
        check_suffix = [s for s in self._rules[key.replace('prefix', 'suffix')] if word.endswith(s)]
        if not check_suffix:
            return None, None
        string = [s for s in self._rules[key]]
        matches = list()
        while True:
            if string:
                best_match = ''.join([s for s in string if word.startswith(s)])
                if len(best_match) > 0:
                    new_word = re.sub(rf'^{best_match}', '', word)
                    matches.append(best_match)
                    string.remove(best_match)
                    word = new_word
                else:
                    break
            else:
                break
        if matches:
            return word, matches
        return None, None

    def return_keys(self):
        return self._rules.keys()


def _read_file(file : str):
    """
    function reads .txt file that contains parts of speech with suffixes and prefixes
    and returns it as dictionary
    """
    rules = dict()
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(THIS_FOLDER, file)
    with open(filename, 'r') as file:
        for line in file:
            key, values = line.rstrip().split(': ')
            rules[str(key)] = values.split(',')
    return rules
