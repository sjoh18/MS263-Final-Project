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



def jelly_anova(jellydf):
    '''
    Function to: 1. run an ANOVA on jellyfish abundance data, and 2. if there is a significant difference between any groups, run a post-hoc test to determine which group(s) is/are significantly different

    Parameters
    ----------
    jellydf: pandas dataframe
        Dataframe containing jellyfish abundance data

    Returns
    -------
    anova: pandas dataframe
        Results of the Welch's ANOVA
    post_hoc: pandas dataframe
        Results of the post-hoc, if a significant difference was found by ANOVA (alpha = 0.05)
    '''
    anova = pg.welch_anova(data=jellydf, dv='abundance', between='genus')

    if anova['p-unc'][0] <= 0.05:
        post_hoc = pg.pairwise_tukey(data=jellydf, dv='abundance', between='genus')

    return anova, post_hoc


