#!/usr/bin/env python
# coding: utf-8

# **Exercise 5.2:** Write and test three functions that return the largest, the smallest, and the number of dividables by 3 in a given collection of numbers. Use the algorithm described earlier in the Part 5 lecture :)

# In[68]:


# Your functions
def main():
    """
    a = [2, 4, 6, 12, 15, 99, 100]
    100
    2
    4
    """
    a_k = [2, 4, 6, 12, 15, 99, 100]
    f= max(a_k)
    h= min(a_k)
    print ("largest is",f)
    print("smallest is",h)
    for i in a_k:
        if i%3 == 0:
            print("dividables by 3 are ",i)
    
main()

