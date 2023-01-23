#!/usr/bin/env python
# coding: utf-8

# In[29]:


from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import os
import tkinter
from tkinter import messagebox
import sys


# In[30]:


n_tifs = len([f for f in os.listdir() 
     if f.endswith('.tif') and os.path.isfile(os.path.join(os.getcwd(), f))])

if n_tifs == 1:
    for file in os.listdir():
        if file.endswith(".tif"):
            filename = file
else:
    window = tkinter.Tk()
    window.wm_withdraw()
    messagebox.showinfo(title="Warning", message="More than 1 .tif in folder")
    sys.exit()


# In[32]:


stack = io.imread(filename)


# In[ ]:


for i in range(len(stack)):
    io.imsave(filename[:-4] + '_' + str(i) + '.tif', stack[i], check_contrast=False)

