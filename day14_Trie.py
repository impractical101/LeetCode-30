#submitted by thr3sh0ld
class Trieinit(object):
    def __init__(self):
        self.checkword = False
        self.ls = {}
        
        
class Trie(object):
    def __init__(self):
        self.link = Trieinit()

    def insert(self, word):
        save = self.link
        for i in word:
            if i not in save.ls:
                save.ls[i] = Trieinit()
            save = save.ls[i]
        save.checkword = True

    def search(self, word):
        save = self.link
        for i in word:
            if i not in save.ls:
                return False
            save = save.ls[i]
        return save.checkword

    def startsWith(self, prefix):
        save = self.link
        for i in prefix:
            if i not in save.ls:
                return False
            save = save.ls[i]
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
