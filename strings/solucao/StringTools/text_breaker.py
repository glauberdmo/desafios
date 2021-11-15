import random
class TextBreaker:

    def __init__(self, text:str, row_length:int):
        self.text = text
        self.row_length = row_length        
        self.rows = []
        
        #Breaks the text into words
        self.words = self.text.split()

        #Countings
        self.word_count = len(self.words)
        self.char_count = len(self.text)
        self.words_lenght = [len(word) for word in self.words]
        
        #verifies if breaks are possible
        if max(self.words_lenght) > self.row_length:
            raise ValueError("There is at least one word with length > than row lenght")

        #breaks rows
        self._break_to_rows()

    def __str__(self)->str:
        return self.text
    
    def __getitem__(self, index)->str:
        return self.rows[index]

    def get_number_of_words(self)->int:
        return self.word_count

    def get_number_of_chars(self)->int:
        return self.char_count

    def print_rows(self)->None:
        #Prints the rows
        for row in self.rows:
            print(row)


    def _break_to_rows(self)->list:
        #Breaks the text into rows
        #empty list
        self.rows = []
        
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
    
    def alignment_justify(self)->str:      
        #rebreaks
        self._break_to_rows()

        #number of spaces to be distributed in those selected rand_positions
        space_left:int = 0 
        rand_position:int = 0

        #Freeze random seed
        random.seed(1)

        for i, row in enumerate(self.rows):
            space_left = self.row_length - len(row)
            current_row = row.split()

            #Assigns the spaces randomly after any word... 
            while space_left != 0:
                rand_position = random.randint(0,len(current_row)-2) #<-except in the last position
                current_row[rand_position] += " "
                space_left -= 1

            #Rejoin the words
            self.rows[i] = ' '.join(current_row)

    def alignment_left(self):
        #rebreaks, do nothing to aligns left
        self._break_to_rows()

    def alignment_right(self):
        #rebreaks
        self._break_to_rows()

        #distributes the spaces at the end of the row
        space_left:int = 0
        for i, row in enumerate(self.rows):
            space_left = self.row_length - len(row)
            self.rows[i] = " "*space_left + row
        return self.rows    

    