"""
APproach -
1. convert to ascii code

T - O(n)
S - O(1)
"""
class Solution:
    def encode(self, strs: List[str]) -> str:
        encodes = []
        for string in strs:
            encode = []
            for ch in string:
                encode.append(ord(ch))
            encodes.append(encode)
        return str(encodes)

    def decode(self, s: str) -> List[str]:
        print(s)
        decodes = []
        word = ""
        i = 0
        while i < len(s)-1:
            ch = s[i]
            if ch == '[' or ch == ',' or ch == ' ':
                i += 1
            elif ch == ']':
                decodes.append(word)
                word = ""
                i += 1
            else:
                while s[i+1].isdigit() and i < len(s)-1:
                    ch += s[i+1]
                    i += 1
                # print(ch,i)
                word += chr(int(ch))
                i += 1
        return decodes
