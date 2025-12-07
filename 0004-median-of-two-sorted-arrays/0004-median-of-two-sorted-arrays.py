class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numA, numB = nums1, nums2

        if len(numB) < len(numA):
            numA, numB = numB, numA
        
        total_len = len(numA) + len(numB)
        half = total_len // 2

        l, r = 0, len(numA) - 1
        while 1:
            i = (l+r)//2
            j = half - i - 2

            Aleft = numA[i] if i >= 0 else float("-infinity")
            Aright = numA[i + 1] if (i + 1) < len(numA) else float("infinity")
            Bleft = numB[j] if j >= 0 else float("-infinity")
            Bright = numB[j + 1] if (j + 1) < len(numB) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total_len % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1