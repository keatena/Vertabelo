
# coding: utf-8

# # Python Sets

# ## Creating sets in Python

# In[93]:


# Creating sets using built-in function
set_one = set((0, "one", (2, 3, 4)))
set_one


# In[94]:


# Creating sets using built-in function
set_two = set("Game of Thrones")
set_two


# In[95]:


# Creating sets using curly braces
set_three = {0, "one", (2, 3, 4)}
set_three


# In[96]:


# Creating sets using curly braces
set_four = {"Game of Thrones"}
set_four


# ## Set size and membership

# In[97]:


# Checking the number of elements in a set
len(set_one)


# In[98]:


# Checking if an element is in a set
0 in set_one


# In[99]:


# Checking if an element is not in a set
0 not in set_one


# ## Adding elements to a set

# In[100]:


# Adding a single element using add() method
my_set = {'a', 'b', 'c'}
my_set.add('d')
my_set


# In[101]:


# Adding multiple elements using update() method
my_set.update('e', 'f', 'g', 'b')
my_set


# In[102]:


# Adding multiple elements of different types (i.e., adding a tuple and another set)
my_set.update(('a', 'h'), {'c', 'i', 'j'})
my_set


# ## Removing elements from a set

# In[103]:


# Using remove() to remove an item that doesn't exist in a set
my_set.remove('o')
my_set


# In[104]:


# Using discard() to remove an item that doesn't exist in a set
my_set.discard('o')
my_set


# In[105]:


# Using pop() to remove and return a random element
print(my_set.pop())
print(my_set)


# In[106]:


# Using clear() to remove all elements from a set
my_set.clear()
my_set


# ## Set Union

# In[107]:


# Initializing sets
first_set = {1, 3, 5, 7, 9}
second_set = {2, 4, 6, 8, 10}


# In[108]:


# Set union using | operator
first_set | second_set


# In[109]:


# Set union using union() method
first_set.union(second_set)


# In[110]:


# Getting a union of a set and a list
first_set.union([2, 4, 6, 8, 10])


# ## Set Intersection

# In[111]:


# Initializing sets
first_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7, 8}
third_set = {4, 5, 9, 10}


# In[112]:


# Performing intersection using & operator
first_set & second_set & third_set


# In[113]:


# Performing inteesection using intersection() method
first_set.intersection(second_set, third_set)


# ## Set Difference

# In[114]:


# Initializing sets
first_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7, 8}


# In[115]:


# Performing difference using - operator
print(first_set - second_set)
print(second_set - first_set)


# In[116]:


# Performing difference using difference() method
print(first_set.difference(second_set))
print(second_set.difference(first_set))


# ## Set Symmetric Difference

# In[117]:


# Initializing sets
first_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7, 8}


# In[118]:


# Performing symmetric difference using ^ operator
first_set^second_set


# In[119]:


# Performing symmetric difference using symmetric_difference() method
first_set.symmetric_difference(second_set)


# ## Update operations

# In[120]:


# Initializing sets
first_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7, 8}


# In[121]:


# Modifying a set by union using update() method
first_set.update(second_set)
first_set


# In[122]:


# Modifying a set by intersection using an operator
first_set &= second_set
first_set


# In[123]:


# Modifying a set by difference using difference_update() method
first_set.difference_update((6, 7, 8))
first_set


# In[124]:


# Modifying a set by symmetric difference using an operator
first_set ^= second_set
first_set

