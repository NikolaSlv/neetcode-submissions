class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Move j forward to find the delimiter
            while s[j] != "#":
                j += 1
                
            # Extract the integer length
            length = int(s[i:j])
            
            # Blindly extract the string chunk
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # Jump i to the start of the next chunk
            i = j + 1 + length
            
        return res