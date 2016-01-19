from parts_of_speech import *
import re

class VocabFile:
    def __init__(self, path):
        f = open(path, 'r')
        self.vocab_list = []
        line = f.readline()
        while line != '':
            self.vocab_list.append(create_noun(line))
            line = f.readline()
        assert self.vocab_list != [], ".txt file is empty!"

    def test(self, aspect, given, filter=lambda x: True):
        for word in self.vocab_list:
            if filter(word):
                word.test(aspect, given)

############################# Helper Functions ################################

def create_noun(line):
    match = re.search(r'(.*)[ ]+(.*)[ ]+(.*)[ ]+"(.*)"', line)
    return Noun(match.group(1), match.group(2), match.group(3), match.group(4))
