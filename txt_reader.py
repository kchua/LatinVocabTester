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

    def test(self, given, *aspects):
        score, total = 0, 0
        aspects = list(aspects)
        for word, _ in self.filter(lambda x: True).items():
            total += 1
            while True:
                try:
                    is_correct_response = word.test(given, aspects)
                    break
                except AssertionError as e:
                    print(e)
            if is_correct_response:
                    print("Correct!")
                    score += 1
            else:
                print("Incorrect! The correct answer is: " + correct_answer(word, aspects))
                while True:
                    try:
                        response = input("Please retype the correct answer to proceed: ")
                        assert response == correct_answer(word, aspects)
                        break
                    except AssertionError as e:
                        print(e)

        print(str(score) + " out of " + str(total) + " correct.")

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

def correct_answer(word, aspects):
    answer = ""
    for aspect in aspects:
        answer += getattr(word, aspect) + " "
    return answer.strip()

test = VocabFile('test.txt')
test.test('english', 'noun', 'singular_genitive', 'gender')
