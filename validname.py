"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #4 - Validate Name (validname.py)


Author: Wonjun Lee

Difficulty Level: 3/10

Prompt: Bill is trying to come up with a name for his RACECAR, but he wants to name his 
car so that there are no duplicate characters in the name. Please write a function that 
returns whether a given string input is a valid name or not. 

Constraints: Inputs will consist of only alphanumeric characters. Lowercase and uppercase
characters are considered different. The length of string will be in the range [0, 100] inclusive.

Test Cases:
Input: “AaBbCc1234”     Output: True 
Input: “Aa123a”         Output: False
Input: “qwer12341”      Output: False
"""

class Solution:
    def validateName(self,input):
        # type input: string
        # return: bool
            
        # TODO: Write code below to return a bool with the solution to the prompt
       
        list1 = input
        no_duplicate = []
        i = 0
        while i < len(list1):
            if list1[i] not in no_duplicate and list1[i] != '':
                no_duplicate.append(list1[i])
            i += 1
        if len(no_duplicate) < len(list1):
            return False
        return True
        pass

def main():
    string1 = input()

    tc1 = Solution()
    ans = tc1.validateName(string1)
    print(ans)

if __name__ == "__main__":
    main()