import numpy as np

class TextBreaker:

    def __init__(self, text:str,total_length:int, row_length:int):
        self.text = text
        self.total_length = total_length
        self.row_length = row_length        
        self.rows = []

        #Breaks the text into words
        self.words = self.text.split()

        #Countings
        self.word_count = len(self.words)
        self.char_count = len(self.text)
        self.words_lenght = [len(word) for word in self.words]

    def __str__(self):
        return self.text
    
    def __getitem__(self, index):
        return self.rows[index]

    def get_number_of_words(self):
        return self.word_count

    def get_number_of_chars(self):
        return self.char_count

    def print_rows(self):
        #Prints the rows
        for row in self.rows:
            print(row)

    def break_to_rows(self):
        #Breaks the text into rows
        for word in self.words:
            if not self.rows: 
                #Initializes the first row
                self.rows.append(word)
            else:
                if len(self.rows[-1])+len(word) < self.row_length:
                    #concatenates in current row
                    self.rows[-1] += " " + word
                else:
                    #Initializes a new row with the current word
                    self.rows.append(word)                    
        return self.rows
    
    