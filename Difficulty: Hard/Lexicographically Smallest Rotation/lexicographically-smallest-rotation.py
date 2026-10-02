class Solution:
    def lexiString(self, s: str) -> str:
        n = len(s)
        S = s + s

        i, j, k = 0, 1, 0

        while i < n and j < n and k < n:
            if S[i + k] == S[j + k]:
                k += 1
            elif S[i + k] > S[j + k]:
                i += k + 1
                if i <= j:
                    i = j + 1
                k = 0
            else:
                j += k + 1
                if j <= i:
                    j = i + 1
                k = 0

        ans_idx = min(i, j)
        return s[ans_idx:] + s[:ans_idx]