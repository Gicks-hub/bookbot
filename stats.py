def get_book_text():
	with open("books/frankenstein.txt") as f:
		file_contents =f.read()
	return file_contents

def main():
	text = get_book_text().split()
	return text

def count_words_in_text(searched_word):
	text = main()
	count = 0
	for word in text:
		if word == searched_word:
			count+=1
	return f"Found {count} total words"

def get_num_words():
	text = main()
	count=0
	for word in text:
		count+=1
	print(f"Found {count} total words")

def fit_character_in_dict():
	book_character = get_book_text().lower()
	alphabet_dict={}
	for character in book_character:
		if character in alphabet_dict:
			alphabet_dict[character] +=1
		else:
			alphabet_dict[character] = 1
	print(alphabet_dict)
	return alphabet_dict

def sort_dict_by_item(dict):
	return dict["num"]


def num_char_dictionary(dict):
	num_char_dict={}
	new_dict_list=[]
	for element in dict:
		if element.isalpha():
			num_char_dict["char"] = element
			num_char_dict["num"] = dict[element]
			new_dict_list.append(num_char_dict)
			print(num_char_dict)
			print(new_dict_list)
	print(new_dict_list)
	return num_char_dict
