"""
Write a function to find the longest common prefix string amongst
an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        # return an empty string if there's no prefix to find
        if len(strs) == 0:
            return ""
        else:
            prefix = []
            # sort the list of strings alphabetically
            strs = sorted(strs)
            # If there's a common prefix, it must be in both frst and lst
            frst, lst = strs[0], strs[-1]
            # Iterate through the characters of the first string
            for i in range(len(frst)):
                # if the current character index i is within the bounds of the last string and
                # the character at position i is the same in both frst and lst, add to prefix
                if len(lst) > i and lst[i] == frst[i]:
                    prefix.append(lst[i])
                else:
                    # If at any point the characters don't match, it means the common prefix ends there
                    return "".join(prefix)
            return "".join(prefix)
