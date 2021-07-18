#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[29]:


tickers = ['CRFB3.SA', 'ABEV3.SA']

pf_data = pd.DataFrame()

for t in tickers:
    pf_data[t] = wb.DataReader(t, data_source ='yahoo', start = '2015-8-1')['Adj Close']


# In[31]:


pf_data.tail()


# In[50]:


(pf_data / pf_data.iloc[0] * 100).plot(figsize=(10,5));


# In[33]:


log_retorno = np.log(pf_data / pf_data.shift(1))


# In[34]:


log_retorno.mean() * 250


# In[35]:


log_retorno.cov() * 250


# In[36]:


log_retorno.corr() 


# In[37]:


num_carteira = len(tickers)
num_carteira


# In[38]:


arr = np.random.random(2)
arr


# In[39]:


arr[0] + arr[1]


# In[40]:


pesos = np.random.random(num_carteira)
pesos /=np.sum(pesos)
pesos


# In[41]:


pesos[0] + pesos[1]


# ## Expectativa de retorno

# In[42]:


np.sum(pesos * log_retorno.mean()) * 250


# ## Expectativa  de variancia

# In[43]:


np.dot(pesos.T, np.dot(log_retorno.cov() *250, pesos))


# ## Expectativa de Volatividade

# In[44]:


np.sqrt(np.dot(pesos.T, np.dot(log_retorno.cov() *250, pesos)))


# In[45]:


portifolio_retorno = []
portifolio_volatividade = []
for x in range (1000):
    pesos = pesos = np.random.random(num_carteira)
    pesos /=np.sum(pesos)
    portifolio_retorno.append(np.sum(pesos * log_retorno.mean()) * 250)
    portifolio_volatividade.append(np.sqrt(np.dot(pesos.T, np.dot(log_retorno.cov() *250, pesos))))
    
portifolio_retorno =np.array(portifolio_retorno)
portifolio_volatividade =np.array(portifolio_volatividade)
    
portifolio_retorno, portifolio_volatividade


# In[46]:


portifolio = pd.DataFrame({'Retorno': portifolio_retorno, 'Volatibilidade': portifolio_volatividade})


# In[47]:


portifolio.head()


# In[48]:


portifolio.tail()


# In[49]:


portifolio.plot(x='Volatibilidade', y='Retorno', kind='scatter', figsize=(10,6));
plt.xlabel('Expectativa de Volatibiliade')
plt.ylabel('Expectativa de Retorno')


# In[ ]:




