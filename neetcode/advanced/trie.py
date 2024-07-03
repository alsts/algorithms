class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        # Insert all characters of word in Tree
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.word = True  # Mark final character as end of word

    def search(self, word):
        curr = self.root
        # Search all characters of word in Tree
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word  # Check if final char is end of word

    def starts_with(self, prefix):
        curr = self.root
        # Search all characters of prefix in Tree
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


trie = Trie()
trie.insert("apple")
trie.insert("ape")
trie.insert("nope")

print(trie.search("ape"))
print(trie.search("no"))
print(trie.starts_with("no"))
