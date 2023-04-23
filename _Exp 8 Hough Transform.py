#!/usr/bin/env python
# coding: utf-8

# In[11]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


img = cv2.imread("lined.png")
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


bigger = cv2.resize(img, (350, 300))
cv2.imshow("resize",bigger)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


gray = cv2.cvtColor(bigger, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


img = cv2.GaussianBlur(gray,(3,3),0)
cv2.imshow("Gaussian blur",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


canny_edges = cv2.Canny(bigger,10,150)
plt.figure(1)
cv2.imshow("Canny Edges",canny_edges)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[ ]:


lines = cv2.HoughLinesP(canny_edges,1,np.pi/180,threshold = 80,minLineLength = 50,maxLineGap=250)


# In[ ]:


for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(bigger,(x1,y1),(x2,y2),(255,0,0),3)

cv2.imshow("lines",bigger)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




