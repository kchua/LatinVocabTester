from parts_of_speech import *
import re

class VocabFile:
    def __init__(self, path):
        f = open(path, 'r')
        self.vocab_list = []
        line = f.readline()
        while line != '':
            #print(line)
            self.vocab_list.append(create_noun(line))
            line = f.readline()
        assert self.vocab_list != [], ".txt file is empty!"

    def test(self, aspect, given, f=lambda x: True):
        for word, _ in self.filter(f).items():
            if word.test(aspect, given):
                print("Correct!")
            else:
                print("Incorrect! The correct answer is: " + getattr(word, aspect))
                while True:
                    try:
                        response = input("Please retype the correct answer to proceed: ")
                        assert response == getattr(word, aspect)
                        break
                    except AssertionError:
                        print("Invalid. Please try again")

    def filter(self, f):
        '''Returns words in the vocabulary list that satisfy a condition governed
        by f in the form of a dictionary (for randomization).
        '''
        filtered_dict = {}
        for word in self.vocab_list:
            if f(word):
                filtered_dict[word] = 0
        return filtered_dict

############################# Helper Functions ################################

def create_noun(line):
    match = re.search(r'(\S*)\s+(\S*)\s+(\S*)\s+"([\S\s]+)"', line)
    return Noun(match.group(1), match.group(2), match.group(3), match.group(4))

test = VocabFile('test.txt')
