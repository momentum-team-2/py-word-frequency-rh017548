STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    txt_files = open(file) 
    poem_words = {} # makes an empty dictionary
    for item in txt_files: 
        item = item.lower() # make all letters in file lowercase
        item = item.strip() # takes out the leading spaces in the text
        poem = item.split() # seperates the words by white spaces
    
        for word in poem: # loops over each word in the text
            if word in poem_words: # This checks to see if the word is in the dictionary
                poem_words[word] = poem_words[word] + 1 # If the word is in the dictionary increase the count by 1
            else: 
                poem_words[word] = 1 # if the word is not in the dictionary add it.
  
    for key in (poem_words.keys()): 
        print(key, "|", poem_words[key], '*' * poem_words[key] ) 


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
