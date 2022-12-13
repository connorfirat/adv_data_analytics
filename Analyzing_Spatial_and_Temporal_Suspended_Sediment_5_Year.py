import matplotlib.pyplot as plt
import pandas as pd


All_Stats = pd.read_csv(r"D:\School\Adv_Data_Analytics\Project\GEE_Output_Rasters\csv\All_Stats.csv")
print(All_Stats)

#Convert all dates to a datetime format                                                             
All_Stats['Date'] = pd.to_datetime(All_Stats['Date'], infer_datetime_format = True)
#Sort dates
All_Stats = All_Stats.sort_values(by = 'Date')

#Filter out the data for the 5 year period between 1982-12-07 and 1987-12-31
Stats_1983 = All_Stats.loc[(All_Stats['Date'] >= '1982-12-07')
                     & (All_Stats['Date'] <= '1987-12-31')]
#Create a subplot figure with four different axes
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize = (10,8))
#Assign a mean line plot for each reach in the NDTI index subplot
Stats_1983.plot(x = 'Date', y = 'Mean_NDTI_Reach_1', kind = 'line', ax = ax1)
Stats_1983.plot(x = 'Date', y = 'Mean_NDTI_Reach_2', kind = 'line', ax = ax1)
Stats_1983.plot(x = 'Date', y = 'Mean_NDTI_Reach_3', kind = 'line', ax = ax1)
Stats_1983.plot(x = 'Date', y = 'Mean_NDTI_Reach_4', kind = 'line', ax = ax1)
#Assign a mean line plot for each reach in the NSMI index subplot
Stats_1983.plot(x = 'Date', y = 'Mean_NSMI_Reach_1', kind = 'line', ax = ax2)
Stats_1983.plot(x = 'Date', y = 'Mean_NSMI_Reach_2', kind = 'line', ax = ax2)
Stats_1983.plot(x = 'Date', y = 'Mean_NSMI_Reach_3', kind = 'line', ax = ax2)
Stats_1983.plot(x = 'Date', y = 'Mean_NSMI_Reach_4', kind = 'line', ax = ax2)
#Assign a mean line plot for each reach in the NDSSI index subplot
Stats_1983.plot(x = 'Date', y = 'Mean_NDSSI_Reach_1', kind = 'line', ax = ax3)
Stats_1983.plot(x = 'Date', y = 'Mean_NDSSI_Reach_2', kind = 'line', ax = ax3)
Stats_1983.plot(x = 'Date', y = 'Mean_NDSSI_Reach_3', kind = 'line', ax = ax3)
Stats_1983.plot(x = 'Date', y = 'Mean_NDSSI_Reach_4', kind = 'line', ax = ax3)
#Assign a mean line plot for each reach in the QUANT subplot
Stats_1983.plot(x = 'Date', y = 'Mean_QUANT_Reach_1', kind = 'line', ax = ax4)
Stats_1983.plot(x = 'Date', y = 'Mean_QUANT_Reach_2', kind = 'line', ax = ax4)
Stats_1983.plot(x = 'Date', y = 'Mean_QUANT_Reach_3', kind = 'line', ax = ax4)
Stats_1983.plot(x = 'Date', y = 'Mean_QUANT_Reach_4', kind = 'line', ax = ax4)
#Add a legend to the side of the plots
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax4.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#Compress the data
plt.tight_layout()
#Plot and show the graph
plt.show()


#Filter out the data for the 5 year period between 1982-12-07 and 1992-12-31
Stats_1988 = All_Stats.loc[(All_Stats['Date'] >= '1988-01-01')
                     & (All_Stats['Date'] <= '1992-12-31')]
