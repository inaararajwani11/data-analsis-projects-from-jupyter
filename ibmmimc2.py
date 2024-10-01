#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


tt=pd.read_csv(r'titanic.csv')
import sweetviz as sv


# In[ ]:


tr=sv.analyze(tt)


# In[ ]:


tr.show_html('titanic.html')


# In[ ]:





# In[ ]:


import pandas as pd
titanic=pd.read_csv(r'titanic.csv')

import dtale
d = dtale.show(titanic)
d.open_browser()


# In[ ]:


import folium


# In[ ]:


la,lo=40.7128,-74.0060
m=folium.Map(location=[la,lo],zoom_start=12)
folium.Marker([la,lo],popup='New York City').add_to(m)
m.save('map.html')


# In[ ]:


m


# In[ ]:


la,lo=23.0225,72.5714
m=folium.Map(location=[la,lo],zoom_start=12)
folium.Marker([la,lo],popup='Ahmadabad  City').add_to(m)
m.save('map.html')


# In[ ]:


m


# In[ ]:




