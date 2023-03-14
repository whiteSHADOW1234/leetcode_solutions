from solution import Solution

def main():
    s = Solution()
    ransomNote = "aa"
    magazine = "aab"
    print(s.canConstruct(ransomNote, magazine)) # expected output: True
    
    ransomNote = "aa"
    magazine = "ab"
    print(s.canConstruct(ransomNote, magazine)) # expected output: False
    
    ransomNote = "aaa"
    magazine = "aab"
    print(s.canConstruct(ransomNote, magazine)) # expected output: False

if __name__ == "__main__":
    main()
