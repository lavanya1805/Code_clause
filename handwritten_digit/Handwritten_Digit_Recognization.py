#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pylab as pl
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn import svm


# In[2]:


digits = load_digits()


# In[3]:


pl.gray()
pl.matshow(digits.images[14])
pl.show()


# In[4]:


digits.images[14]


# In[5]:


images_and_labels = list(zip(digits.images, digits.target))
plt.figure(figsize = (5,5))
for index, (image,label) in enumerate(images_and_labels[:15]):
    plt.subplot(3, 5, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('%i' % label)


# In[6]:


n_samples  = len(digits.images)
print(n_samples)


# In[7]:


X = digits.images.reshape((n_samples, -1))
y = digits.target


# In[8]:


X_train, X_test, y_train, y_test = train_test_split(X,y)
print(X_train.shape)
print(X_test.shape)


# In[9]:


model_linear = svm.SVC(kernel='linear',degree=3, gamma='scale')
model_linear.fit(X_train,y_train)
y_pred = model_linear.predict(X_test)


# In[10]:


model_linear.score(X_test, y_test)


# In[11]:


model_RBF = svm.SVC(degree=3, gamma = 'scale',kernel='rbf')
model_RBF.fit(X_train, y_train)
y_pred2 = model_RBF.predict(X_test)
model_RBF.score(X_test, y_test)


# In[12]:


from sklearn.metrics import classification_report
predictions = model_linear.predict(X_test)
print(classification_report(y_test,predictions))


# In[ ]:




