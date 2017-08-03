
# coding: utf-8

# In[1]:

import ipympl
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib notebook')

from openpiv import tools, process, scaling, filters, validation
import numpy as np
# %matplotlib notebook


# In[2]:

frame_a  = tools.imread('20110919 exp3 x10 stream 568570.TIF')
frame_b  = tools.imread('20110919 exp3 x10 stream 568571.TIF' )


# In[14]:

def update(winsize,overlap,s2n,s2n_method):
    u, v, sig2noise = process.extended_search_area_piv( frame_a.astype(np.int32), frame_b.astype(np.int32), window_size=winsize, overlap=overlap, dt=1.0, search_area_size=64, sig2noise_method=s2n_method )
    x, y = process.get_coordinates( image_size=frame_a.shape, window_size=winsize, overlap=overlap )
    u, v, mask = validation.sig2noise_val( u, v, sig2noise, threshold = s2n )
    # u, v = filters.replace_outliers( u, v, method='localmean', max_iter=10, kernel_size=2)
    # x, y, u, v = scaling.uniform(x, y, u, v, scaling_factor = 1.0 )
    # tools.save(x, y, u, v, mask, 'tutorial-part3.txt' )
    fig,ax = plt.subplots()
    ax.imshow(tools.imread('20110919 exp3 x10 stream 488570.TIF'),cmap=plt.cm.gray,origin='upper')
    ax.quiver(x,np.flipud(y),u/10.,v/10.,scale=10,color='r',lw=3)
    plt.show()
    
# update(winsize=32,overlap=16)



# In[17]:

from ipywidgets import interact, interactive, HBox, VBox, Box
interactive_plot = interact(update, winsize=[32,64,128], overlap=[16,32,64],s2n=(1.0,10.0,0.1),s2n_method=['peak2peak','peak2mean'])
# _ = interact(update, winsize=[32,64,128], overlap=[16,32,64],s2n=(1.0,3.0,0.1))
# interactive_plot.layout.height = '800px'
# interactive_plot


# In[ ]:




# In[ ]:




# In[ ]:



