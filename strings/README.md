## String solution

### Solution description
Was asked to be developed a way to break a string using a char delimiter by row as parameter.</br>
To do that was made a class called TextBreaker with a method to break the string by row
	
### Setup
To run this project first you need to clone the repository:
```
git clone https://github.com/glauberdmo/desafios.git   
```
There are two constants to be assigned:
```
TEXT_TO_BREAK = "\\InputTexts\\inputText2.txt"
CHARS_BY_ROW = 40   
```

The constructor receives the string to be broken and the delimiter
```
OutputText = TextBreaker(text_to_break,40)    
```

Select the alignment of the text
```
OutputText.alignment_justify() 
OutputText.alignment_right()
OutputText.alignment_left() #default
```   

This method will return the string broken by row in your terminal
```
OutputText.print_rows()
```


### Extras

1 - Is possible to access this object as list, there is a magic method implemented🧙‍♂️

```Bash
first_row = OutputText[0]
```

2 - The justify method was implemented using a random distribution 🍀.</br>
<b>BUT DO NOT WORRY</b>, the result printing each time always will be the same, the seed was frozen.
This aproach is cool because increasing the delimiter flats the distribution of the spaces (the number of spaces increases faster than the average of words by row).</br></br>
![](https://memegenerator.net/img/instances/50042869.jpg)