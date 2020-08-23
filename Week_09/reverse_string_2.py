class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        split = []
        for i in range(0, len(s), k):
            split.append(s[i:i + k])
        for i in range(len(split)):
            if i % 2 == 0:
                split[i] = split[i][::-1]
        return ''.join(split)
