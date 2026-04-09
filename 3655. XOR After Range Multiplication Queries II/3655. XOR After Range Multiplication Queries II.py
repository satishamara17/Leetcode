#
# Problem: 3655. XOR After Range Multiplication Queries II
# Difficulty: Hard
# Link: https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/submissions/1973739100/?envType=daily-question&envId=2026-04-09
# Language: python3
# Date: 2026-04-09


class Solution:
    def xorAfterQueries(self, nums, queries):
        mod = 10**9 + 7  # modulo used in every multiplication
        n = len(nums)  # length of nums
        b = int(n ** 0.5) + 1  # sqrt threshold to split small k and large k cases

        mul = [1] * n  # final multiplier to be applied on each index
        small = [[] for _ in range(b + 1)]  # buckets for queries having small step k

        for l, r, k, v in queries:  # process each query once
            if k > b:  # large k means this query touches only few indices
                i = l  # current index for direct jumping
                while i <= r:  # visit all affected indices
                    mul[i] = (mul[i] * v) % mod  # apply this query's multiplier directly
                    i += k  # jump by k
            else:
                small[k].append((l, r, v))  # store small-k query for grouped processing later

        for k in range(1, b + 1):  # process each possible small step
            if not small[k]:  # skip if no query uses this k
                continue

            groups = [[] for _ in range(k)]  # groups[rem] stores diff events for one remainder class

            for l, r, v in small[k]:  # handle all queries with this fixed k
                rem = l % k  # only this remainder class is affected
                s = (l - rem) // k  # start position inside the remainder subsequence
                e = (r - rem) // k  # end position inside the remainder subsequence
                groups[rem].append((s, v))  # start multiplying by v from s
                groups[rem].append((e + 1, pow(v, mod - 2, mod)))  # stop effect after e using modular inverse

            for rem in range(k):  # scan each remainder subsequence separately
                if not groups[rem]:  # no updates for this remainder class
                    continue

                groups[rem].sort()  # sort events by subsequence position
                cur = 1  # running product active at current subsequence position
                p = 0  # pointer over sorted events
                t = 0  # position inside this remainder subsequence
                i = rem  # actual index in nums for this subsequence

                while i < n:  # walk through all real indices having this remainder
                    while p < len(groups[rem]) and groups[rem][p][0] == t:  # apply all events starting here
                        cur = (cur * groups[rem][p][1]) % mod  # update running multiplier
                        p += 1  # move to next event
                    mul[i] = (mul[i] * cur) % mod  # apply current small-k contribution to this index
                    i += k  # move to next real index in same remainder class
                    t += 1  # move to next subsequence position

        ans = 0  # final XOR answer

        for i in range(n):  # build final values and XOR them
            val = (nums[i] * mul[i]) % mod  # final value at index i after all queries
            ans ^= val  # include this value in XOR

        return ans  # final XOR of all elements
