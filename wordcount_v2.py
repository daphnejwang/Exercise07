def main():
	input_file = open ("twain.txt")
	corpus = input_file.read()
	split_text = corpus.split()
	word_counts_dict = {}

	for word in split_text:
		# 1 Way
		# word_counts_dict[word] = word_counts_dict.get(word, 0) + 1

		# 2nd Way
		# if word_counts_dict.get(word, 0):
		# 	word_counts_dict[word] += 1
		# else:
		# 	word_counts_dict[word] = 1

		# 3rd Way
		if word in word_counts_dict:
			word_counts_dict[word] +=1
		else:
			word_counts_dict[word] = 1


if __name__ == "__main__"
	main()