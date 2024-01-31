"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""


class Solution:
    def isValid(self, s):
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}

        # Stack to keep track of opening brackets
        stack = []

        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop from the stack (or use a dummy value if empty)
                top_element = stack.pop() if stack else "#"

                # Check if the popped bracket matches the map
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly
        return not stack
