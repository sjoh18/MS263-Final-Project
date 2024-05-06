import numpy as np
from scipy import stats
import pandas as pd
import pingouin as pg
import netCDF4 as nc4
import os


def relative_abundance(sp_richness, N, ni):
    '''
    Function to calculate relative species abundance

    Parameters
    ----------
    sp_richness: float
        Species richness - total number of species observed

    N: int
        Total biomass of all samples [CPUE]

    ni: int
        Biomass of target species individuals observed [CPUE]

    Returns
    -------
    rel_abundance: float
        Relative abundance of species of interest [CPUE]
    '''
    rel_abundance = -(np.sum(ni/N*np.log(ni/N)))
    return(rel_abundance)

def jelly_anova(chrysaora, aurelia, aequorea):
    '''
    Function to: 1. run an ANOVA on jellyfish abundance data, and 2. if there is a significant difference between any groups, run a post-hoc test to determine which group(s) is/are significantly different

    Parameters
    ----------
    chrysaora: pandas dataframe
        Subsetted data including only Chrysaora genus biomass

    aurelia: pandas dataframe
        Subsetted data including only Aurelia genus biomass

    aequorea: pandas dataframe
        Subsetted data including only Aequora genus biomass


    Returns
    -------
    anova: pandas dataframe
        Results of the Welch's ANOVA
    post_hoc: pandas dataframe
        Results of the post-hoc, if a significant difference was found by ANOVA (alpha = 0.05)
    '''
    filepath = '/Users/sarah/Documents/MLML/Current_classes/MS263-Data_Analysis/Final_project/jelly_abundance_combined.csv'
    jelly_ab = pd.read_csv(filepath,header=1)

    chrysaora = jelly_ab[(jelly_ab['species_group'] == 'Chrysaora')]
    aurelia = jelly_ab[(jelly_ab['species_group'] == 'Aurelia')]
    aequorea = jelly_ab[(jelly_ab['species_group'] == 'Aequorea')]
    abundance = jelly_ab['abundance']
    
    anova = pg.welch_anova(data=jelly_ab, dv='abundance', between='species_group')

    if anova['p-unc'][0] <= 0.05:
        post_hoc = pg.pairwise_gameshowell(data=jelly_ab, dv='abundance', between='species_group')

    return anova, post_hoc
    


def read_chl_from_file(file_path):
    '''
    Function to extract chlorophyll-a Ocean Color data from NASA's AQUA-MODIS satellite in a specified area, Monterey Bay in this case. Ocean Color data must be downloaded already.

    Parameters
    ----------
    file_path: string
        path to folder and list of file names containing Ocean Color data
        
    Returns
    -------
    montbay_chl: float
        value of chlorophyll-a concentration as measured by AQUA-MODIS satellite at specified lat-lon coordinate
    '''

    ds = nc4.Dataset(file_path)
    
    # tell python what the latitude and longitude variables are called in the netCDF files
    modis_lat = np.array(ds.variables['lat'])
    modis_lon = np.array(ds.variables['lon'])
    modis_chl = np.array(ds.variables['chlor_a'])

    # specify a central point, then the radius
    # use the radius to calculate the square area of values to be included
    center_lat = 36.8
    center_lon = -121.9
    radius = 0.5
    min_lat = center_lat + radius
    max_lat = center_lat - radius
    min_lon = center_lon - radius
    max_lon = center_lon + radius

    min_lat_index = np.abs(modis_lat - min_lat).argmin()
    max_lat_index = np.abs(modis_lat - max_lat).argmin()
    min_lon_index = np.abs(modis_lon - min_lon).argmin()
    max_lon_index = np.abs(modis_lon - max_lon).argmin()

    ds.close()

    # extract chlorophyll values from the specified square
    montbay_chl = modis_chl[min_lat_index:max_lat_index+1, min_lon_index:max_lon_index+1]
    
    return(montbay_chl)




def remove_nans_chl(chl_values):
    chl_values = np.array(chl_values)
    values_nonans = np.where(chl_values == -3.2767e+04, 0, chl_values)

    return values_nonans



def read_sst_from_file(file_path):

    ds = nc4.Dataset(file_path)

    mur_lat = np.array(ds.variables['lat'])
    mur_lon = np.array(ds.variables['lon'])
    mur_sst = np.array(ds.variables['analysed_sst'])
    
    center_lat = 36.8
    center_lon = -121.9
    radius = 0.5
    min_lat = center_lat - radius
    max_lat = center_lat + radius
    min_lon = center_lon - radius
    max_lon = center_lon + radius

    min_lat_index = np.abs(mur_lat - min_lat).argmin()
    max_lat_index = np.abs(mur_lat - max_lat).argmin()
    min_lon_index = np.abs(mur_lon - min_lon).argmin()
    max_lon_index = np.abs(mur_lon - max_lon).argmin()
    
    ds.close()
    
    mur_sst = mur_sst[0,:,:]
    # gives a 2D array, why does it need to be 2D?
    
    montbay_sst = mur_sst[min_lat_index:max_lat_index+1, min_lon_index:max_lon_index+1]
    
    return(montbay_sst)



def remove_nans_sst(sst_values):
    sst_values = np.array(sst_values)
    values_nonans = np.where(sst_values == -32768, 0, sst_values)

    return values_nonans


