from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class RelativeHumidityUnits(Enum):
        """
            RelativeHumidityUnits enumeration
        """
        
        Percent = 'Percent'
        """
            
        """
        

class RelativeHumidityDto:
    def __init__(self, value: float, unit: RelativeHumidityUnits):
        self.value: float = value
        self.unit: RelativeHumidityUnits = unit

    def to_json(self):
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        return RelativeHumidityDto(value=data["value"], unit=RelativeHumidityUnits(data["unit"]))


class RelativeHumidity(AbstractMeasure):
    """
    Relative humidity is a ratio of the actual water vapor present in the air to the maximum water vapor in the air at the given temperature.

    Args:
        value (float): The value.
        from_unit (RelativeHumidityUnits): The RelativeHumidity unit to create from, The default unit is Percent
    """
    def __init__(self, value: float, from_unit: RelativeHumidityUnits = RelativeHumidityUnits.Percent):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__percent = None
        

    def convert(self, unit: RelativeHumidityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: RelativeHumidityUnits = RelativeHumidityUnits.Percent) -> RelativeHumidityDto:
        return RelativeHumidityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)

    @staticmethod
    def from_dto(relative_humidity_dto: RelativeHumidityDto):
        return RelativeHumidity(relative_humidity_dto.value, relative_humidity_dto.unit)

    def __convert_from_base(self, from_unit: RelativeHumidityUnits) -> float:
        value = self._value
        
        if from_unit == RelativeHumidityUnits.Percent:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: RelativeHumidityUnits) -> float:
        
        if to_unit == RelativeHumidityUnits.Percent:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_percent(percent: float):
        """
        Create a new instance of RelativeHumidity from a value in percent.

        

        :param meters: The RelativeHumidity value in percent.
        :type percent: float
        :return: A new instance of RelativeHumidity.
        :rtype: RelativeHumidity
        """
        return RelativeHumidity(percent, RelativeHumidityUnits.Percent)

    
    @property
    def percent(self) -> float:
        """
        
        """
        if self.__percent != None:
            return self.__percent
        self.__percent = self.__convert_from_base(RelativeHumidityUnits.Percent)
        return self.__percent

    
    def to_string(self, unit: RelativeHumidityUnits = RelativeHumidityUnits.Percent) -> str:
        """
        Format the RelativeHumidity to string.
        Note! the default format for RelativeHumidity is Percent.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == RelativeHumidityUnits.Percent:
            return f"""{self.percent} %RH"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: RelativeHumidityUnits = RelativeHumidityUnits.Percent) -> str:
        """
        Get RelativeHumidity unit abbreviation.
        Note! the default abbreviation for RelativeHumidity is Percent.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == RelativeHumidityUnits.Percent:
            return """%RH"""
        