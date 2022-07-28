#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[ ]:





# In[5]:


np.array(74)


# In[ ]:





# In[6]:


np.array([1,2,3,4,5])


# In[ ]:





# In[11]:


np.array([[1, 2, 3, 4, 5],[6,7,8,9,10]])


# In[ ]:





# In[12]:


np.array([[1, 2, 3, 4, 5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])


# In[ ]:





# In[13]:


a = np.array([2,1,23,3])


# In[14]:


a.ndim


# In[ ]:





# In[15]:


a.shape


# In[ ]:





# In[16]:


a.size


# In[ ]:





# In[17]:


a.dtype


# In[ ]:





# In[18]:


arr = np.array([1,2,3])
arr


# In[ ]:





# In[20]:


nested_arr = np.array([[1,2,3],[4,5,6]])
nested_arr


# In[ ]:





# In[21]:


type(nested_arr)


# In[ ]:





# In[23]:


list =[[1, 2, 3, 4, 5],[6,7,8,9,10]]


# In[27]:


arr1 = np.array(list)


# In[31]:


arr1.size


# In[ ]:





# In[32]:


arr1.ndim


# In[ ]:





# In[34]:


np.zeros(3)


# In[ ]:





# In[35]:


np.zeros(5,dtype=float)


# In[ ]:





# In[36]:


np.ones(4)


# In[ ]:





# In[39]:


np.ones((3,6), dtype='int')


# In[ ]:





# In[41]:


np.full((3,5), 10)


# In[ ]:





# In[42]:


np.eye(5)


# In[ ]:





# In[45]:


np.arange(2,35,2)


# In[ ]:





# In[47]:


np.arange(1,40,2)


# In[ ]:





# In[48]:


np.linspace(0,1,10)


# In[ ]:





# In[49]:


np.random.normal(10,4,(2,5))


# In[ ]:





# In[50]:


np.random.normal(10,4,(2,5))


# In[ ]:





# In[51]:


np.random.randint(2,10,9)


# In[ ]:





# In[54]:


a = np.arange(0,10)
a


# In[ ]:





# In[56]:


a[4]


# In[ ]:





# In[58]:


a[2:8]


# In[ ]:





# In[59]:


a[-2]


# In[ ]:





# In[61]:


a[3]


# In[ ]:





# In[82]:


a[4::-1]


# In[ ]:





# In[83]:


ar = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


# In[84]:


ar


# In[ ]:





# In[85]:


ar.shape


# In[ ]:





# In[86]:


ar[0]


# In[ ]:





# In[87]:


ar[1]


# In[ ]:





# In[88]:


ar[2]


# In[ ]:





# In[91]:


ar1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
ar1


# In[ ]:





# In[92]:


ar>2


# In[ ]:





# In[93]:


ar[ar>2]


# In[ ]:





# In[94]:


ar = np.random.randint(20, size=(4,5))


# In[ ]:





# In[95]:


ar


# In[ ]:





# In[118]:


array1 = np.random.randint(2,5,4)
array2 = np.random.randint(2,5,4)


# In[ ]:





# In[119]:


array1


# In[ ]:





# In[120]:


array2


# In[ ]:





# In[121]:


array1+array2


# In[ ]:





# In[122]:


array1*array2


# In[ ]:





# In[123]:


array1-array2


# In[ ]:





# In[124]:


array1>array2


# In[ ]:





# In[125]:


array1<array2


# In[ ]:





# In[115]:


arra = np.arange(1,10)
arra


# In[ ]:





# In[116]:


arra.shape


# In[ ]:





# In[129]:


shaped_array = arra.reshape(3,3)


# In[130]:


shaped_array


# In[ ]:





# In[ ]:





# In[ ]:





# In[145]:


array = np.arange(0,9)
array


# In[ ]:





# In[160]:


ar = np.random.randint(9, size=(3,3))
ar


# In[ ]:





# In[156]:


ar = np.random.randint(9, size=(3,2))
ar


# In[ ]:





# In[158]:


ar = np.random.randint(9, size=(4,3))
ar


# In[ ]:




