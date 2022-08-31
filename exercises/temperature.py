class Temperature:
    """
    A class used to represent the temperature

    Attributes
    ----------
    
    value : float
        temperature, in degrees specified
        
    unit : str
        units of temperature, in F or C
    
    Methods
    -------
    
    get_K()
        returns the temperature in Kelvin instead of the original degree unit
        
    """
    
    def __init__(self, value=74.0, unit='F'):
        """ 
        Parameters
        ----------
        value : float
            default temperature in degrees F
        
        unit : str
            default unit of Fahrenheit
        """
        self.value = value
        self.unit = unit
        self.temp_K = self.get_K()

    def __repr__(self):
        """
        Formatting for how the variable is represented
        """
        return "Temperature({value},°{unit})".format(value=self.value,unit=self.unit)

    def __str__(self):
        """
        How the variable is printed
        """
        return "The temperature is {value} °{unit}".format(value=self.value, unit=self.unit)

    def get_K(self):
        """
        Converts degrees F or C to K
        
        Parameters
        ----------
        T : float
            temperature, in degrees specified
        
        unit : str
            units of temperature, in F or C
            
        Returns:
        --------
        
        T, temperature, in K
        """
        
        unit = self.unit
        T = self.value

        # If T is in Fahrenheit, convert to C:
        if unit == 'F':
            T = (T - 32) * (5./9.)
            unit = 'C' # Re-assign unit to C
        
        # If T is in Celsius, convert to Kelvin
        if unit == 'C':
            T = T + 273.15

        return T