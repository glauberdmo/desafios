from .text_breaker import TextBreaker
from faker import Faker
import random
'''
Tests with text_breaker.py
'''
def test_text_breaker_01():
    #Assure that the lentgh of the text is less than row_length

    #Given
    fake = Faker()
    text = fake.text(500)
    print(text)
    row_length = random.randint(40,100)
    
    #Defining the TextBreaker
    text_breaker = TextBreaker(text, row_length)
    
    #Then
    text_breaker.alignment_left()
    for row in text_breaker.rows:
        print(len(row))
        assert len(row) <= row_length

def test_text_breaker_02():
    '''
    TEST: Alignment_left():Assure that the lentgh of the text is less than row_length
    '''

    #Given
    fake = Faker()
    text = fake.text(500)
    print(text)
    row_length = random.randint(40,100)
    
    #Defining the TextBreaker
    text_breaker = TextBreaker(text, row_length)
    
    #Then
    text_breaker.alignment_right()
    for row in text_breaker.rows:
        print(len(row))
        assert len(row) <= row_length        

def test_text_breaker_03():
    '''
    TEST: Alignment_justify():Assure that the lentgh of the text is equal than row_length
    '''
    #Given
    fake = Faker()
    text = fake.text(500)
    print(text)
    row_length = random.randint(40,100)
    
    #Defining the TextBreaker
    text_breaker = TextBreaker(text, row_length)
    
    #Then
    text_breaker.alignment_justify()
    for row in text_breaker.rows:
        print(len(row))
        assert len(row) == row_length

def test_text_breaker_04():
    '''
    TEST: _break_to_rows():Assure that the lentgh of the text is less than row_length
    '''
    #Given
    fake = Faker()
    text = fake.text(500)
    print(text)
    row_length = random.randint(40,100)
    
    #Defining the TextBreaker
    text_breaker = TextBreaker(text, row_length)
    
    #Then
    text_breaker._break_to_rows()
    for row in text_breaker.rows:
        print(len(row))
        assert len(row) <= row_length

def test_text_breaker_05():
    '''
    TEST: Verifies if justify result is always the same, no matter how many times it is called
    Important test to assure the randomness distribution of spaces was frozen
    '''
    #Given
    fake = Faker()
    text = fake.text(500)
    print(text)
    row_length = random.randint(40,100)

    #Defining the TextBreaker
    text_breaker1 = TextBreaker(text, row_length)
    text_breaker2 = TextBreaker(text, row_length)
    
    #Then
    text_breaker1.alignment_justify()
    text_breaker2.alignment_justify()
       
    for rowBreak1, rowbreak2 in enumerate(text_breaker2.rows):
        assert text_breaker1.rows[rowBreak1] == rowbreak2