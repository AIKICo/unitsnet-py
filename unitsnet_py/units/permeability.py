from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class PermeabilityUnits(Enum):
        """
            PermeabilityUnits enumeration
        """
        
        HenryPerMeter = 'HenryPerMeter'
        """
            
        """
        

class PermeabilityDto:
    """
    A DTO representation of a Permeability

    Attributes:
        value (float): The value of the Permeability.
        unit (PermeabilityUnits): The specific unit that the Permeability value is representing.
    """

    def __init__(self, value: float, unit: PermeabilityUnits):
        """
        Create a new DTO representation of a Permeability

        Parameters:
            value (float): The value of the Permeability.
            unit (PermeabilityUnits): The specific unit that the Permeability value is representing.
        """
        self.value: float = value
        """
        The value of the Permeability
        """
        self.unit: PermeabilityUnits = unit
        """
        The specific unit that the Permeability value is representing
        """

    def to_json(self):
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        return PermeabilityDto(value=data["value"], unit=PermeabilityUnits(data["unit"]))


class Permeability(AbstractMeasure):
    """
    In electromagnetism, permeability is the measure of the ability of a material to support the formation of a magnetic field within itself.

    Args:
        value (float): The value.
        from_unit (PermeabilityUnits): The Permeability unit to create from, The default unit is HenryPerMeter
    """
    def __init__(self, value: float, from_unit: PermeabilityUnits = PermeabilityUnits.HenryPerMeter):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__henries_per_meter = None
        

    def convert(self, unit: PermeabilityUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: PermeabilityUnits = PermeabilityUnits.HenryPerMeter) -> PermeabilityDto:
        """
        Get a new instance of Permeability DTO representing the current unit.

        :param hold_in_unit: The specific Permeability unit to store the Permeability value in the DTO representation.
        :type hold_in_unit: PermeabilityUnits
        :return: A new instance of PermeabilityDto.
        :rtype: PermeabilityDto
        """
        return PermeabilityDto(value=self.convert(hold_in_unit), unit=hold_in_unit)

    @staticmethod
    def from_dto(permeability_dto: PermeabilityDto):
        """
        Obtain a new instance of Permeability from a DTO unit object.

        :param permeability_dto: The Permeability DTO representation.
        :type permeability_dto: PermeabilityDto
        :return: A new instance of Permeability.
        :rtype: Permeability
        """
        return Permeability(permeability_dto.value, permeability_dto.unit)

    def __convert_from_base(self, from_unit: PermeabilityUnits) -> float:
        value = self._value
        
        if from_unit == PermeabilityUnits.HenryPerMeter:
            return (value)
        
        return None


    def __convert_to_base(self, value: float, to_unit: PermeabilityUnits) -> float:
        
        if to_unit == PermeabilityUnits.HenryPerMeter:
            return (value)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_henries_per_meter(henries_per_meter: float):
        """
        Create a new instance of Permeability from a value in henries_per_meter.

        

        :param meters: The Permeability value in henries_per_meter.
        :type henries_per_meter: float
        :return: A new instance of Permeability.
        :rtype: Permeability
        """
        return Permeability(henries_per_meter, PermeabilityUnits.HenryPerMeter)

    
    @property
    def henries_per_meter(self) -> float:
        """
        
        """
        if self.__henries_per_meter != None:
            return self.__henries_per_meter
        self.__henries_per_meter = self.__convert_from_base(PermeabilityUnits.HenryPerMeter)
        return self.__henries_per_meter

    
    def to_string(self, unit: PermeabilityUnits = PermeabilityUnits.HenryPerMeter) -> str:
        """
        Format the Permeability to string.
        Note! the default format for Permeability is HenryPerMeter.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == PermeabilityUnits.HenryPerMeter:
            return f"""{self.henries_per_meter} H/m"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: PermeabilityUnits = PermeabilityUnits.HenryPerMeter) -> str:
        """
        Get Permeability unit abbreviation.
        Note! the default abbreviation for Permeability is HenryPerMeter.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == PermeabilityUnits.HenryPerMeter:
            return """H/m"""
        