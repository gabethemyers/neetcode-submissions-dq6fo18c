class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashset_s1 = {}
        hashset_s2 = {}

        for char in s1:
            if char in hashset_s1:
                hashset_s1[char] += 1
            else:
                hashset_s1[char] = 1
        
        # every time left goes foward, right has to too? so is it a fixed window? yes and yes

        left = 0

        for right in range(len(s2)):
            current_char = s2[right]
            print(current_char)

            if current_char in hashset_s2:
                hashset_s2[current_char] += 1
            else:
                hashset_s2[current_char] = 1

            if hashset_s1 == hashset_s2:
                return True
            
            
            print(hashset_s2)
            left_char = s2[left]
            if right - left >= (len(s1)-1):
                if hashset_s2[left_char] > 1:
                    hashset_s2[left_char] -= 1
                else:
                    hashset_s2.pop(left_char)
                left += 1
        return False
            
            
        



        