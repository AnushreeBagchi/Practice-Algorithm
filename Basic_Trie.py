
#a and add word
basic_trie = {"a": {"d": {"d": {"word_end": True},
                          "word_end": False},
                    "word_end": True
                    }
              }

#hi word
basic_trie1 = {
    "h":{
        "i":{ "word_end": True},
        "word_end": False
    }
}

# print(basic_trie1["h"]["i"]["word_end"])
def is_word(word):
    current_node = basic_trie
    for char in word:
        if char not in current_node:
            return False
        current_node = current_node[char]
    return current_node["word_end"]

            
            

print(is_word("add"))