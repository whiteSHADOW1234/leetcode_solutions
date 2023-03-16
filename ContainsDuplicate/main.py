from solution import Solution

def main():
    s = Solution()
    nums = [1, 2, 3, 1]
    print(s.containsDuplicate(nums))  # should print True

    nums = [1, 2, 3, 4]
    print(s.containsDuplicate(nums))  # should print False

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(s.containsDuplicate(nums))  # should print True

if __name__ == "__main__":
    main()
