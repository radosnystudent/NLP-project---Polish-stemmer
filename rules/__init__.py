#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

_dictionary = {
        'general suffix': ["u", u"ą", "i", "a", u"ę", "y", u"ę", u"ł", "ia",
                           "ie"],
        'diminutive suffix': ["eczek", "eczko", "aczek", "iczek", "iszek",
                              "aszek", "uszek", "enek", "ejek", "erek", "ek",
                              "ak", u"ątko", "ka", "ko", "uchna", "unia",
                              "unio", u"uś", "usia", "uszko", "yk"],
        'verbs suffix': ["esz", "acz", "asz", "cie", u"eść", u"łem", "amy",
                         "emy", "bym", "by", "esz", u"eńka", u"eś", "asz",
                         u"aść", u"eć", u"ać", "aj", u"ać", "em", "am", u"ał",
                         u"ił", u"ić", u"ąc", u"ować", u"aś"],
        'verbs prefix': ["do", "od"],
        'nouns suffix': ["anin", "ant", "arka", "arz", "ot", "anka", "zacja",
                         u"zacją", "zacji", "acja", "acji", u"acją", "tach",
                         "anie", "enie", "eniu", "aniu", "yka", "ach", "ami",
                         "nia", "niu", "cia", "ciu", "cji", "cja", u"cją",
                         "ce", "ta", "ba", "czyk", u"czyńca", u"dło", u"ęcie",
                         "el", "ina", "iny", "isia", "isko", "iwo", "izacja",
                         "izm", "jad", "lit", "lnia", "nauta", "nica", "nik",
                         u"ówa", u"ość", "ota", "owce", "owczyni", "owicz",
                         "owiczka", "owiec", u"ówka", u"ówna", "sko", "stwo",
                         u"wóz", "yni", "ysko", "yzm", "yzna", u"żer",
                         u"żerca"],
        'numerals suffix': [u"naście"],
        'infinitive suffix': [u"ć", u"yć"],
        'adjective suffix': ["sze", "awy", "szy", "szych", "czny", "owy",
                             "owa", "owe", "ych", "ego", "ej", "aty", "in",
                             "letni", "liwy", "lubny", "ny", "owate", "owski",
                             "ski", "ysty", "ystyczny", u"żerny", u"złotowy",
                             "iej"],
        'adjective prefix': ["przed", "naj"],
        'adverbs suffix': ["awo", "nie", "wie", "rze", "o"],
        'plural suffix': [u"ów", "om", "ami"],
}


def check_rule(word, key):
    if "suffix" in key:
        string = [s for s in _dictionary[key] if word.endswith(s)]
        if string:
            best_match = max(string, key=len)
            return re.sub(rf'{best_match}$', '', word), best_match
    else:
        string = [s for s in _dictionary[key] if word.startswith(s)]
        if string:
            best_match = max(string, key=len)
            return re.sub(rf'^{best_match}', '', word), best_match
    return None, None
