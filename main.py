from stats import get_num_words
from stats import fit_character_in_dict
from stats import num_char_dictionary
from stats import print_records
import sys


if len(sys.argv) <2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
else:
	print_records(num_char_dictionary(fit_character_in_dict(sys.argv[1])),sys.argv[1])

