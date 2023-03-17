from solution import Solution, Interval

def main():
    intervals = [
        Interval(1, 3),
        Interval(2, 4),
        Interval(5, 7),
    ]
    solution = Solution()
    if solution.can_attend_meetings(intervals):
        print("The person can attend all meetings.")
    else:
        print("The person cannot attend all meetings.")

if __name__ == '__main__':
    main()
