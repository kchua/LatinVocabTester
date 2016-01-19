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

    def test(self, aspect, given, filter=lambda x: True):
        for word in self.vocab_list:
            if filter(word):
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

############################# Helper Functions ################################

def create_noun(line):
    match = re.search(r'(\S*)\s+(\S*)\s+(\S*)\s+"([\S\s]+)"', line)
    return Noun(match.group(1), match.group(2), match.group(3), match.group(4))

test = VocabFile('test.txt')
test.test('noun', 'english', lambda x: x.gender == 'm')
