
# coding: utf-8

# In[16]:

import multiprocessing as mp
import multiprocessing as mp


# In[17]:

print dir(mp)


# In[9]:

def squre(numbers):
    for x in numbers:
        print "Suqre-->"+str(x*x)
def cube(numbers):
    for x in numbers:
        print "cube-->"+str(x*x*x)

if "__main__" == __name__ :
    num =  (i for i in range(100))
    p1 = mp.Process(target=cube ,args=[num])
    p2 = mp.Process(target=squre ,args=[num])
    
    


# In[10]:

print p1


# In[11]:

dir(p1)


# In[15]:

p1.start
p2.start
p1.join
p2.join


# In[ ]:



