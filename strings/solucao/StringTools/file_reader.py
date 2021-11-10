import os.path
from pathlib import Path

def get_string_from_file(relative_path:str)->str:   
    # get string from file sugin relative path  
    BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent.absolute()
    file_to_open = BASE_DIR.__str__() + relative_path    
    with open(file_to_open) as file_text:
        return file_text.read()