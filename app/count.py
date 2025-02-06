from collections import Counter
from emoji import is_emoji
from detect_delimiter import detect

def is_valid_word(word):
    """Process the text and return the number of requests"""
    return any(char.isalpha() for char in word)


class WordCount():
    """Process the text and return the number of words"""

    def __init__(self, text):
        """Initialize the WordCount object"""
        self._text = text

    def get_word_count(self):
        """Get the number of words in the text"""

        return len(self._text)
    
    def split_words(self):
        """Split the text into words detecting the delimiters"""

        self._text = self._text.replace('\r\n', '\n').replace('\r', '\n')
        self._text = self._text.replace('\t', ' ')
        self._text = self._text.replace('\n', ' ')
        
        delimiter = detect(self._text, whitelist=[' ', '-', '|'])
        self._text = self._text.split(delimiter)
    
    def remove_trimming_spaces(self):
        """Remove the trimming space from the text"""
        
        self._text = self._text.strip()

    def remove_non_words(self):
        """Remove non words from the text, numbers, special characters and emojis are considered non words"""

        word_list = []
        for word in self._text:
            if is_emoji(word):
                continue
            elif is_valid_word(word):
                word_list.append(word)
        
        self._text = word_list

    def count_frequency(self):
        """Count the frequency of the words"""

        return Counter(self._text)
    
    def text_processing_pipeline(self):
        """Execute the pipeline to count how many words are in the text and return the count"""
        
        self.remove_trimming_spaces()
        self.split_words()
        self.remove_non_words()
        return self.get_word_count()

if __name__ == "__main__":

    text = """       How are you doing ?
        I am doing great!
        and you 1ola  \U0001F43F    ?     
    """

    text = "How-are-you"
    sentence = WordCount(text)
    sentence.remove_trimming_spaces()
    sentence.split_words()
    sentence.remove_non_words()
    print(sentence._text)
    count = sentence.get_word_count()
    print(count)
    print(Counter(sentence._text))
    
