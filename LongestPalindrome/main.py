from solution import Solution

def main():
    s = "abccccdd"
    sol = Solution()
    longest_palindrome = sol.longestPalindrome(s)
    print("Longest palindrome length:", longest_palindrome)

if __name__ == "__main__":
    main()
