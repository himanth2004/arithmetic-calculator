#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=int(input())
b=int(input())
operator=input()
if operator=="+":#addition
    print(a+b)
elif operator=="-":#subtraction
    print(a-b)
elif operator=="/":#division
    print(a/b)
elif operator=="*":#multiplication
    print(a*b)
elif operator=="==":#equal
    print(a==b)
elif operator==">>":#right shift
    print(a>>b)
elif operator=="<<":#left shift
    print(a<<b)  
else:#remainder 
    print(a%b)


# In[ ]:




