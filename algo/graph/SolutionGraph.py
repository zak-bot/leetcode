


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1

        trust_set = set() # We create a set to track what trust originators.
        trust_dict = {}
        for i, j in trust:
            trust_set.add(i)
            if j in trust_dict.keys(): # We count how many times we see the recipient of trust
                trust_dict[j]+=1
            else:
                trust_dict[j]=1

        if len(trust_set) != N-1:
            return -1

        else:
            for i in trust_dict:
                if i not in trust_set and trust_dict[i] == N-1:
                    return i

            return -1


