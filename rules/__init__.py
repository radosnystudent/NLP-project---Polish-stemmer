# -*- coding: utf-8 -*-

import re
import os


class Ruler:

    def __init__(self):
        self._dictionary = _read_file('rules.txt')

    def check_suffix_rule(self, word : str, key : str, stepsDone : int):
        string = [s for s in self._dictionary[key] if word.endswith(s)]
        while string:
            if string:
                best_match = max(string, key=len)
                rs = re.sub(rf'{best_match}$', '', word)
                if stepsDone != 0:
                    if len(rs) >= 4:
                        return rs, best_match
                    else:
                        string.remove(best_match)
                else:
                    if len(rs) >= 3:
                        return rs, best_match
                    else:
                        string.remove(best_match)
        return None, None

    def check_prefix_rule(self, word : str, key : str):
        check_suffix = [s for s in self._dictionary[key.replace('prefix', 'suffix')] if word.endswith(s)]
        if not check_suffix:
            return None, None
        string = [s for s in self._dictionary[key]]
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
        return self._dictionary.keys()


def _read_file(file : str):
    dictionary = dict()
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(THIS_FOLDER, file)
    with open(filename, 'r') as file:
        for line in file:
            key, values = line.rstrip().split(': ')
            dictionary[str(key)] = values.split(',')
    return dictionary
