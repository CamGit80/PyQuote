#dependancies
from pypdf import PdfReader
import random

#intake directory of PDF and init PDF
pdf_direct = input("Input directory of pdf: ")

reader = PdfReader(pdf_direct)




#chose random page and split the page into an array
def split_a_page():
	page = reader.pages[random.randint(1, len(reader.pages))]
	page_extracted= page.extract_text()
	text_split = page_extracted.splitlines()
	return(text_split)


#appends a new list of strings into a speperate array based on length of sentances, were assuming here that if the string is less than 50 characters
#because generally at the end of a paragraph the final sentance is shorter then the other lines of the paragraph
#this should get us a list of paragraphs or at least multiple sentances
def get_paragraph(text):
	looped = 0
	list_item = 0
	paragraph_list = [" x "]

	for item in text:
		if len(text[looped]) > 50:
			paragraph_list[list_item] += text[looped]

		else:
			paragraph_list[list_item] += text[looped]
			#this is done to create a new list item to append into with a very unique substring. we will remove any instance of this substring in the final result
			paragraph_list.append(" x ")
			list_item = list_item + 1
		looped = looped + 1
	return(paragraph_list)


#this will give us a final result that is a good chunk of text
#should also naturally keep from displaying headders or footers
#some pages will be incapable of being pulled from with this solution but this will ensure the result is always a few sentances long
final_result = ""
split_text = split_a_page()

while len(final_result) < 300:
	try:
		result = get_paragraph(split_text)
		final_result = result[random.randint(1, len(result))]
	#this is to make sure we dont get an infinate loop if theres no string equal to 300 characters in the list
	#it will just choose a new page to pull from
	except IndexError:
		split_text = split_a_page()


#gets us the name of the pdf
if "/" in pdf_direct:
	pdf_direct_array = pdf_direct.split('/')
	pdf_name = pdf_direct_array[len(pdf_direct_array) - 1]
else:
	pdf_name = pdf_direct



#gets page number, sometimes PyQuote seems to list the page number as the first list item and other times it displays as the last
#not sure why this is my best guess is it has something to do with how pypdf handles PDFs
page_number = " "
if len(split_text[len(split_text) - 1]) > 5:
	page_number = split_text[0]
else:
	page_number = split_text[len(split_text) - 1]


#finally prints the result with annotation of page and name of the pdf!
print("\"" + final_result.replace(" x ", '') + "\"" + " page: " + page_number + " of pdf: " + pdf_name)




