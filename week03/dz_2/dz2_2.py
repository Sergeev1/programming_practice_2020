#!/usr/bin/env python
# coding: utf-8

# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка. (pythontutor.ru, занятие 7, «Переставить min и max»)

# In[8]:


def перестановка_min_max(l):
    ma=max(l)
    mi=min(l)
    l[l.index(ma)]=mi
    l[l.index(mi)]=ma
    print(l, ' - Переставил min и max')


# In[9]:


l=[1,2,3]
перестановка_min_max(l)


# In[ ]:




