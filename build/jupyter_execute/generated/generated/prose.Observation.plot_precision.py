#!/usr/bin/env python
# coding: utf-8

# In[1]:


from prose import Observation
from prose.tutorials import example_phot

obs = Observation(example_phot)
obs.plot_precision()

