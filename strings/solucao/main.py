from StringTools.text_breaker import TextBreaker
from StringTools.file_reader import *

TEXT_TO_BREAK = "\\InputTexts\\inputText2.txt"
CHARS_BY_ROW = 40
if __name__ == "__main__":

    # Read the file
    text_to_break = get_string_from_file(TEXT_TO_BREAK)

    #initializes a new TextBreaker object
    OutputText = TextBreaker(text_to_break,CHARS_BY_ROW)    

    #sets alignment
    OutputText.alignment_justify() # options: aligment_left, aligment_right and alignment_justify]

    #Print all broken rows
    OutputText.print_rows()

    #returning by item
    #first_row = print(OutputText[0])
