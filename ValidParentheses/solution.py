class Solution:
    def isValid(self, s: str) -> bool:
        # Create a dictionary mapping each closing character to its corresponding opening character
        closing_to_opening_map = {")": "(", "]": "[", "}": "{"}
        
        # Create an empty list to store opening characters
        stack = []
        
        # Iterate over each character in the input string
        for c in s:
            # If the character is a closing character
            if c in closing_to_opening_map:
                # Check if there is a corresponding opening character at the top of the stack
                if stack and closing_to_opening_map[c] == stack[-1]:
                    # If there is, pop it off the stack and continue iterating
                    stack.pop()
                else:
                    # If there isn't, the string is not valid
                    return False
            else:
                # If the character is an opening character, append it to the stack
                stack.append(c)
        
        # If the stack is empty, all opening characters have been matched with their corresponding closing characters
        # and the string is valid. Otherwise, it is not valid.
        return True if not stack else False
