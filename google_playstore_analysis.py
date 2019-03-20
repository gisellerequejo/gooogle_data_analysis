import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Goal is to Plot correlation between number of reviews and number of installs as wells as ratings vs number of installs_df

###################################################################################

#Created pandas dataframe
google_df = pd.read_csv('/Users/gisellerequejo/python/data_analytics/googleplaystore.csv')


#Let's see the data
reviews_df_clean= google_df.iloc[0:10000,3]
#Need to change Data Type to integer
reviews_df_clean1= (reviews_df_clean.astype(int))
#Let's make it decimals. 1.2 million etc
reviews_df_clean2=reviews_df_clean1.values/10**6


#Let's see the data
installs_df = google_df.iloc[0:10000,5]
#Unfortunately there are special characters. Need to remove them
installs_df_clean1=installs_df.replace('\+','',regex=True).astype(str)
#Seems there are still some special characters. Need to remove them here too.
installs_df_clean2=(installs_df_clean1.replace('\,','',regex=True).astype(int))/10**6
#Let's make it decimals of millions
installs_df_clean3=installs_df_clean2.values


#Time to plot
plt.scatter(reviews_df_clean2, installs_df_clean3)
#Let's get some labels
plt.xlabel('# of reviews in millions')
plt.ylabel('# of installs in millions')
#Let's give it a title
plt.title('Connection between Number of Installs and Number of Reviews')
#Time to show what we've done
plt.show()

#We've found that if there are a low amount of reviews, people are installing the app more often. How unexpected! :D
