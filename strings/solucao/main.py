from numpy.core.numeric import outer
from StringTools.text_breaker import TextBreaker
from StringTools.file_reader import *

if __name__ == "__main__":

    # Read the file
    text_to_break = get_string_from_file("\\InputTexts\\inputText2.txt")

    #initializes a new TextBreaker object
    OutputText = TextBreaker(text_to_break,40)    

    #sets alignment
    OutputText.alignment_justify() # options: aligment_left, aligment_right and alignment_justify]

    #Print all broken rows
    OutputText.print_rows()

    #return by item
    print(OutputText[0])
