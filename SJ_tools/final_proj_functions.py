import numpy as np
import pingouin as pg


def relative_abundance(N, ni):
    '''
    Function to calculate relative species abundance

    Parameters
    ----------
    N: int
        Total biomass of all samples [CPUE]

    ni: int
        Biomass of target genus [CPUE]

    Returns
    -------
    rel_abundance: float
        Relative abundance of target genus [CPUE]
        -(np.sum(ni/N*np.log(ni/N)))
    '''
    rel_abundance = (ni/N)*100
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



def calc_correlations(beuti, jellies):
    '''
    Function to calculate the correlation matrices between BEUTI index data and jellyfish abundance data. Calculates the R^2 value, then extracts the values from the resulting matrix.

    Parameters
    ----------
    beuti: numpy array
        BEUTI index data; daily observations averaged by month
    jellies: numpy array
        Jellyfish abundance data; one value per year
    
    Returns
    -------
    r2: float
        Correlation coefficient squared
    '''
    r2_array = (np.sqrt(np.abs(np.corrcoef(beuti, jellies, rowvar=False))))
    r2_value = np.fliplr(r2_array).diagonal()
    r2 = r2_value[0]
    return(r2)


