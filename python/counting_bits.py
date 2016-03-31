'''
Example:
  For num = 5 you should return [0,1,1,2,1,2].

  Follow up:

  It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
  Space complexity should be O(n).
  Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
  Hint:

  You should make use of what you have produced already.
  Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.Show More Hint 
'''

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0 for n in range(num+1)]
        ptr = 1
        next = 1
        for i in range(1, num+1):
          if( i == next ):
            next = next * 2
            ptr = 1
            result[i] = 1
          else:
            result[i] = result[ptr] + 1
            ptr = ptr + 1
        return result

if __name__ == '__main__':
  s = Solution()
  l = s.countBits(10)
  for i in range(len(l)):
    print l[i]
