# PyQuote
A small python program to pull a random paragraph from a pdf and print it to a terminal


## Requirements
This program requires the python package "pypdf"

> pip install pypdf

## Instructions
When prompted give directory to your pdf

### Some things to note:
The program uses length of the quote in characters to determine if it should display a quote. This means no quote displayed will be less than 300 characters. 
This program also uses length of strings to decide where the end of a paragraph is, using the assumption in English grammar we tend to end paragraphs with less than 50 characters.
This at times results in odd cuts in quotes, this is the best method I could find to reliably seperate paragraphs from strings generated by pypdf
