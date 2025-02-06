def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents


def word_count(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
        
    return count


def char_count(text):
    working_text = text.lower()
    result = {}
    # take every char of the text -> if the char is in the dict, add + 1 -> if it is not, add it and set its value to 1
    for c in working_text:
        if c in result:
            result[c] += 1
        elif c not in result:
            result[c] = 1 
    
    return result
    
def convert_dict_to_list(dict):
    list_of_dict = []
    for key,value in dict.items():
        if key.isalpha():
            char_dict = {"char": key, "num": value}
            list_of_dict.append(char_dict)
    
    return list_of_dict
           
    
def sort_on(dict):
    return dict["num"]
    

frankenstein = main()
count_of_chars = char_count(frankenstein)
list_of_dict = convert_dict_to_list(count_of_chars)
list_of_dict.sort(reverse=True, key=sort_on)
  

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count(frankenstein)} words found in the document")
for dict in list_of_dict:
    print(f"The '{dict["char"]}' character was found {dict["num"]} times")
print("--- End report ---")
