def celsius_to_fahr(temp_c):
    '''
    Function to convert temperature in celsius to fahrenheit

    Parameters
    ----------
    temp_c : float
        The temperature in celsius to convert to fahrenheit

    Returns
    -------
    F : float
        The temperature in fahrenheit
    '''
    F = (9/5)*temp_c+ 32
    return(F)

def fahr_to_celsius(temp_f):
    '''
    Function to convert temperature in fahrenheit to celsius

    Parameters
    ----------
    temp_f : float
        The temperature in fahrenheit to convert to celsius

    Returns
    -------
    C : float
        The temperature in celsius
    '''
    C = (temp_f - 32)*(5/9)
    return(C)

def celsius_to_kelvin(temp_c):
    '''
    Function to convert temperature in celsius to Kelvin

    Parameters
    ----------
    temp_c : float
        The temperature in celsius to convert to Kelvin

    Returns
    -------
    K : float
        The temperature in Kelvin
    '''
    K = temp_c + 273.15
    return(K)

def fahr_to_kelvin(temp_f):
    '''
    Function to convert temperature in fahrenheit to Kelvin

    Parameters
    ----------
    temp_f : float
        temperature in fahrenheit that is converted first to celsius then Kelvin

    Returns
    -------
    K : float
        temperature in kelvin

    '''
    C = (temp_f - 32)*(5/9)
    K = C + 273.15
    return(K)

def lbs_to_kg(lbs):
    '''
    Function to convert weight in lbs to kg

    Parameters
    ----------
    lbs : float
        weight in lbs to be converted to kg

    Returns
    -------
    kg : float
        weight in kg
    '''
    kg = lbs/2.2046
    return(kg)

def mmHg_to_Pa(pressure_mmHg):
    '''
    Function to convert pressure in mmHg to Pa

    Parameters
    ----------
    pressure_mmHg : float
        pressure in mmHg to be converted to Pa

    Returns
    -------
    Pa : float
        pressure in Pa
    '''
    Pa = pressure_mmHg*133.3
    return(Pa)

