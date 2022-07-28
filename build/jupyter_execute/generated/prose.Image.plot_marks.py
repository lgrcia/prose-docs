#!/usr/bin/env python
# coding: utf-8

# In[1]:


from prose import archive
import matplotlib.pyplot as plt

# star coordinates
coord = "04 27 01.36232", "-28 12 48.21681"

# getting an archival image for example
field_of_view = [3, 1.5]
image = archive.pos1_image(coord, field_of_view)

# overplotting coord on image
image.show()
plt.title(image.date.date())
image.plot_marks(coord, color="k", ms=15)

