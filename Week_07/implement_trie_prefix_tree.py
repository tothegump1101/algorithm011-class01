class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.d
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        tree['#'] = '#'


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.d
        for c in word:
            if c not in tree:
                return False
            tree = tree[c]
        if '#' not in tree:
            return False
        return True


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.d
        for c in prefix:
            if c not in tree:
                return False
            tree = tree[c]
        return True
