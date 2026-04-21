#
# Problem: 1722. Minimize Hamming Distance After Swap Operations
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/submissions/1984497786/?envType=daily-question&envId=2026-04-21
# Language: python3
# Date: 2026-04-21


class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)  # n: number of elements

        parent = list(range(n))  # parent: stores parent of each node in union-find

        def find(x):  # find: returns root of x with path compression
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression to flatten tree
            return parent[x]

        def union(x, y):  # union: merges two components
            px = find(x)  # px: root of x
            py = find(y)  # py: root of y
            if px != py:
                parent[py] = px  # attach one root to another

        for a, b in allowedSwaps:  # process all allowed swaps
            union(a, b)  # connect indices

        groups = {}  # groups: root -> list of indices in that component
        for i in range(n):
            root = find(i)  # root: representative of component
            if root not in groups:
                groups[root] = []
            groups[root].append(i)  # collect indices per component

        ans = 0  # ans: minimum hamming distance

        for comp in groups.values():  # comp: list of indices in one component
            freq = {}  # freq: counts of values from source in this component

            for i in comp:
                val = source[i]  # val: value at index i in source
                freq[val] = freq.get(val, 0) + 1  # get(): fetch existing count or 0

            for i in comp:
                val = target[i]  # val: value at index i in target
                if val in freq and freq[val] > 0:
                    freq[val] -= 1  # match found, reduce count
                else:
                    ans += 1  # mismatch contributes to hamming distance

        return ans  # return final answer
