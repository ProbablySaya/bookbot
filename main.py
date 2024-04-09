def main():
	book_path = "books/frankenstein.txt"
	text = get_text(book_path)
	print(get_word_count(text))
	print(get_character_count(text))


def get_text(path):
	with open(path) as f:
		return f.read()

def get_word_count(text):
	words = text.split()
	return(len(words))

def get_character_count(text):
	dict_character_count = dict()
	lowered_string = text.lower()
	for i in range(0,len(lowered_string)):
		if lowered_string[i] in dict_character_count:
			count = dict_character_count[lowered_string[i]]
			count += 1
			dict_character_count.update({lowered_string[i]: count})
		else:
			dict_character_count.update({lowered_string[i]: 1})
	return dict_character_count 


main()
