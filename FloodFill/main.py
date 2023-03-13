from solution import Solution


def main():
    # create a Solution object
    s = Solution()

    # sample input
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2

    # run the floodFill method and print the result
    result = s.floodFill(image, sr, sc, newColor)
    print(result)

    # Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    # The original image is:
    # 1 1 1
    # 1 1 0
    # 1 0 1
    # 
    # Starting from the point (1,1), which has the value 1, we change its color to 2.
    # We then recursively visit its neighbors (1,0) and (2,1) which also have the value 1, 
    # and change their color to 2 as well. This results in the final image:
    # 2 2 2
    # 2 2 0
    # 2 0 1



if __name__ == "__main__":
    main()