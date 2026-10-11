"""
Idea:
    -> Encode:
    have to find a way to uniquely identify the encryption.
    Like adding \n won't be unique, it has ASCII code

"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            num = ""
            j = i
            while s[j].isnumeric():
                num += s[j]
                j+= 1
            
            i = j + 1
            j = i + int(num)           
            res.append(s[i:j])
            i = j
        return res
