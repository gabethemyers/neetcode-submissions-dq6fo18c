class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # if n + m is odd then is just the middle value
        # if n + m is even then it is the the mean between the two values

        # i think I will need left right and mid for both lists?
        # what is it that will let me cut the search space in half?

        half = (len(nums1) + len(nums2)) // 2

        if len(nums1) <= len(nums2):
            a = nums1
            b = nums2
        else:
            a = nums2
            b = nums1
            #perform binary search on nums1
        left = 0
        right = len(a)
        mid = 0

        while left <= right:
            mid = (left + right) // 2
            print("mid: ", mid)

            B_mid = half - mid

            # just partion and compare now?

            a_left, a_right = a[:mid], a[mid:]
            b_left, b_right = b[:B_mid], b[B_mid:]

            print(a_left, a_right)
            print(b_left, b_right)

            # the actual validity condition (a_left max <= b_right min and b_left max <= a_right min)
            # empty partitions need some kind of placeholder value.
            a_left_max = a_left[-1] if a_left else float('-inf')
            b_left_max = b_left[-1] if b_left else float('-inf')
            a_right_min = a_right[0] if a_right else float('inf')
            b_right_min = b_right[0] if b_right else float('inf')


            if a_left_max <= b_right_min and b_left_max <= a_right_min:
                # valid
                print("valid")
                break
            elif a_left_max > b_right_min:
                right = mid - 1
            else:
                left = mid + 1
            print(left, right)
        
    
        # given the mid partition, how do I find the median?
        # I know that mid is for a array, I know that I can get b_mid by doing half - mid
        # 
        print(half - mid)

        B_mid = half - mid

        a_left, a_right = a[:mid], a[mid:]
        b_left, b_right = b[:B_mid], b[B_mid:]


        a_left_max = a_left[-1] if a_left else float('-inf')
        b_left_max = b_left[-1] if b_left else float('-inf')
        a_right_min = a_right[0] if a_right else float('inf')
        b_right_min = b_right[0] if b_right else float('inf')

        if (len(a) + len(b)) % 2 == 0:
            # even
            left_max = 0
            right_min = 0

            if a_left_max < b_left_max:
                left_max = b_left_max
            else:
                left_max = a_left_max
            
        
            if a_right_min > b_right_min:
                right_min = b_right_min
            else:
                right_min = a_right_min

            return (right_min + left_max) / 2




        else:
            # odd
            if a_right_min > b_right_min:
                return b_right_min
            else:
                return a_right_min


            

        
            



