class Noun:
    def __init__(self, noun, singular_genitive, gender, english):
        self.noun = noun
        self.singular_genitive = singular_genitive
        self.gender = gender
        self.english = english

    def test(self, aspect, given="english"):
        response = input("What is the " + remove_underscores(aspect) + " for " + getattr(self, given) + "? ")
        return getattr(self, aspect) == response

class Preposition:
    def __init__(self, prep, complementary_case, english):
        self.prep = prep
        self.complementary_case = complementary_case
        self.english = english

    def test(self, aspect, given="english"):
        response = input("What is the " + remove_underscores(aspect) + " for " + getattr(self, given) + "? ")
        return getattr(self, aspect) == response

############################# Helper Functions ################################

import re

def remove_underscores(string):
    match = re.search(r'(.*)_(.*)', string)
    if match is None:
        return string
    else:
        return remove_underscores(match.group(1)) + ' ' + match.group(2)
