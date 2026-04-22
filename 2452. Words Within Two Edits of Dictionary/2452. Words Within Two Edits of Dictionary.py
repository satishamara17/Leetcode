#
# Problem: 2452. Words Within Two Edits of Dictionary
# Difficulty: Medium
# Link: https://leetcode.com/problems/words-within-two-edits-of-dictionary/submissions/1985445580/?envType=daily-question&envId=2026-04-22
# Language: python3
# Date: 2026-04-22


class TrieNode:
    def __init__(self):
        self.next = {}   # next stores child nodes by character
        self.end = False # end tells whether a dictionary word ends here


class Solution:
    def twoEditWords(self, queries, dictionary):
        root = TrieNode() # root is the trie root

        for w in dictionary:
            node = root # node is used to build trie for current word
            for ch in w:
                if ch not in node.next:
                    node.next[ch] = TrieNode() # creates child node when character path is missing
                node = node.next[ch]           # moves to next trie node
            node.end = True                    # marks end of one dictionary word

        ans = [] # ans stores all valid query words

        for q in queries:
            if self.ok(q, 0, root, 0): # checks whether q can match some dictionary word within 2 edits
                ans.append(q)          # append adds valid query word to result list

        return ans

    def ok(self, w, i, node, diff):
        if diff > 2:
            return False

        if i == len(w):
            return node.end

        ch = w[i] # ch is current query character at index i

        for c, nxt in node.next.items(): # items is used to iterate over character-child pairs in trie
            nd = diff + (c != ch)        # bool becomes 1 for mismatch and 0 for match in Python
            if self.ok(w, i + 1, nxt, nd):
                return True

        return False
