class Solution:
    def reverseBits(self, n: int) -> int:
        """
        基本思路： 不断获取 n 的最后一个 bit 位，
        然后 n 右移一位，返回值左移一位，补给返回值，
        """
        ans = 0
        for i in range(32):
            last = n & 1  # 获取最后一个 bit
            n >>= 1  # 右移一位
            ans <<= 1 # 给最后一位留出空间
            ans |= last  # 把最后一位给补上去
        return ans
        