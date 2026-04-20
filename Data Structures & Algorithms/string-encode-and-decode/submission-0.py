class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""

        for word in strs:
            enc_str += f'{len(word)}#{word}'

        return enc_str

    def decode(self, s: str) -> List[str]:
        dec_str = []
        i = 0
        j = 0
        
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            dec_str.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return dec_str