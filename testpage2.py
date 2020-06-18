

txt_files = open('praise_song_for_the_day.txt') 
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
    print(key.rjust(20) , "|", poem_words[key], '*' * poem_words[key] ) 


########################## Remove Stop Words####################
  
  #def remove_from_list(list_of_items, item_to_remove):
   # items = [item for item in list_of_items if item is not item_to_remove] # Only add item to new list if item is not the item we want to remove
    #return items

    #def remove_from_list(list_of_items, item_to_remove):
     #   newlist = []
      #  for item in words_list:
       #     if item != words_to_remove:
        #        newlist.append(item)
        #        return newlist




