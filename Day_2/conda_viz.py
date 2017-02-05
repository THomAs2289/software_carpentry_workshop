
# coding: utf-8

# In[4]:

#display SVG

from IPython.display import SVG


# # Challenge 
# 1. import pygal and pandas
# 2. read Data

# In[13]:

import pandas as pd
import pygal


# In[14]:

health_dat=pd.read_csv('Dem_Health_Full.txt',sep='\t')


# In[16]:

health_dat.head()


# In[17]:

#help(health_dat)
dir (health_dat)


# In[33]:

#health_dat['State']
#health_dat[['State','Poverty']]
#health_dat.loc[0,:]
#health_dat.loc[0,['Population_Density', 'Povert']]
#health_dat.iloc[0,2:4]
health_dat[(health_dat['State']=='AL') |(health_dat['State']=='TX')]


# In[38]:

#cleaning
#health_dat.iloc[3126]
health_dat.fillna(0, inplace=True)
health_dat.iloc[3126]


# In[47]:

# cleaning suicides (a.k.a antidepressants) 
#health_dat.head(6)
health_dat['Suicide'].replace(-1111.1,0,inplace=True)
health_dat.head(70)


# In[48]:

nested_list=[(1,2),(3,4),]
nested_list


# In[49]:

data_for_al=health_dat.loc[health_dat['State']=='AL',                           ['Population_Density','Poverty']]
data_for_al.head()


# In[53]:

lst=[tuple(x) for x in data_for_al.values]
#lst


# In[56]:

#create scatter
scatter_plot=pygal.XY(stroke=False)
scatter_plot.add('AL',lst)
SVG(scatter_plot.render())


# In[57]:

scatter_plot=pygal.XY(stroke=False)
scatter_plot.title='Poor People are Everywhere'

scatter_plot.add('AL',lst)
SVG(scatter_plot.render())


# In[59]:

scatter_plot=pygal.XY(stroke=False, x_title='#People', y_title="#poverty")
scatter_plot.title="Poor People are Everywhere (for real guys it's scary)"
scatter_plot.add('AL',lst)
SVG(scatter_plot.render())


# In[76]:

data_for_tn=health_dat.loc[health_dat['State']=='MO',                           ['Population_Density','Poverty']]
lst1=[tuple(x) for x in data_for_tn.values]
scatter_plot=pygal.XY(stroke=False, x_title='#People', y_title="#poverty")
scatter_plot.title="Poor People are Everywhere (Tennesse edition)"
scatter_plot.add('MO',lst1)
SVG(scatter_plot.render())


# In[77]:

#adding values from TN
scatter_plot=pygal.XY(stroke=False, x_title='#People', y_title="#poverty")
scatter_plot.title="Poor People are Everywhere (for real guys it's scary)"
scatter_plot.add('AL',lst)
scatter_plot.add('MO',lst1)
SVG(scatter_plot.render())


# In[80]:

for i in range(0,6,2):
    print (i)


# In[88]:

#changinhg x-axis
scatter_plot=pygal.XY(stroke=False, x_title='#People', y_title="#poverty")
scatter_plot.title="Poor People are Everywhere (for real guys it's scary)"
scatter_plot.x_labels=(i for i in range (0,7000,400))
scatter_plot.add('AL',lst)
scatter_plot.add('MO',lst1)
SVG(scatter_plot.render())


# In[99]:

#adjusting axis range
scatter_plot=pygal.XY(stroke=False, x_title='#People', y_title="#poverty", xrange=(0,100))
scatter_plot.title="Poor People are Everywhere (for real guys it's scary)"
scatter_plot.x_labels=(i for i in range (0,100,10))
scatter_plot.add('AL',lst)
scatter_plot.add('MO',lst1)
SVG(scatter_plot.render())
scatter_plot.render_to_file('C:/Users/Thomas/Desktop/software_carpentry_workshop/Day_2/poo_ppl.')


# In[100]:

al=health_dat.loc[health_dat['State']=='AL',['Poverty']]
poverty_mean_al=al['Poverty'].mean()
poverty_mean_al


# In[102]:

def mean_of_column(state_name, column_name):
    state_df=health_dat.loc[health_dat['State']== state_name, [column_name]]
    return state_df[column_name].mean()


# In[105]:

mean_of_column('TX', 'Suicide')


# In[111]:

health_dat['State'].unique()
#list(health_dat['State'].unique())


# In[112]:

#Bar me
bar_chart=pygal.Bar()
bar_chart.title='Mean poverty'
for state in list(health_dat['State'].unique()):
    bar_chart.add(state, mean_of_column(state, 'Poverty'))
SVG(bar_chart.render())


# In[113]:

bar_chart=pygal.Bar()
bar_chart.title='Mean poverty'
for state in list(health_dat['State'].unique()):
    bar_chart.add(state, mean_of_column(state, 'Suicide'))
SVG(bar_chart.render())


# In[115]:

bar_chart=pygal.HorizontalBar()
bar_chart.title='Mean poverty'
for state in list(health_dat['State'].unique()):
    bar_chart.add(state, mean_of_column(state, 'Poverty'))
SVG(bar_chart.render())


# In[116]:

bar_chart=pygal.HorizontalBar(legend_at_bottom=True,                             legend_at_bottom_columns=11)
bar_chart.title='Mean poverty'
for state in list(health_dat['State'].unique()):
    bar_chart.add(state, mean_of_column(state, 'Poverty'))
SVG(bar_chart.render())


# In[ ]:



