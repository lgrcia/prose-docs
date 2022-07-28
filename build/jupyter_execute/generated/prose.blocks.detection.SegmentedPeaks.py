#!/usr/bin/env python
# coding: utf-8

# In[1]:


from prose.tutorials import example_image

image = example_image()


# In[2]:


from prose.blocks import SegmentedPeaks

image = SegmentedPeaks()(image)
image.show()


# In[3]:


image = SegmentedPeaks(n_stars=5)(image)
image.show()


# In[4]:


image = SegmentedPeaks(n_stars=50, auto=True, verbose=True)(image)
image.show()


# In[5]:


from tqdm.auto import tqdm

print("threshold optimisation for multiple images")
# -------------------------------------------------
for _ in tqdm(range(3)):
    SegmentedPeaks(n_stars=15, auto=True)(image)


print("threshold optimisation once")
# ----------------------------------
detection = SegmentedPeaks(n_stars=15, reference=image)

for _ in tqdm(range(3)):
    detection(image)

