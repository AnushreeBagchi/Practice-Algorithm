class TrieNode: 
    def __init__(self):
        self.is_word = False
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True
    def exist(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_word
    
trie = Trie()
word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
for word in word_list:
    trie.add(word)

test_word = ['bear', 'goo', 'good', 'goos']
for word in test_word:
    print("Word exist" if trie.exist(word)== True else "Do not exist")