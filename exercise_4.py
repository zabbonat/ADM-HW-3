#!/usr/bin/env python
# coding: utf-8

# In[13]:


#We create a two dimensional matrix of nxn dimension and we follow a dynamic program approach to get the length on the longest palindrome and display it.
#So, first of all, we create a two dimentional array M[n][n] where n is the string(s) length and we initialize the 
#matrix with 0.

s = input()

n = len(s) 

M = [[0 for _ in range(n)] for _ in range(n)] 

#For example, for our case s= 'dataminingsapienza' we'll have a matrix whose dimensions are 18x18
#M is going to store the length of the longest palindromic subsequence of substring s. 
#We will iterate through the string and when we run into matching letters.
#It starts from the top left element [0,0] and diagonally iterate through to the bottom right element (n,n) where n is 
#the number of elements. 
#The diagonal of the matrix is so filled with 1 because for each character there is a palindrome of size 1.

for i in range(n, -1, -1):
    for j in range(i, n):
        if i==j:                          
             M[i][j] = 1

#Now, if we consider sequences with n>= 3 , it can be consider as the following:

#s[i] = s[j] (the end characters match): M[i][j] will store the length of longest palindrome formed 
#by the remaining characters.(If they are the same it increases the value from the left diagonal with 2)

#s[i] != s[j] (they don't match): M[i][j] will store the maximum of the length of the longest palindrome substring composed
#by the first two characters or the length of longest palindrome formed by the last two characters.

        elif s[i]==s[j]:                  
            M[i][j] = M[i+1][j-1]+2
        elif s[i]!=s[j]:                       
            M[i][j] = max(M[i][j-1], M[i+1][j])
            
#The length of the longest possible subsequence that can be read in the same way forward and backwards is:

longestpalindrome=M[0][-1]
print("The length of the longest possible subsequence that can be read in the same way forward and backwards is", str(longestpalindrome))

#OUTPUT
# s= 'dataminingsapienza'
# The length of the longest possible subsequence that can be read in the same way forward and backwards is 7

