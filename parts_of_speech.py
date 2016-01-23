class Noun:
    def __init__(self, noun, singular_genitive, gender, english):
        self.noun = noun
        self.singular_genitive = singular_genitive
        self.gender = gender
        self.english = english

    def test(self, given, aspects):
        response = input("What is the " + separate_by_commas(aspects) + " for " + getattr(self, given) + "? ").split()
        assert len(response) == len(aspects), "Incomplete answer. Please try again."
        i = 0
        for aspect in aspects:
            if getattr(self, aspect) != response[i]:
                return False
            i += 1
        return True


############################# Helper Functions ################################

import re

def remove_underscores(string):
    match = re.search(r'(.*)_(.*)', string)
    if match is None:
        return string
    else:
        return remove_underscores(match.group(1)) + ' ' + match.group(2)

def separate_by_commas(aspects, called_before= False):
    if len(aspects) == 1:
        if called_before:
            return 'and ' + remove_underscores(aspects[0])
        else:
            return remove_underscores(aspects[0])
    else:
        return remove_underscores(aspects[0]) + ', ' + separate_by_commas(aspects[1:], True)
