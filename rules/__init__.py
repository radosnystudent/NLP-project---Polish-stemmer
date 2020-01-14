# -*- coding: utf-8 -*-

import re
import os

class Ruler:

    def __init__(self):
        self._dictionary = _readFile()

    def checkRule(self, word : str, key : str):
        if "suffix" in key:
            string = [s for s in self._dictionary[key] if word.endswith(s)]
            while string:
                if string:
                    best_match = max(string, key=len)
                    rs = re.sub(rf'{best_match}$', '', word)
                    if len(rs) >= 4:
                        return rs, best_match
                    else:
                        string.remove(best_match)
        else:
            string = [s for s in self._dictionary[key] if word.startswith(s)]
            if string:
                best_match = max(string, key=len)
                return re.sub(rf'^{best_match}', '', word), best_match
        return None, None

    def returnKeys(self):
        return self._dictionary.keys()


def _readFile():
    dictionary = dict()
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(THIS_FOLDER, 'rules.txt')
    with open(filename, 'r') as file:
        for line in file:
            key, values = line.rstrip().split(': ')
            dictionary[str(key)] = values.split(',')
    return dictionary
