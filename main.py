def main():
	book_path = "books/frankenstein.txt"
	text = get_text(book_path)
	dict_count = get_character_count(text)
	num_words = get_word_count(text)
	list_dict = create_list(dict_count)

	print(f"--- Begin report of {book_path} ---")
	print(f"{num_words} words found in the document")
	print()

	for item in list_dict:
		if item["char"] == "\n":
			print(f"The 'newline' character was found {item["num"]} times")
		else:
			print(f"The '{item["char"]}' character was found {item["num"]} times")
	print("--- End report ---")
	
def sort_on(dict):
	return dict["num"]

def create_list(dict):
	list_count = []
	for count in dict:
		list_count.append({"char": count, "num": dict[count]})
	list_count.sort(reverse=True, key=sort_on)
	return list_count

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
