class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2

        if len(b) < len(a):
            a,b = b,a

        total = len(a)+len(b)
        half = total//2

        l = 0
        r = len(a)-1

        while True:
            mid = (l+r)//2
            j = half-mid-2

            Aleft = a[mid] if mid>= 0 else float("-infinity")
            Aright = a[mid+1] if mid+1 < len(a) else float("infinity")
            Bleft = b[j] if j >= 0 else float("-infinity")
            Bright = b[j+1] if j+1 < len(b) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total%2==1:
                    return min(Bright, Aright)
                return (max(Aleft, Bleft) + min(Aright, Bright))/2
            
            elif Aleft > Bright:
                r = mid-1
            else:
                l = mid+1