# Effects of temperature and food availability on abundance of three genera of marine gelatinous medusae

## Steps for running analysis
1. Download the three CSV files in the "data" folder
2. Import SJ_tools; this is the package containing functions necessary for data wrangling and analysis
3. Run "Data_processing.ipynb" first 

   a. Note: running this notebook is not necessary for analysis; I made and used this notebook to wrangle the SST and Chl-a data. Part of the end result is two CSV files that are used for analysis in "Final_project.ipynb", one for SST and one for Chl-a, both of which are provided in the "data" folder. The data necessary for running this notebook is the SST and chl-a NetCDF files that can be downloaded from PODAAC (more info below).
5. Run "Final_project.ipynb"

## Data location and sources
- Jellyfish abundance data was downloaded from NOAA's Environmental Research Division's Data Access Program (ERDDAP). These data were collected as part of the Rockfish Recruitment and Ecosystem Assessment Surveys (RREAS) conducted by NOAA.
- SST data is from the Multi-scale Ultra-high Resolution (MUR) level 4 SST data products and was downloaded from NASA's Physical Oceanography Distributed Active Archive Center (PODAAC).
- Chlorophyll-a data was also downloaded from PODAAC and was collected by NASA's AQUA-MODIS Ocean Color satellite.

## Dependencies
Python packages needed to run analysis:
1. Numpy
2. MatPlotLib
3. Pandas
4. Pingouin
5. CmOcean
6. OS
7. DateTime
8. Cartopy
9. Scipy
10. Glidertools

## Location of data
All data is provided in the "data" folder in the main branch of the repository
