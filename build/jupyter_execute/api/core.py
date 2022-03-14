#!/usr/bin/env python
# coding: utf-8

# In[1]:


from prose.tutorials import image_sample

# loading and showing an example image
image = image_sample("05 38 44.851", "+04 32 47.68")
image.show()


# In[2]:


image.header[0:10] # the 10 first lines


# In[3]:


print(f"pixel scale : {image.pixel_scale:.2f}\nFOV: {image.fov}\nnight: {image.night_date}\n")

