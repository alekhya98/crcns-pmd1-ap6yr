The following steps explain how the dataset was retrieved and loaded/accessed via the io.py file. 

The dataset pmd-1 was retrieved from the following link: https://crcns.org/data-sets/motor-cortex/pmd-1/about-pmd-1. On this page, there is a link that leads to multiple downloadable files related to the pmd-1. From here, there are 4 downloadable files listed; the data was retrieved from downloading "data_and_scripts.tar.gz". 

After unzipping "data_and_scripts.tar.gz" in the project directory, another folder was created titled "data_and_scripts". In this folder, the data is stored in multiple files under a folder called "source_data". There are raw and processed files, all separated into two folders under "source_data". For this specific project, we will be dealing with the processed data, specifically the .mat file named "MM_S1_processed.mat" This file is representative of neural recordings and kinematics data during a reach task of one macaque, which is the unit of analysis for this particular study. 

An io.py file was moved into the "processed" data folder that will then allow the loading of "MM_S1_processed.mat" into a python jupyter notebook for further processing.