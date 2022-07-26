import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self,file_path= "wordfinder.txt"):
        self.file_path = file_path
        self.list_of_words = self.get_word_list()
        print("filepath", self.file_path)
        print("self.list_of_words", self.list_of_words)
        print(f"{len(self.list_of_words)} words read")
    
        


    def get_word_list(self):
        words = open(self.file_path)
        return [word.strip('\n') for word in words]
            

    def random(self):
        return random.choice(self.list_of_words)


word = WordFinder()
print(word.random())