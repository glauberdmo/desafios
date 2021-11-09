from StringTools.text_breaker import TextBreaker
import os.path

if __name__ == "__main__":

    # Path to the file
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_to_open = BASE_DIR + "\\InputTexts\\inputText2.txt"
    
    with open(file_to_open) as file_text:
        text_to_break = file_text.read()


    OutputText = TextBreaker(text_to_break,10000,40)
    OutputText.break_to_rows()
    OutputText.print_rows()
