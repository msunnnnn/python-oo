import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self,file_path= "wordfinder.txt"):
        """takes in a file"""
        self.file_path = file_path
        self.list_of_words = self.get_word_list()

        print(f"{len(self.list_of_words)} words read")

    def get_word_list(self):
        """creates a list of words from file_path"""
        words = open(self.file_path)
        return [word.strip('\n').strip('\ufeff') for word in words]


    def random(self):
        """chooses a random word from list_of_words"""
        return random.choice(self.list_of_words)


word = WordFinder()
print(word.random())


class SpecialWordFinder(WordFinder):
    """In addition to finding a word from WordFinder
        will remove words with blank lines and #"""

    def __init__(self, file_path):
        """Takes in a file"""
        super().__init__(file_path)
        self.list_words = self.get_word_list()


    def get_word_list(self):
        """returns a new list without blanks and #"""
        new_list = super().get_word_list()
        return [word for word in new_list if "#" not in word and word]




word1 = SpecialWordFinder("wordfinder.txt")
print(word1.list_words)


