#!/usr/bin/env python
# coding: utf-8

# In[1]:


from prose.tutorials import example_image
from prose.blocks import Trim

# our example image
image = example_image()

# Creating and applying the Trim block
trim = Trim(trim=100)
trimmed_image = trim(image)


# In[2]:


import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))

ax1 = plt.subplot(121)
image.show(ax=ax1)
trim.draw_cutout(image)
plt.axis("off")
_ = plt.title("original image (white = cutout)", loc="left")

ax2 = plt.subplot(122)
trimmed_image.show(ax=ax2)
plt.axis("off")
_ = plt.title("trimmed image", loc="left")

