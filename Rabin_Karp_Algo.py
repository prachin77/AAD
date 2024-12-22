class RabinKarp:
    def __init__(self,string,pattern):
        self.Char_Hash_Code = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
                               "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
                               "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
                               "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                               "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
                               }
        self.string = string.lower()
        self.pattern = pattern.lower()
        self.patternHashCode = 0

    def ComputeHashCode(self,pattern,n,m):
        hashValue = 0
        for i in range(m):
            if pattern[i] in self.Char_Hash_Code:
                # hashValue = hashValue + self.Char_Hash_Code[i]
                hashValue = hashValue + self.Char_Hash_Code[pattern[i]]

        print(f"{pattern} : hashcode {hashValue}") 
        return hashValue

    def CheckPattern(self,window_pattern,pattern):
        count = 0
        for i in range(len(pattern)):
            if window_pattern[i] == pattern[i]:
                count += 1
            elif window_pattern[i] != pattern[i]:
                print("pattern did not match")
                break

        if count == len(pattern):
            print("pattern matched sucessfully")
            return window_pattern
        
        return ""

    def SolveRabinKarp(self):
        n = len(self.string)
        m = len(self.pattern)

        if m > n:
            print("Pattern length is greater than string length")
            return
        
        self.patternHashCode = self.ComputeHashCode(self.pattern,n,m)
        print(f"hash code for pattern : {self.patternHashCode}")  

        window_pattern = ""
        for i in range(n-m):
            for j in range(m):
                window_pattern += self.string[i+j]
            print(f"window pattern : {window_pattern}")
            Window_Hash_Code = self.ComputeHashCode(window_pattern,n,m)
            if self.patternHashCode == Window_Hash_Code:
                isPatternMatch = self.CheckPattern(window_pattern,self.pattern)
                if isPatternMatch != "":
                    print(f"pattern found at index {i}")
            window_pattern = ""

                

if __name__ == "__main__":
    string = "abcdaabcdde"
    pattern = "aab"
    rk = RabinKarp(string,pattern)
    rk.SolveRabinKarp()