#Create a subplot figure with four different axes
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize = (10,8))
#Assign a mean line plot for each reach in the NDTI index subplot
Stats_1988.plot(x = 'Date', y = 'Mean_NDTI_Reach_1', kind = 'line', ax = ax1)
Stats_1988.plot(x = 'Date', y = 'Mean_NDTI_Reach_2', kind = 'line', ax = ax1)
Stats_1988.plot(x = 'Date', y = 'Mean_NDTI_Reach_3', kind = 'line', ax = ax1)
Stats_1988.plot(x = 'Date', y = 'Mean_NDTI_Reach_4', kind = 'line', ax = ax1)
#Assign a mean line plot for each reach in the NSMI index subplot
Stats_1988.plot(x = 'Date', y = 'Mean_NSMI_Reach_1', kind = 'line', ax = ax2)
Stats_1988.plot(x = 'Date', y = 'Mean_NSMI_Reach_2', kind = 'line', ax = ax2)
Stats_1988.plot(x = 'Date', y = 'Mean_NSMI_Reach_3', kind = 'line', ax = ax2)
Stats_1988.plot(x = 'Date', y = 'Mean_NSMI_Reach_4', kind = 'line', ax = ax2)
#Assign a mean line plot for each reach in the NDSSI index subplot
Stats_1988.plot(x = 'Date', y = 'Mean_NDSSI_Reach_1', kind = 'line', ax = ax3)
Stats_1988.plot(x = 'Date', y = 'Mean_NDSSI_Reach_2', kind = 'line', ax = ax3)
Stats_1988.plot(x = 'Date', y = 'Mean_NDSSI_Reach_3', kind = 'line', ax = ax3)
Stats_1988.plot(x = 'Date', y = 'Mean_NDSSI_Reach_4', kind = 'line', ax = ax3)
#Assign a mean line plot for each reach in the QUANT subplot
Stats_1988.plot(x = 'Date', y = 'Mean_QUANT_Reach_1', kind = 'line', ax = ax4)
Stats_1988.plot(x = 'Date', y = 'Mean_QUANT_Reach_2', kind = 'line', ax = ax4)
Stats_1988.plot(x = 'Date', y = 'Mean_QUANT_Reach_3', kind = 'line', ax = ax4)
Stats_1988.plot(x = 'Date', y = 'Mean_QUANT_Reach_4', kind = 'line', ax = ax4)
#Add a legend to the side of the plots
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax4.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#Compress the data
plt.tight_layout()
#Plot and show the graph
plt.show()


#Filter out the data for the 5 year period between 1993-01-01 and 1997-12-31
Stats_1993 = All_Stats.loc[(All_Stats['Date'] >= '1993-01-01')
                     & (All_Stats['Date'] <= '1997-12-31')]
#Create a subplot figure with four different axes
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize = (10,8))
#Assign a mean line plot for each reach in the NDTI index subplot
Stats_1993.plot(x = 'Date', y = 'Mean_NDTI_Reach_1', kind = 'line', ax = ax1)
Stats_1993.plot(x = 'Date', y = 'Mean_NDTI_Reach_2', kind = 'line', ax = ax1)
Stats_1993.plot(x = 'Date', y = 'Mean_NDTI_Reach_3', kind = 'line', ax = ax1)
Stats_1993.plot(x = 'Date', y = 'Mean_NDTI_Reach_4', kind = 'line', ax = ax1)
#Assign a mean line plot for each reach in the NSMI index subplot
Stats_1993.plot(x = 'Date', y = 'Mean_NSMI_Reach_1', kind = 'line', ax = ax2)
Stats_1993.plot(x = 'Date', y = 'Mean_NSMI_Reach_2', kind = 'line', ax = ax2)
Stats_1993.plot(x = 'Date', y = 'Mean_NSMI_Reach_3', kind = 'line', ax = ax2)
Stats_1993.plot(x = 'Date', y = 'Mean_NSMI_Reach_4', kind = 'line', ax = ax2)
#Assign a mean line plot for each reach in the NDSSI index subplot
Stats_1993.plot(x = 'Date', y = 'Mean_NDSSI_Reach_1', kind = 'line', ax = ax3)
Stats_1993.plot(x = 'Date', y = 'Mean_NDSSI_Reach_2', kind = 'line', ax = ax3)
Stats_1993.plot(x = 'Date', y = 'Mean_NDSSI_Reach_3', kind = 'line', ax = ax3)
Stats_1993.plot(x = 'Date', y = 'Mean_NDSSI_Reach_4', kind = 'line', ax = ax3)
#Assign a mean line plot for each reach in the QUANT subplot
Stats_1993.plot(x = 'Date', y = 'Mean_QUANT_Reach_1', kind = 'line', ax = ax4)
Stats_1993.plot(x = 'Date', y = 'Mean_QUANT_Reach_2', kind = 'line', ax = ax4)
Stats_1993.plot(x = 'Date', y = 'Mean_QUANT_Reach_3', kind = 'line', ax = ax4)
Stats_1993.plot(x = 'Date', y = 'Mean_QUANT_Reach_4', kind = 'line', ax = ax4)
#Add a legend to the side of the plots
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax4.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#Compress the data
plt.tight_layout()
#Plot and show the graph
plt.show()


#Filter out the data for the 5 year period between 1998-01-01 and 2002-12-31
Stats_1998 = All_Stats.loc[(All_Stats['Date'] >= '1998-01-01')
                     & (All_Stats['Date'] <= '2002-12-31')]
#Create a subplot figure with four different axes
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize = (10,8))
#Assign a mean line plot for each reach in the NDTI index subplot
Stats_1998.plot(x = 'Date', y = 'Mean_NDTI_Reach_1', kind = 'line', ax = ax1)
Stats_1998.plot(x = 'Date', y = 'Mean_NDTI_Reach_2', kind = 'line', ax = ax1)
Stats_1998.plot(x = 'Date', y = 'Mean_NDTI_Reach_3', kind = 'line', ax = ax1)
Stats_1998.plot(x = 'Date', y = 'Mean_NDTI_Reach_4', kind = 'line', ax = ax1)
#Assign a mean line plot for each reach in the NSMI index subplot
Stats_1998.plot(x = 'Date', y = 'Mean_NSMI_Reach_1', kind = 'line', ax = ax2)
Stats_1998.plot(x = 'Date', y = 'Mean_NSMI_Reach_2', kind = 'line', ax = ax2)
Stats_1998.plot(x = 'Date', y = 'Mean_NSMI_Reach_3', kind = 'line', ax = ax2)
Stats_1998.plot(x = 'Date', y = 'Mean_NSMI_Reach_4', kind = 'line', ax = ax2)
#Assign a mean line plot for each reach in the NDSSI index subplot
Stats_1998.plot(x = 'Date', y = 'Mean_NDSSI_Reach_1', kind = 'line', ax = ax3)
Stats_1998.plot(x = 'Date', y = 'Mean_NDSSI_Reach_2', kind = 'line', ax = ax3)
Stats_1998.plot(x = 'Date', y = 'Mean_NDSSI_Reach_3', kind = 'line', ax = ax3)
Stats_1998.plot(x = 'Date', y = 'Mean_NDSSI_Reach_4', kind = 'line', ax = ax3)
#Assign a mean line plot for each reach in the QUANT subplot
Stats_1998.plot(x = 'Date', y = 'Mean_QUANT_Reach_1', kind = 'line', ax = ax4)
Stats_1998.plot(x = 'Date', y = 'Mean_QUANT_Reach_2', kind = 'line', ax = ax4)
Stats_1998.plot(x = 'Date', y = 'Mean_QUANT_Reach_3', kind = 'line', ax = ax4)
Stats_1998.plot(x = 'Date', y = 'Mean_QUANT_Reach_4', kind = 'line', ax = ax4)
#Add a legend to the side of the plots
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax4.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#Compress the data
plt.tight_layout()
#Plot and show the graph
plt.show()


#Filter out the data for the 5 year period between 2003-01-01 and 2007-12-31
Stats_2003 = All_Stats.loc[(All_Stats['Date'] >= '2003-01-01')
                     & (All_Stats['Date'] <= '2007-12-31')]
#Create a subplot figure with four different axes
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize = (10,8))
#Assign a mean line plot for each reach in the NDTI index subplot
Stats_2003.plot(x = 'Date', y = 'Mean_NDTI_Reach_1', kind = 'line', ax = ax1)
Stats_2003.plot(x = 'Date', y = 'Mean_NDTI_Reach_2', kind = 'line', ax = ax1)
Stats_2003.plot(x = 'Date', y = 'Mean_NDTI_Reach_3', kind = 'line', ax = ax1)
Stats_2003.plot(x = 'Date', y = 'Mean_NDTI_Reach_4', kind = 'line', ax = ax1)
#Assign a mean line plot for each reach in the NSMI index subplot
Stats_2003.plot(x = 'Date', y = 'Mean_NSMI_Reach_1', kind = 'line', ax = ax2)
Stats_2003.plot(x = 'Date', y = 'Mean_NSMI_Reach_2', kind = 'line', ax = ax2)
Stats_2003.plot(x = 'Date', y = 'Mean_NSMI_Reach_3', kind = 'line', ax = ax2)
Stats_2003.plot(x = 'Date', y = 'Mean_NSMI_Reach_4', kind = 'line', ax = ax2)
#Assign a mean line plot for each reach in the NDSSI index subplot
Stats_2003.plot(x = 'Date', y = 'Mean_NDSSI_Reach_1', kind = 'line', ax = ax3)
Stats_2003.plot(x = 'Date', y = 'Mean_NDSSI_Reach_2', kind = 'line', ax = ax3)
Stats_2003.plot(x = 'Date', y = 'Mean_NDSSI_Reach_3', kind = 'line', ax = ax3)
Stats_2003.plot(x = 'Date', y = 'Mean_NDSSI_Reach_4', kind = 'line', ax = ax3)
#Assign a mean line plot for each reach in the QUANT subplot
Stats_2003.plot(x = 'Date', y = 'Mean_QUANT_Reach_1', kind = 'line', ax = ax4)
Stats_2003.plot(x = 'Date', y = 'Mean_QUANT_Reach_2', kind = 'line', ax = ax4)
Stats_2003.plot(x = 'Date', y = 'Mean_QUANT_Reach_3', kind = 'line', ax = ax4)
Stats_2003.plot(x = 'Date', y = 'Mean_QUANT_Reach_4', kind = 'line', ax = ax4)
#Add a legend to the side of the plots
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax4.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#Compress the data
plt.tight_layout()
#Plot and show the graph
plt.show()


#Filter out the data for the 5 year period between 2008-01-01 and 2012-12-31
Stats_2008 = All_Stats.loc[(All_Stats['Date'] >= '2008-01-01')
                     & (All_Stats['Date'] <= '2012-12-31')]
#Create a subplot figure with four different axes
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize = (10,8))
#Assign a mean line plot for each reach in the NDTI index subplot
Stats_2008.plot(x = 'Date', y = 'Mean_NDTI_Reach_1', kind = 'line', ax = ax1)
Stats_2008.plot(x = 'Date', y = 'Mean_NDTI_Reach_2', kind = 'line', ax = ax1)
Stats_2008.plot(x = 'Date', y = 'Mean_NDTI_Reach_3', kind = 'line', ax = ax1)
Stats_2008.plot(x = 'Date', y = 'Mean_NDTI_Reach_4', kind = 'line', ax = ax1)
#Assign a mean line plot for each reach in the NSMI index subplot
Stats_2008.plot(x = 'Date', y = 'Mean_NSMI_Reach_1', kind = 'line', ax = ax2)
Stats_2008.plot(x = 'Date', y = 'Mean_NSMI_Reach_2', kind = 'line', ax = ax2)
Stats_2008.plot(x = 'Date', y = 'Mean_NSMI_Reach_3', kind = 'line', ax = ax2)
Stats_2008.plot(x = 'Date', y = 'Mean_NSMI_Reach_4', kind = 'line', ax = ax2)
#Assign a mean line plot for each reach in the NDSSI index subplot
Stats_2008.plot(x = 'Date', y = 'Mean_NDSSI_Reach_1', kind = 'line', ax = ax3)
Stats_2008.plot(x = 'Date', y = 'Mean_NDSSI_Reach_2', kind = 'line', ax = ax3)
Stats_2008.plot(x = 'Date', y = 'Mean_NDSSI_Reach_3', kind = 'line', ax = ax3)
Stats_2008.plot(x = 'Date', y = 'Mean_NDSSI_Reach_4', kind = 'line', ax = ax3)
#Assign a mean line plot for each reach in the QUANT subplot
Stats_2008.plot(x = 'Date', y = 'Mean_QUANT_Reach_1', kind = 'line', ax = ax4)
Stats_2008.plot(x = 'Date', y = 'Mean_QUANT_Reach_2', kind = 'line', ax = ax4)
Stats_2008.plot(x = 'Date', y = 'Mean_QUANT_Reach_3', kind = 'line', ax = ax4)
Stats_2008.plot(x = 'Date', y = 'Mean_QUANT_Reach_4', kind = 'line', ax = ax4)
#Add a legend to the side of the plots
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax4.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#Compress the data
plt.tight_layout()
#Plot and show the graph
plt.show()


#Filter out the data for the 5 year period between 2013-01-01 and 2017-12-31
Stats_2013 = All_Stats.loc[(All_Stats['Date'] >= '2013-01-01')
                     & (All_Stats['Date'] <= '2017-12-31')]
#Create a subplot figure with four different axes
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize = (10,8))
#Assign a mean line plot for each reach in the NDTI index subplot
Stats_2013.plot(x = 'Date', y = 'Mean_NDTI_Reach_1', kind = 'line', ax = ax1)
Stats_2013.plot(x = 'Date', y = 'Mean_NDTI_Reach_2', kind = 'line', ax = ax1)
Stats_2013.plot(x = 'Date', y = 'Mean_NDTI_Reach_3', kind = 'line', ax = ax1)
Stats_2013.plot(x = 'Date', y = 'Mean_NDTI_Reach_4', kind = 'line', ax = ax1)
#Assign a mean line plot for each reach in the NSMI index subplot
Stats_2013.plot(x = 'Date', y = 'Mean_NSMI_Reach_1', kind = 'line', ax = ax2)
Stats_2013.plot(x = 'Date', y = 'Mean_NSMI_Reach_2', kind = 'line', ax = ax2)
Stats_2013.plot(x = 'Date', y = 'Mean_NSMI_Reach_3', kind = 'line', ax = ax2)
Stats_2013.plot(x = 'Date', y = 'Mean_NSMI_Reach_4', kind = 'line', ax = ax2)
#Assign a mean line plot for each reach in the NDSSI index subplot
Stats_2013.plot(x = 'Date', y = 'Mean_NDSSI_Reach_1', kind = 'line', ax = ax3)
Stats_2013.plot(x = 'Date', y = 'Mean_NDSSI_Reach_2', kind = 'line', ax = ax3)
Stats_2013.plot(x = 'Date', y = 'Mean_NDSSI_Reach_3', kind = 'line', ax = ax3)
Stats_2013.plot(x = 'Date', y = 'Mean_NDSSI_Reach_4', kind = 'line', ax = ax3)
#Assign a mean line plot for each reach in the QUANT subplot
Stats_2013.plot(x = 'Date', y = 'Mean_QUANT_Reach_1', kind = 'line', ax = ax4)
Stats_2013.plot(x = 'Date', y = 'Mean_QUANT_Reach_2', kind = 'line', ax = ax4)
Stats_2013.plot(x = 'Date', y = 'Mean_QUANT_Reach_3', kind = 'line', ax = ax4)
Stats_2013.plot(x = 'Date', y = 'Mean_QUANT_Reach_4', kind = 'line', ax = ax4)
#Add a legend to the side of the plots
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax4.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#Compress the data
plt.tight_layout()
#Plot and show the graph
plt.show()


#Filter out the data for the 5 year period between 2018-01-01 and 2022-12-31
Stats_2018 = All_Stats.loc[(All_Stats['Date'] >= '2018-01-01')
                     & (All_Stats['Date'] <= '2022-12-31')]
#Create a subplot figure with four different axes
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize = (10,8))
#Assign a mean line plot for each reach in the NDTI index subplot
Stats_2018.plot(x = 'Date', y = 'Mean_NDTI_Reach_1', kind = 'line', ax = ax1)
Stats_2018.plot(x = 'Date', y = 'Mean_NDTI_Reach_2', kind = 'line', ax = ax1)
Stats_2018.plot(x = 'Date', y = 'Mean_NDTI_Reach_3', kind = 'line', ax = ax1)
Stats_2018.plot(x = 'Date', y = 'Mean_NDTI_Reach_4', kind = 'line', ax = ax1)
#Assign a mean line plot for each reach in the NSMI index subplot
Stats_2018.plot(x = 'Date', y = 'Mean_NSMI_Reach_1', kind = 'line', ax = ax2)
Stats_2018.plot(x = 'Date', y = 'Mean_NSMI_Reach_2', kind = 'line', ax = ax2)
Stats_2018.plot(x = 'Date', y = 'Mean_NSMI_Reach_3', kind = 'line', ax = ax2)
Stats_2018.plot(x = 'Date', y = 'Mean_NSMI_Reach_4', kind = 'line', ax = ax2)
#Assign a mean line plot for each reach in the NDSSI index subplot
Stats_2018.plot(x = 'Date', y = 'Mean_NDSSI_Reach_1', kind = 'line', ax = ax3)
Stats_2018.plot(x = 'Date', y = 'Mean_NDSSI_Reach_2', kind = 'line', ax = ax3)
Stats_2018.plot(x = 'Date', y = 'Mean_NDSSI_Reach_3', kind = 'line', ax = ax3)
Stats_2018.plot(x = 'Date', y = 'Mean_NDSSI_Reach_4', kind = 'line', ax = ax3)
#Assign a mean line plot for each reach in the QUANT subplot
Stats_2018.plot(x = 'Date', y = 'Mean_QUANT_Reach_1', kind = 'line', ax = ax4)
Stats_2018.plot(x = 'Date', y = 'Mean_QUANT_Reach_2', kind = 'line', ax = ax4)
Stats_2018.plot(x = 'Date', y = 'Mean_QUANT_Reach_3', kind = 'line', ax = ax4)
Stats_2018.plot(x = 'Date', y = 'Mean_QUANT_Reach_4', kind = 'line', ax = ax4)
#Add a legend to the side of the plots
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax4.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#Compress the data
plt.tight_layout()
#Plot and show the graph
plt.show()