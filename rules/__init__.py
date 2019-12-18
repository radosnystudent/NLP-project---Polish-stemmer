#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

general_ends = {"u", u"ą", "i", "a", u"ę", "y", u"ę", u"ł", "ia", "ie"} 
diminutive_ends = {"eczek", "eczko", "aczek" ,"iczek", "iszek", "aszek", "uszek", "enek", "ejek", "erek", "ek",\
                   "ak", u"ątko", "ka", "ko", "uchna", "unia", "unio", u"uś", "usia", "uszko", "yk"}
verbs_ends = {"esz", "acz", "asz", "cie", u"eść", u"łem", "amy", "emy", "bym", "by", "esz", u"eńka", u"eś", \
              "asz", u"aść", u"eć", u"ać", "aj", u"ać", "em", "am", u"ał", u"ił", u"ić", u"ąc", u"ować", u"aś"}
nouns_ends = {"anin", "ant", "arka", "arz", "ot", "anka", "zacja", u"zacją", "zacji", "acja", "acji", u"acją", \
              "tach", "anie", "enie", "eniu", "aniu", "yka", "ach", "ami", "nia", "niu", "cia", "ciu", "cji", \
              "cja", u"cją", "ce", "ta", "ba", "czyk", u"czyńca", u"dło", u"ęcie", "el", "ina", "iny", "isia", "isko",\
              "iwo", "izacja", "izm", "jad", "lit", "lnia", "nauta", "nica", "nik", u"ówa", u"ość", "ota", "owce", \
              "owczyni", "owicz", "owiczka", "owiec", u"ówka", u"ówna", "sko", "stwo", u"wóz", "yni", "ysko", "yzm", \
              "yzna", u"żer", u"żerca"}
numerals_ending = {u"naście"}
infinitive_ends = {u"ć", u"yć"}
adjective_starts = {"naj"}
adjective_ends = {"sze", "awy", "szy", "szych", "czny", "owy", "owa", "owe", "ych", "ego", "ej", "aty", "in", "letni", \
                  "liwy", "lubny", "ny", "owate", "owski", "ski", "ysty", "ystyczny", u"żerny", u"złotowy", "iej"}
adverbs_ends = {"awo", "nie", "wie", "rze", "o"}
plural_ends = {u"ów", "om", "ami"}

def check_general_ends(word):
    string = [s for s in general_ends if word.endswith(s)]
    if string:
        best_match = max(string, key=len)
        if word.endswith(best_match):
            return re.sub(rf'{best_match}$', '', word), [best_match]
    return word, []

def check_nouns_ends(word):
    string = [s for s in nouns_ends if word.endswith(s)]
    if string:
        best_match = max(string, key=len)
        if word.endswith(best_match):
            return re.sub(rf'{best_match}$', '', word), [best_match]
    return word, []
        
def check_plural_ends(word):
    string = [s for s in plural_ends if word.endswith(s)]
    if string:
        best_match = max(string, key=len)
        if word.endswith(best_match):
            return re.sub(rf'{best_match}$', '', word), [best_match]
    return word, []

def check_diminutive_ends(word):
    string = [s for s in diminutive_ends if word.endswith(s)]
    if string:
        best_match = max(string, key=len)
        if word.endswith(best_match):
            return re.sub(rf'{best_match}$', '', word), [best_match]
    return word, []

def check_verbs_ends(word):
    string = [s for s in verbs_ends if word.endswith(s)]
    if string:
        best_match = max(string, key=len)
        if word.endswith(best_match):
            return re.sub(rf'{best_match}$', '', word), [best_match]
    return word, []

def check_numerals_ends(word):
    string = [s for s in numerals_ending if word.endswith(s)]
    if string:
        best_match = max(string, key=len)
        if word.endswith(best_match):
            return re.sub(rf'{best_match}$', '', word), [best_match]
    return word, []

def check_ininitive_ends(word):
    string = [s for s in infinitive_ends if word.endswith(s)]
    if string:
        best_match = max(string, key=len)
        if word.endswith(best_match):
            return re.sub(rf'{best_match}$', '', word), [best_match]
    return word, []

def check_adjective(word):
    string1 = [s for s in adjective_ends if word.endswith(s)]
    string2 = [s for s in adjective_starts if word.startswith(s)]
    best_match1, best_match2 = '', ''
    if string1:
        best_match1 = max(string1, key=len)
        if word.endswith(best_match1):
            word = re.sub(rf'{best_match1}$', '', word)
    if string2:
        best_match2 = max(string2, key=len)
        if word.startswith(best_match2):
            word = re.sub(rf'^{best_match2}', '', word)
    return word, [best_match1, best_match2]

def check_adverbs_ends(word):
    string = [s for s in adverbs_ends if word.endswith(s)]
    if string:
        best_match = max(string, key=len)
        if word.endswith(best_match):
            return re.sub(rf'{best_match}$', '', word), [best_match]
    return word, []

rules = {
        'plural': check_plural_ends, 'diminutive': check_diminutive_ends, \
         'nouns': check_nouns_ends, 'verbs': check_verbs_ends, 'numerals': check_numerals_ends, \
         'ininitive': check_ininitive_ends, 'adjective': check_adjective, 'adverbs': check_adverbs_ends, \
         'general': check_general_ends 
         }