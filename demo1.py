
# coding: utf-8

# In[1]:


x = 1
type(x)


# In[2]:


x = work
type(x)


# In[3]:


x = 1.1
type(x)


# In[4]:


x = 1j
type(x)


# In[5]:


b1 = True
b2 = False

type(b1)


# In[10]:


b1 = 'True'
b2 = 'False'

type(b1 + b2)


# In[7]:


name1 = 'your name'
type(name1)


# In[8]:


name1 = 'your name'
name2 = 'your name2'
type(name1, name2)


# In[9]:


name1 = 'your name'
name2 = 'your name2'
type(name1 + name2)


# In[11]:


x = 1.0 - 2.0j
type(x)


# In[12]:


print(x)


# In[13]:


print(x.real, x.imag)


# In[14]:


tenth = 10
tenth


# In[15]:


ten = 'ten'
ten


# In[16]:


'Day ' + 1


# In[17]:


'Day ' + str(1)


# In[18]:


True and False


# In[19]:


True or False


# In[20]:


not True


# In[21]:


not False


# In[22]:


True is True


# In[23]:


'a' is 'a'


# In[24]:


'a' is 'b'


# In[25]:


5 is 5


# In[26]:


5 is 1


# In[27]:


i = 3
if i < 3:
    print('less than 3')
elif i < 5:
    print('less than 5')
else:
    print('5 or more')


# In[28]:


i = 3
if i < 3:
    print("less than 3")
elif i < 5:
    print("less than 5")
else:
    print("5 or more")


# In[30]:


i = 3
if i < 3:
    print("less than 3")
elif i < 5:
    print('less than 5')
else:
    print("5 or more")


# In[31]:


l = []
l


# In[32]:


l = list()
l


# In[33]:


l = ['a', 'b', 'c']


# In[34]:


1


# In[35]:


l = ['a', 'b', 'c']
l


# In[36]:


l = ['a',6]
l


# In[37]:


l2 = list(l)
l2


# In[38]:


list('abcdef')


# In[39]:


l = []
l.append('b')
l.append('c')
l.insert(1, 56)
l


# In[45]:


l = []
l.append('b')
l.append('c')
l.append('d')
l.insert(-1, 56)
l


# In[43]:


l = []
l.append('b')
l.append('d')
l.insert(1, 56)
l


# In[46]:


for every_letter in l:
    print(every_letter)


# In[47]:


numbers = [6, 5, 3, 8, 4, 2, 5, 4,9]
sum = 0
for val in numbers:
    sum = sum+val
    print("The sum is", sum)


# In[48]:


numbers = [6, 5, 3, 8, 4, 2, 5, 4,9]
sum = 0
for val in numbers:
    sum = sum+val
print("The sum is", sum)


# In[49]:


digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

