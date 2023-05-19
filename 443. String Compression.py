from operator import countOf
class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        count = 1
        while i < len(chars):
            if i + 1 < len(chars) and chars[i] == chars[i+1]:
                count += 1
            else:
                chars[j] = chars[i]
                j += 1
                if count > 1:
                    for digit in str(count):
                        chars[j] = digit
                        j += 1
                count = 1
            i += 1
        return j
