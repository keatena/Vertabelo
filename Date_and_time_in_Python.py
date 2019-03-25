
# coding: utf-8

# # How to work with date and time in Python?

# In[1]:


# Starting with the required imports
from datetime import datetime, date, time, timedelta


# ## Current date and time

# In[4]:


# Getting current date
today = date.today()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print ("Today's date is ", today)
print ("\n", "Year:", today.year,
       "\n", "Month:", today.month, 
       "\n","Day:", today.day, 
       "\n","Weekday:", today.weekday(),
       "\n","Weekday (name):", days[today.weekday()])


# In[6]:


# Getting current time
time = datetime.now()
print("It's", time, "now.")
print ("\n", "Time:", datetime.time(time),
       "\n", "Hour:", time.hour, 
       "\n","Minute:", time.minute, 
       "\n","Second:", time.second,
       "\n","Microsecond:", time.microsecond)


# ## Creating datetime object

# In[15]:


# Creating date object
einstein_birthday = date(1879, 3, 14)
print ('Einstein\'s birthday is on {}.'.format(einstein_birthday))


# In[17]:


# Creating datetime object
einstein_birthtime = datetime(1879, 3, 14, 8, 34, 55, 2345)
print ('Einstein was born on {}.'.format(einstein_birthtime))


# In[18]:


einstein_birthday = datetime(1879, 3, 14)
print ('Einstein\'s birthday is on {}.'.format(einstein_birthday))


# ## Comparing datetime objects

# In[19]:


# Comparing times
einstein_birthtime = datetime(1879, 3, 14, 8, 34, 55, 2345)
newton_birthtime = datetime(1643, 1, 4, 15, 55, 4, 15432)
hawking_birthtime = datetime(1942, 1, 8, 22, 13, 43, 78432)


# In[20]:


einstein_birthtime > newton_birthtime


# In[21]:


hawking_birthtime < einstein_birthtime


# In[22]:


einstein_birthday = datetime(1879, 3, 14)
newton_birthday = datetime(1643, 1, 4)
hawking_birthday = datetime(1942, 1, 8)


# In[23]:


einstein_birthday > newton_birthday


# ## Timedelta objects

# In[33]:


# Calculating the difference between two dates
delta = einstein_birthday - newton_birthday
print (delta)
print ('Einstein was born {} years later than Newton.'.format(round(delta.days/365)))


# In[35]:


delta_time = einstein_birthtime - newton_birthtime
print(delta_time)


# In[46]:


# Calculating the difference between two dates with a negative result
einstein_death = datetime(1955, 4, 18)
hawking_birthday = datetime(1942, 1, 8)
delta = hawking_birthday - einstein_death
print(delta)


# In[51]:


# Calculating the date 100 days before Einstein's birth
einstein_100days_before = einstein_birthday + timedelta(days=-100)
print ('Einstein was born 100 days after {}.'.format(einstein_100days_before))


# In[50]:


# Calculating the date 4 weeks after Einstein's birth
einstein_4weeks_after = einstein_birthday + timedelta(weeks=4)
print ('Einstein was 4 weeks old on {}.'.format(einstein_4weeks_after))


# ## Formatting datetime objects

# In[59]:


# Formatting a date object
einstein_birthday = datetime(1879, 3, 14)
print ('Einstein was born on {}.'.format(einstein_birthday))
print ('Einstein was born on {}.'.format(einstein_birthday.strftime('%b %d, %Y')))
print ('Einstein was born on {}.'.format(einstein_birthday.strftime('%a, %B %d, %Y')))
print ('Einstein was born on {}.'.format(einstein_birthday.strftime('%A, %B %d, %Y')))
print ('Einstein was born on {}.'.format(einstein_birthday.strftime('%d.%m.%Y')))
print ('Einstein was born on {}.'.format(einstein_birthday.strftime('%d/%m/%y')))


# In[2]:


# Formatting a time object
meeting_time = datetime.time(datetime (2019, 3, 25, 20, 30))
print ('Meeting starts at {}.'.format(meeting_time))
print ('Meeting starts at {}.'.format(meeting_time.strftime('%H:%M')))
print ('Meeting starts at {}.'.format(meeting_time.strftime('%I:%M %p')))


# ## Converting strings to datetime objects

# In[63]:


# Converting strings to dates
date = datetime.strptime('March 25, 2019', '%B %d, %Y')
print(date)

