#!/usr/bin/env python
# coding: utf-8

# In[1]:


# we define a method 
def longest(s, i, j): 
      
    # If there there isn't any substring with more than one character
    if (i == j): 
        return 1
  
    # if the palindrome substring is composed of only two letters
    if (s[i] == s[j] and i + 1 == j): 
        return 2
      
    
    if (s[i] == s[j]): 
        return longest(s, i + 1, j - 1) + 2
  
  
    return max(longest(s, i, j - 1),  
               longest(s, i + 1, j)) 
  
if __name__ == '__main__': 
    s = input()
    n = len(s) 
    print("The length of the longest possible subsequence that can be read in the same way forward and backwards is",  
                  longest(s, 0, n - 1)) 
      
        


# In[ ]:




