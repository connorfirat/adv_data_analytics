import geopandas as gpd
import rasterio
import rasterstats
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

#Create a variable for theshp file
file = r'D:\School\Adv_Data_Analytics\Project\River_Boundary\shp_file\TN_River_Main_5000m_Divide_Edit\TN_River_Main_5000m_Divide_Edit.shp'
#Import shapefile for clipping images
reaches = gpd.read_file(file)
reaches.plot()

#Divide shapefile into individual 5000 meter reaches
reach_1_df = pd.DataFrame(reaches.loc[0]).transpose()
#Save shapefile as a geometry geopandas dataframe
reaches_1_polygon = gpd.GeoDataFrame(reach_1_df, geometry = 'geometry')
#Set geometry as the same coordinate system as the reach
reaches_1_polygon.crs = reaches.crs
#Plot the geopandas dataframe
reaches_1_polygon.plot()

#Divide shapefile into individual 5000 meter reaches
reach_2_df = pd.DataFrame(reaches.loc[2]).transpose()
#Save shapefile as a geometry geopandas dataframe
reaches_2_polygon = gpd.GeoDataFrame(reach_2_df, geometry = 'geometry')
#Set geometry as the same coordinate system as the reach
reaches_2_polygon.crs = reaches.crs
#Plot the geopandas dataframe
reaches_2_polygon.plot()

#Divide shapefile into individual 5000 meter reaches
reach_3_df = pd.DataFrame(reaches.loc[1]).transpose()
#Save shapefile as a geometry geopandas dataframe
reaches_3_polygon = gpd.GeoDataFrame(reach_3_df, geometry = 'geometry')
#Set geometry as the same coordinate system as the reach
reaches_3_polygon.crs = reaches.crs
#Plot the geopandas dataframe
reaches_3_polygon.plot()

#Divide shapefile into individual 5000 meter reaches
reach_4_df = pd.DataFrame(reaches.loc[3]).transpose()
#Save shapefile as a geometry geopandas dataframe
reaches_4_polygon = gpd.GeoDataFrame(reach_4_df, geometry = 'geometry')
#Set geometry as the same coordinate system as the reach
reaches_4_polygon.crs = reaches.crs
#Plot the geopandas dataframe
reaches_4_polygon.plot()

#Create a new pandas dataframe for NDTI making a blank column that hold each mean value for each reach 
NDTI_data = pd.DataFrame('', columns = ['Date', 'Satellite', 
                                        'Mean_NDTI_Reach_1', 'Mean_NDTI_Reach_2', 'Mean_NDTI_Reach_3', 'Mean_NDTI_Reach_4'], 
                                        index = np.arange(1, 1015))

#Create a new pandas dataframe for NSMI making a blank column that hold each mean value for each reach 
NSMI_data = pd.DataFrame('', columns = ['Date', 'Satellite', 
                                        'Mean_NSMI_Reach_1', 'Mean_NSMI_Reach_2', 'Mean_NSMI_Reach_3', 'Mean_NSMI_Reach_4'],
                                        index = np.arange(1, 1015))

#Create a new pandas dataframe for NDSSI making a blank column that hold each mean value for each reach 
NDSSI_data = pd.DataFrame('', columns = ['Date', 'Satellite', 
                                        'Mean_NDSSI_Reach_1', 'Mean_NDSSI_Reach_2', 'Mean_NDSSI_Reach_3', 'Mean_NDSSI_Reach_4'],
                                        index = np.arange(1, 1014))

#Create a new pandas dataframe for QUANT making a blank column that hold each mean value for each reach 
QUANT_data = pd.DataFrame('', columns = ['Date', 'Satellite', 
                                        'Mean_QUANT_Reach_1', 'Mean_QUANT_Reach_2', 'Mean_QUANT_Reach_3', 'Mean_QUANT_Reach_4'],
                                        index = np.arange(1, 1014))

#os.chdir(r'D:\School\Adv_Data_Analytics\Project\GEE_Output_Rasters\NDTI')
#print(os.getcwd())

#Create a counter for each for loop iterator
i = 1
j = 1
l = 1
n = 1

#Create a for loop for the NDTI suspended sediment index locating the folder that copntains all the geotif files
for NDTI_Rast in os.listdir(r'D:\School\Adv_Data_Analytics\Project\GEE_Output_Rasters\NDTI' ):
    #Isolate files with the extension .tif
    if NDTI_Rast[-4: ] == '.tif':
        
        #Open the NDTI geotif in rasterio
        NDTI = rasterio.open(r'D:\School\Adv_Data_Analytics\Project\GEE_Output_Rasters\NDTI' + '\\' + NDTI_Rast)
        #Convert the NDTI geotif in a numpy array
        NDTI_array = NDTI.read(1)
        #Assign all 0 values a no data
        NDTI_array[NDTI_array == 0] = 'nan'
        #Account for geometric distortions in the array
        NDTI_affine = NDTI.transform
        
        # Reaches 1
        #Calculate zonal statistics for the mean value in reach 1
        NDTI_Reach_1 = rasterstats.zonal_stats(reaches_1_polygon, NDTI_array, affine = NDTI_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        NDTI_Reach_1_mean = NDTI_Reach_1[0]['mean']
        
        # Reaches 2
        #Calculate zonal statistics for the mean value in reach 2
        NDTI_Reach_2 = rasterstats.zonal_stats(reaches_2_polygon, NDTI_array, affine = NDTI_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        NDTI_Reach_2_mean = NDTI_Reach_2[0]['mean']
        
        # Reaches 3
        #Calculate zonal statistics for the mean value in reach 3
        NDTI_Reach_3 = rasterstats.zonal_stats(reaches_3_polygon, NDTI_array, affine = NDTI_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        NDTI_Reach_3_mean = NDTI_Reach_3[0]['mean']
        
        # Reaches 4
        #Calculate zonal statistics for the mean value in reach 4
        NDTI_Reach_4 = rasterstats.zonal_stats(reaches_4_polygon, NDTI_array, affine = NDTI_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        NDTI_Reach_4_mean = NDTI_Reach_4[0]['mean']         
        
        #All Data
        #Save each mean value to the column in the blank pandas dataframe
        NDTI_data.loc[i]['Mean_NDTI_Reach_1'] = NDTI_Reach_1_mean
        NDTI_data.loc[i]['Mean_NDTI_Reach_2'] = NDTI_Reach_2_mean
        NDTI_data.loc[i]['Mean_NDTI_Reach_3'] = NDTI_Reach_3_mean
        NDTI_data.loc[i]['Mean_NDTI_Reach_4'] = NDTI_Reach_4_mean          
 
        #Locate the date in the file name and save the string into the column in the blank pandas dataframe
        NDTI_data.loc[i]['Date'] = NDTI_Rast[-24:-14]
        #Locate the sensor name in the file name and save the string into the column in the blank pandas dataframe
        NDTI_data.loc[i]['Satellite'] = NDTI_Rast[-13:-4]        
 
        #Increment the counter by one when the first loop is finished
        i = i + 1
        
        #Print the name of the raster
        print(NDTI_Rast)
  
#Create a for loop for the NSMI suspended sediment index locating the folder that copntains all the geotif files        
for NSMI_Rast in os.listdir(r'D:\School\Adv_Data_Analytics\Project\GEE_Output_Rasters\NSMI' ):
    #Isolate files with the extension .tif
    if NSMI_Rast[-4: ] == '.tif':    
    
        #Open the NSMI geotif in rasterio
        NSMI = rasterio.open(r'D:\School\Adv_Data_Analytics\Project\GEE_Output_Rasters\NSMI' + '\\' + NSMI_Rast)
        #Convert the NSMI geotif in a numpy array
        NSMI_array = NSMI.read(1)
        #Assign all 0 values a no data
        NSMI_array[NSMI_array == 0] = 'nan'
        #Account for geometric distortions in the array
        NSMI_affine = NSMI.transform
        
        #Reaches 1
        #Calculate zonal statistics for the mean value in reach 1
        NSMI_Reach_1 = rasterstats.zonal_stats(reaches_1_polygon, NSMI_array, affine = NSMI_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        NSMI_Reach_1_mean = NSMI_Reach_1[0]['mean']
        
        # Reaches 2
        #Calculate zonal statistics for the mean value in reach 2
        NSMI_Reach_2 = rasterstats.zonal_stats(reaches_2_polygon, NSMI_array, affine = NSMI_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        NSMI_Reach_2_mean = NSMI_Reach_2[0]['mean']
        
        # Reaches 3
        #Calculate zonal statistics for the mean value in reach 3
        NSMI_Reach_3 = rasterstats.zonal_stats(reaches_3_polygon, NSMI_array, affine = NSMI_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        NSMI_Reach_3_mean = NSMI_Reach_3[0]['mean']
        
        # Reaches 4
        #Calculate zonal statistics for the mean value in reach 4
        NSMI_Reach_4 = rasterstats.zonal_stats(reaches_4_polygon, NSMI_array, affine = NSMI_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        NSMI_Reach_4_mean = NSMI_Reach_4[0]['mean']         
        
        #Save each mean value to the column in the blank pandas dataframe
        NSMI_data.loc[j]['Mean_NSMI_Reach_1'] = NSMI_Reach_1_mean
        NSMI_data.loc[j]['Mean_NSMI_Reach_2'] = NSMI_Reach_2_mean
        NSMI_data.loc[j]['Mean_NSMI_Reach_3'] = NSMI_Reach_3_mean
        NSMI_data.loc[j]['Mean_NSMI_Reach_4'] = NSMI_Reach_4_mean             
    
        #Locate the date in the file name and save the string into the column in the blank pandas dataframe
        NSMI_data.loc[j]['Date'] = NSMI_Rast[-24:-14]
        #Locate the sensor name in the file name and save the string into the column in the blank pandas dataframe
        NSMI_data.loc[j]['Satellite'] = NSMI_Rast[-13:-4]
        
        #Increment the counter by one when the first loop is finished
        j = j + 1
        
        #Print the name of the raster
        print(NSMI_Rast)

#Create a for loop for the NDSSI suspended sediment index locating the folder that copntains all the geotif files          
for NDSSI_Rast in os.listdir(r'D:\School\Adv_Data_Analytics\Project\GEE_Output_Rasters\NDSSI' ):
    #Isolate files with the extension .tif
    if NDSSI_Rast[-4: ] == '.tif':    
    
        #Open the NDSSI geotif in rasterio
        NDSSI = rasterio.open(r'D:\School\Adv_Data_Analytics\Project\GEE_Output_Rasters\NDSSI' + '\\' + NDSSI_Rast)
        #Convert the NDSSI geotif in a numpy array
        NDSSI_array = NDSSI.read(1)
        #Assign all 0 values a no data
        NDSSI_array[NDSSI_array == 0] = 'nan'
        #Account for geometric distortions in the array
        NDSSI_affine = NDSSI.transform
        
        #Reaches 1
        #Calculate zonal statistics for the mean value in reach 1
        NDSSI_Reach_1 = rasterstats.zonal_stats(reaches_1_polygon, NDSSI_array, affine = NDSSI_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        NDSSI_Reach_1_mean = NDSSI_Reach_1[0]['mean']
   
        #Reaches 2
        #Calculate zonal statistics for the mean value in reach 2
        NDSSI_Reach_2 = rasterstats.zonal_stats(reaches_2_polygon, NDSSI_array, affine = NDSSI_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        NDSSI_Reach_2_mean = NDSSI_Reach_2[0]['mean']

        #Reaches 3
        #Calculate zonal statistics for the mean value in reach 3
        NDSSI_Reach_3 = rasterstats.zonal_stats(reaches_3_polygon, NDSSI_array, affine = NDSSI_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        NDSSI_Reach_3_mean = NDSSI_Reach_3[0]['mean'] 
        
        #Reaches 4
        #Calculate zonal statistics for the mean value in reach 4
        NDSSI_Reach_4 = rasterstats.zonal_stats(reaches_4_polygon, NDSSI_array, affine = NDSSI_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        NDSSI_Reach_4_mean = NDSSI_Reach_4[0]['mean']          
        
        #Save each mean value to the column in the blank pandas dataframe
        NDSSI_data.loc[l]['Mean_NDSSI_Reach_1'] = NDSSI_Reach_1_mean
        NDSSI_data.loc[l]['Mean_NDSSI_Reach_2'] = NDSSI_Reach_2_mean
        NDSSI_data.loc[l]['Mean_NDSSI_Reach_3'] = NDSSI_Reach_3_mean
        NDSSI_data.loc[l]['Mean_NDSSI_Reach_4'] = NDSSI_Reach_4_mean   
            
        #Locate the date in the file name and save the string into the column in the blank pandas dataframe
        NDSSI_data.loc[l]['Date'] = NDSSI_Rast[-24:-14]
        #Locate the sensor name in the file name and save the string into the column in the blank pandas dataframe
        NDSSI_data.loc[l]['Satellite'] = NDSSI_Rast[-13:-4]

        #Increment the counter by one when the first loop is finished
        l = l + 1
        
        #Print the name of the raster
        print(NDSSI_Rast)
 
#Create a for loop for the QUANT suspended sediment index locating the folder that copntains all the geotif files           
for QUANT_Rast in os.listdir(r'D:\School\Adv_Data_Analytics\Project\GEE_Output_Rasters\QUANT' ):
    #Isolate files with the extension .tif
    if QUANT_Rast[-4: ] == '.tif':    
    
        #Open the QUANT geotif in rasterio
        QUANT = rasterio.open(r'D:\School\Adv_Data_Analytics\Project\GEE_Output_Rasters\QUANT' + '\\' + QUANT_Rast)
        #Convert the QUANT geotif in a numpy array
        QUANT_array = QUANT.read(1)
        #Assign all 0 values a no data
        QUANT_array[QUANT_array == 0] = 'nan'
        #Account for geometric distortions in the array
        QUANT_affine = QUANT.transform
        
        # Reaches 1
        #Calculate zonal statistics for the mean value in reach 1
        QUANT_Reach_1 = rasterstats.zonal_stats(reaches_1_polygon, QUANT_array, affine = QUANT_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        QUANT_Reach_1_mean = QUANT_Reach_1[0]['mean']  
        
        # Reaches 2
        #Calculate zonal statistics for the mean value in reach 2
        QUANT_Reach_2 = rasterstats.zonal_stats(reaches_2_polygon, QUANT_array, affine = QUANT_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        QUANT_Reach_2_mean = QUANT_Reach_2[0]['mean']   
        
        #Reaches 3
        #Calculate zonal statistics for the mean value in reach 3
        QUANT_Reach_3 = rasterstats.zonal_stats(reaches_3_polygon, QUANT_array, affine = QUANT_affine, stats = ['mean'], geojason_out = True) 
        #Save the mean value into the computers memory
        QUANT_Reach_3_mean = QUANT_Reach_3[0]['mean']   
        
        #Reaches 4
        #Calculate zonal statistics for the mean value in reach 4
        QUANT_Reach_4 = rasterstats.zonal_stats(reaches_4_polygon, QUANT_array, affine = QUANT_affine, stats = ['mean'], geojason_out = True)
        #Save the mean value into the computers memory
        QUANT_Reach_4_mean = QUANT_Reach_4[0]['mean']          
        
        #Save each mean value to the column in the blank pandas dataframe
        QUANT_data.loc[n]['Mean_QUANT_Reach_1'] = QUANT_Reach_1_mean
        QUANT_data.loc[n]['Mean_QUANT_Reach_2'] = QUANT_Reach_2_mean
        QUANT_data.loc[n]['Mean_QUANT_Reach_3'] = QUANT_Reach_3_mean
        QUANT_data.loc[n]['Mean_QUANT_Reach_4'] = QUANT_Reach_4_mean                
    
        #Locate the date in the file name and save the string into the column in the blank pandas dataframe
        QUANT_data.loc[n]['Date'] = QUANT_Rast[-24:-14]
        #Locate the sensor name in the file name and save the string into the column in the blank pandas dataframe
        QUANT_data.loc[n]['Satellite'] = QUANT_Rast[-13:-4]
        
        #Increment the counter by one when the first loop is finished        
        n = n + 1
        
        #Print the name of the raster
        print(QUANT_Rast)
        
#Merge all rasters into one dataframe, by the simular 'Date' and 'Satellite' column
ALL_df = NDTI_data.merge(NSMI_data, left_on=['Date', 'Satellite'], right_on = ['Date', 'Satellite'], 
                         how='left').merge(NDSSI_data, left_on=['Date', 'Satellite'], right_on = ['Date', 'Satellite'], 
                                           how='left').merge(QUANT_data, left_on=['Date', 'Satellite'], right_on = ['Date', 'Satellite'], 
                                                             how='left')

#Convert all dates to a datetime format                                                             
ALL_df['Date'] = pd.to_datetime(ALL_df['Date'], infer_datetime_format = True)
#Convert dataes to a smaller day format
ALL_df['Date'] = ALL_df['Date'].dt.date
#Sort dates
ALL_df = ALL_df.sort_values(by = 'Date')

#Create a subplot figure with four different axes
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize = (10,8))
#Assign a mean line plot for each reach in the NDTI index subplot
ALL_df.plot(x = 'Date', y = 'Mean_NDTI_Reach_1', kind = 'line', ax = ax1)
ALL_df.plot(x = 'Date', y = 'Mean_NDTI_Reach_2', kind = 'line', ax = ax1)
ALL_df.plot(x = 'Date', y = 'Mean_NDTI_Reach_3', kind = 'line', ax = ax1)
ALL_df.plot(x = 'Date', y = 'Mean_NDTI_Reach_4', kind = 'line', ax = ax1)
#Assign a mean line plot for each reach in the NSMI index subplot
ALL_df.plot(x = 'Date', y = 'Mean_NSMI_Reach_1', kind = 'line', ax = ax2)
ALL_df.plot(x = 'Date', y = 'Mean_NSMI_Reach_2', kind = 'line', ax = ax2)
ALL_df.plot(x = 'Date', y = 'Mean_NSMI_Reach_3', kind = 'line', ax = ax2)
ALL_df.plot(x = 'Date', y = 'Mean_NSMI_Reach_4', kind = 'line', ax = ax2)
#Assign a mean line plot for each reach in the NDSSI index subplot
ALL_df.plot(x = 'Date', y = 'Mean_NDSSI_Reach_1', kind = 'line', ax = ax3)
ALL_df.plot(x = 'Date', y = 'Mean_NDSSI_Reach_2', kind = 'line', ax = ax3)
ALL_df.plot(x = 'Date', y = 'Mean_NDSSI_Reach_3', kind = 'line', ax = ax3)
ALL_df.plot(x = 'Date', y = 'Mean_NDSSI_Reach_4', kind = 'line', ax = ax3)
#Assign a mean line plot for each reach in the QUANT subplot
ALL_df.plot(x = 'Date', y = 'Mean_QUANT_Reach_1', kind = 'line', ax = ax4)
ALL_df.plot(x = 'Date', y = 'Mean_QUANT_Reach_2', kind = 'line', ax = ax4)
ALL_df.plot(x = 'Date', y = 'Mean_QUANT_Reach_3', kind = 'line', ax = ax4)
ALL_df.plot(x = 'Date', y = 'Mean_QUANT_Reach_4', kind = 'line', ax = ax4)
#Add a legend to the side of the plots
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax4.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#Compress the data
plt.tight_layout()
#Plot and show the graph
plt.show()

#Export the data to be used in the next part where it will be broken into 5 year increments
ALL_df.to_csv(r'D:\School\Adv_Data_Analytics\Project\GEE_Output_Rasters\csv\All_Stats.csv')