class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        # Dictionary to count all characters in t
        t_count = Counter(t)
        # Dictionary to count characters in the current window
        window_count = defaultdict(int)
        
        # Number of unique characters in t that need to be present in the window
        required = len(t_count)
        # Number of unique characters in the current window that meet the required frequency
        formed = 0
        
        # (window length, left, right)
        ans = float("inf"), None, None
        
        l, r = 0, 0
        
        while r < len(s):
            char = s[r]
            window_count[char] += 1
            
            # If the current character's count matches the count in t, increment formed
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Try and contract the window till the point where it ceases to be 'desirable'
            while l <= r and formed == required:
                char = s[l]
                
                # Save the smallest window until now
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
         
