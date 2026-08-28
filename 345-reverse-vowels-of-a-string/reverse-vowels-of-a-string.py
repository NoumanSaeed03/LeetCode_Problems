class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels =  {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left = 0
        right = len(s) - 1
        temp = list(s)

        while left < right:
            if temp[left] in vowels and temp[right] in vowels:
                temp[left], temp[right] = temp[right], temp[left]
                left +=1
                right -=1
            elif temp[left] not in vowels and left < right:
                left +=1
            elif temp[right] not in vowels and left < right:
                right -=1

        return ''.join(temp)