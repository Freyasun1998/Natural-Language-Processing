#!/usr/bin/env python
# coding: utf-8

# In[1]:


#create the data
s1="<s> I am Sam </s>".split(" ")
s2="<s> Sam I am </s>".split(" ")
s3="<s> I am Sam </s>".split(" ")
s4="<s> I do not like green eggs and Ham </s>".split(" ")


# In[3]:


trigram = []
for i in range(len(s1)-2): 
    trigram.append([s1[i], s1[i+1], s1[i+2]])
for i in range(len(s2)-2):
    trigram.append([s2[i], s2[i+1], s2[i+2]])
for i in range(len(s3)-2):
    trigram.append([s3[i], s3[i+1], s3[i+2]])
for i in range(len(s4)-2):
    trigram.append([s4[i], s4[i+1], s4[i+2]])

print(trigram)


# In[4]:


for i in trigram:
    A=len([x for x in trigram if x[0] == i[0] and x[1] == i[1]])
    B=len([y for y in trigram if y[0] == i[0] and y[1] == i[1] and y[2] ==i[2]])
    print(f"P({i[2]}|{i[0]}, {i[1]})={B/A}")

