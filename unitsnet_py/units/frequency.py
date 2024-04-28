from enum import Enum
import math

from ..abstract_unit import AbstractMeasure



class FrequencyUnits(Enum):
        """
            FrequencyUnits enumeration
        """
        
        Hertz = 'Hertz'
        """
            
        """
        
        RadianPerSecond = 'RadianPerSecond'
        """
            
        """
        
        CyclePerMinute = 'CyclePerMinute'
        """
            
        """
        
        CyclePerHour = 'CyclePerHour'
        """
            
        """
        
        BeatPerMinute = 'BeatPerMinute'
        """
            
        """
        
        PerSecond = 'PerSecond'
        """
            
        """
        
        BUnit = 'BUnit'
        """
            
        """
        
        Microhertz = 'Microhertz'
        """
            
        """
        
        Millihertz = 'Millihertz'
        """
            
        """
        
        Kilohertz = 'Kilohertz'
        """
            
        """
        
        Megahertz = 'Megahertz'
        """
            
        """
        
        Gigahertz = 'Gigahertz'
        """
            
        """
        
        Terahertz = 'Terahertz'
        """
            
        """
        

class FrequencyDto:
    """
    A DTO representation of a Frequency

    Attributes:
        value (float): The value of the Frequency.
        unit (FrequencyUnits): The specific unit that the Frequency value is representing.
    """

    def __init__(self, value: float, unit: FrequencyUnits):
        """
        Create a new DTO representation of a Frequency

        Parameters:
            value (float): The value of the Frequency.
            unit (FrequencyUnits): The specific unit that the Frequency value is representing.
        """
        self.value: float = value
        """
        The value of the Frequency
        """
        self.unit: FrequencyUnits = unit
        """
        The specific unit that the Frequency value is representing
        """

    def to_json(self):
        """
        Get a Frequency DTO JSON object representing the current unit.

        :return: JSON object represents Frequency DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Hertz"}
        """
        return {"value": self.value, "unit": self.unit.value}

    @staticmethod
    def from_json(data):
        """
        Obtain a new instance of Frequency DTO from a json representation.

        :param data: The Frequency DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Hertz"}
        :return: A new instance of FrequencyDto.
        :rtype: FrequencyDto
        """
        return FrequencyDto(value=data["value"], unit=FrequencyUnits(data["unit"]))


class Frequency(AbstractMeasure):
    """
    The number of occurrences of a repeating event per unit time.

    Args:
        value (float): The value.
        from_unit (FrequencyUnits): The Frequency unit to create from, The default unit is Hertz
    """
    def __init__(self, value: float, from_unit: FrequencyUnits = FrequencyUnits.Hertz):
        # Do not validate type, to allow working with numpay arrays and similar objects who supports all arithmetic 
        # operations, but they are not a number, see #14 
        # if math.isnan(value):
        #     raise ValueError('Invalid unit: value is NaN')
        self._value = self.__convert_to_base(value, from_unit)
        
        self.__hertz = None
        
        self.__radians_per_second = None
        
        self.__cycles_per_minute = None
        
        self.__cycles_per_hour = None
        
        self.__beats_per_minute = None
        
        self.__per_second = None
        
        self.__b_units = None
        
        self.__microhertz = None
        
        self.__millihertz = None
        
        self.__kilohertz = None
        
        self.__megahertz = None
        
        self.__gigahertz = None
        
        self.__terahertz = None
        

    def convert(self, unit: FrequencyUnits) -> float:
        return self.__convert_from_base(unit)

    def to_dto(self, hold_in_unit: FrequencyUnits = FrequencyUnits.Hertz) -> FrequencyDto:
        """
        Get a new instance of Frequency DTO representing the current unit.

        :param hold_in_unit: The specific Frequency unit to store the Frequency value in the DTO representation.
        :type hold_in_unit: FrequencyUnits
        :return: A new instance of FrequencyDto.
        :rtype: FrequencyDto
        """
        return FrequencyDto(value=self.convert(hold_in_unit), unit=hold_in_unit)
    
    def to_dto_json(self, hold_in_unit: FrequencyUnits = FrequencyUnits.Hertz):
        """
        Get a Frequency DTO JSON object representing the current unit.

        :param hold_in_unit: The specific Frequency unit to store the Frequency value in the DTO representation.
        :type hold_in_unit: FrequencyUnits
        :return: JSON object represents Frequency DTO.
        :rtype: dict
        :example return: {"value": 100, "unit": "Hertz"}
        """
        return self.to_dto(hold_in_unit).to_json()

    @staticmethod
    def from_dto(frequency_dto: FrequencyDto):
        """
        Obtain a new instance of Frequency from a DTO unit object.

        :param frequency_dto: The Frequency DTO representation.
        :type frequency_dto: FrequencyDto
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(frequency_dto.value, frequency_dto.unit)

    @staticmethod
    def from_dto_json(data: dict):
        """
        Obtain a new instance of Frequency from a DTO unit json representation.

        :param data: The Frequency DTO in JSON representation.
        :type data: dict
        :example data: {"value": 100, "unit": "Hertz"}
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency.from_dto(FrequencyDto.from_json(data))

    def __convert_from_base(self, from_unit: FrequencyUnits) -> float:
        value = self._value
        
        if from_unit == FrequencyUnits.Hertz:
            return (value)
        
        if from_unit == FrequencyUnits.RadianPerSecond:
            return (value * 6.2831853072)
        
        if from_unit == FrequencyUnits.CyclePerMinute:
            return (value * 60)
        
        if from_unit == FrequencyUnits.CyclePerHour:
            return (value * 3600)
        
        if from_unit == FrequencyUnits.BeatPerMinute:
            return (value * 60)
        
        if from_unit == FrequencyUnits.PerSecond:
            return (value)
        
        if from_unit == FrequencyUnits.BUnit:
            return (value * value * 1e-3)
        
        if from_unit == FrequencyUnits.Microhertz:
            return ((value) / 1e-06)
        
        if from_unit == FrequencyUnits.Millihertz:
            return ((value) / 0.001)
        
        if from_unit == FrequencyUnits.Kilohertz:
            return ((value) / 1000.0)
        
        if from_unit == FrequencyUnits.Megahertz:
            return ((value) / 1000000.0)
        
        if from_unit == FrequencyUnits.Gigahertz:
            return ((value) / 1000000000.0)
        
        if from_unit == FrequencyUnits.Terahertz:
            return ((value) / 1000000000000.0)
        
        return None


    def __convert_to_base(self, value: float, to_unit: FrequencyUnits) -> float:
        
        if to_unit == FrequencyUnits.Hertz:
            return (value)
        
        if to_unit == FrequencyUnits.RadianPerSecond:
            return (value / 6.2831853072)
        
        if to_unit == FrequencyUnits.CyclePerMinute:
            return (value / 60)
        
        if to_unit == FrequencyUnits.CyclePerHour:
            return (value / 3600)
        
        if to_unit == FrequencyUnits.BeatPerMinute:
            return (value / 60)
        
        if to_unit == FrequencyUnits.PerSecond:
            return (value)
        
        if to_unit == FrequencyUnits.BUnit:
            return (math.sqrt(value * 1e3))
        
        if to_unit == FrequencyUnits.Microhertz:
            return ((value) * 1e-06)
        
        if to_unit == FrequencyUnits.Millihertz:
            return ((value) * 0.001)
        
        if to_unit == FrequencyUnits.Kilohertz:
            return ((value) * 1000.0)
        
        if to_unit == FrequencyUnits.Megahertz:
            return ((value) * 1000000.0)
        
        if to_unit == FrequencyUnits.Gigahertz:
            return ((value) * 1000000000.0)
        
        if to_unit == FrequencyUnits.Terahertz:
            return ((value) * 1000000000000.0)
        
        return None


    @property
    def base_value(self) -> float:
        return self._value

    
    @staticmethod
    def from_hertz(hertz: float):
        """
        Create a new instance of Frequency from a value in hertz.

        

        :param meters: The Frequency value in hertz.
        :type hertz: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(hertz, FrequencyUnits.Hertz)

    
    @staticmethod
    def from_radians_per_second(radians_per_second: float):
        """
        Create a new instance of Frequency from a value in radians_per_second.

        

        :param meters: The Frequency value in radians_per_second.
        :type radians_per_second: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(radians_per_second, FrequencyUnits.RadianPerSecond)

    
    @staticmethod
    def from_cycles_per_minute(cycles_per_minute: float):
        """
        Create a new instance of Frequency from a value in cycles_per_minute.

        

        :param meters: The Frequency value in cycles_per_minute.
        :type cycles_per_minute: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(cycles_per_minute, FrequencyUnits.CyclePerMinute)

    
    @staticmethod
    def from_cycles_per_hour(cycles_per_hour: float):
        """
        Create a new instance of Frequency from a value in cycles_per_hour.

        

        :param meters: The Frequency value in cycles_per_hour.
        :type cycles_per_hour: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(cycles_per_hour, FrequencyUnits.CyclePerHour)

    
    @staticmethod
    def from_beats_per_minute(beats_per_minute: float):
        """
        Create a new instance of Frequency from a value in beats_per_minute.

        

        :param meters: The Frequency value in beats_per_minute.
        :type beats_per_minute: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(beats_per_minute, FrequencyUnits.BeatPerMinute)

    
    @staticmethod
    def from_per_second(per_second: float):
        """
        Create a new instance of Frequency from a value in per_second.

        

        :param meters: The Frequency value in per_second.
        :type per_second: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(per_second, FrequencyUnits.PerSecond)

    
    @staticmethod
    def from_b_units(b_units: float):
        """
        Create a new instance of Frequency from a value in b_units.

        

        :param meters: The Frequency value in b_units.
        :type b_units: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(b_units, FrequencyUnits.BUnit)

    
    @staticmethod
    def from_microhertz(microhertz: float):
        """
        Create a new instance of Frequency from a value in microhertz.

        

        :param meters: The Frequency value in microhertz.
        :type microhertz: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(microhertz, FrequencyUnits.Microhertz)

    
    @staticmethod
    def from_millihertz(millihertz: float):
        """
        Create a new instance of Frequency from a value in millihertz.

        

        :param meters: The Frequency value in millihertz.
        :type millihertz: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(millihertz, FrequencyUnits.Millihertz)

    
    @staticmethod
    def from_kilohertz(kilohertz: float):
        """
        Create a new instance of Frequency from a value in kilohertz.

        

        :param meters: The Frequency value in kilohertz.
        :type kilohertz: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(kilohertz, FrequencyUnits.Kilohertz)

    
    @staticmethod
    def from_megahertz(megahertz: float):
        """
        Create a new instance of Frequency from a value in megahertz.

        

        :param meters: The Frequency value in megahertz.
        :type megahertz: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(megahertz, FrequencyUnits.Megahertz)

    
    @staticmethod
    def from_gigahertz(gigahertz: float):
        """
        Create a new instance of Frequency from a value in gigahertz.

        

        :param meters: The Frequency value in gigahertz.
        :type gigahertz: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(gigahertz, FrequencyUnits.Gigahertz)

    
    @staticmethod
    def from_terahertz(terahertz: float):
        """
        Create a new instance of Frequency from a value in terahertz.

        

        :param meters: The Frequency value in terahertz.
        :type terahertz: float
        :return: A new instance of Frequency.
        :rtype: Frequency
        """
        return Frequency(terahertz, FrequencyUnits.Terahertz)

    
    @property
    def hertz(self) -> float:
        """
        
        """
        if self.__hertz != None:
            return self.__hertz
        self.__hertz = self.__convert_from_base(FrequencyUnits.Hertz)
        return self.__hertz

    
    @property
    def radians_per_second(self) -> float:
        """
        
        """
        if self.__radians_per_second != None:
            return self.__radians_per_second
        self.__radians_per_second = self.__convert_from_base(FrequencyUnits.RadianPerSecond)
        return self.__radians_per_second

    
    @property
    def cycles_per_minute(self) -> float:
        """
        
        """
        if self.__cycles_per_minute != None:
            return self.__cycles_per_minute
        self.__cycles_per_minute = self.__convert_from_base(FrequencyUnits.CyclePerMinute)
        return self.__cycles_per_minute

    
    @property
    def cycles_per_hour(self) -> float:
        """
        
        """
        if self.__cycles_per_hour != None:
            return self.__cycles_per_hour
        self.__cycles_per_hour = self.__convert_from_base(FrequencyUnits.CyclePerHour)
        return self.__cycles_per_hour

    
    @property
    def beats_per_minute(self) -> float:
        """
        
        """
        if self.__beats_per_minute != None:
            return self.__beats_per_minute
        self.__beats_per_minute = self.__convert_from_base(FrequencyUnits.BeatPerMinute)
        return self.__beats_per_minute

    
    @property
    def per_second(self) -> float:
        """
        
        """
        if self.__per_second != None:
            return self.__per_second
        self.__per_second = self.__convert_from_base(FrequencyUnits.PerSecond)
        return self.__per_second

    
    @property
    def b_units(self) -> float:
        """
        
        """
        if self.__b_units != None:
            return self.__b_units
        self.__b_units = self.__convert_from_base(FrequencyUnits.BUnit)
        return self.__b_units

    
    @property
    def microhertz(self) -> float:
        """
        
        """
        if self.__microhertz != None:
            return self.__microhertz
        self.__microhertz = self.__convert_from_base(FrequencyUnits.Microhertz)
        return self.__microhertz

    
    @property
    def millihertz(self) -> float:
        """
        
        """
        if self.__millihertz != None:
            return self.__millihertz
        self.__millihertz = self.__convert_from_base(FrequencyUnits.Millihertz)
        return self.__millihertz

    
    @property
    def kilohertz(self) -> float:
        """
        
        """
        if self.__kilohertz != None:
            return self.__kilohertz
        self.__kilohertz = self.__convert_from_base(FrequencyUnits.Kilohertz)
        return self.__kilohertz

    
    @property
    def megahertz(self) -> float:
        """
        
        """
        if self.__megahertz != None:
            return self.__megahertz
        self.__megahertz = self.__convert_from_base(FrequencyUnits.Megahertz)
        return self.__megahertz

    
    @property
    def gigahertz(self) -> float:
        """
        
        """
        if self.__gigahertz != None:
            return self.__gigahertz
        self.__gigahertz = self.__convert_from_base(FrequencyUnits.Gigahertz)
        return self.__gigahertz

    
    @property
    def terahertz(self) -> float:
        """
        
        """
        if self.__terahertz != None:
            return self.__terahertz
        self.__terahertz = self.__convert_from_base(FrequencyUnits.Terahertz)
        return self.__terahertz

    
    def to_string(self, unit: FrequencyUnits = FrequencyUnits.Hertz, fractional_digits: int = None) -> str:
        """
        Format the Frequency to a string.
        
        Note: the default format for Frequency is Hertz.
        To specify the unit format, set the 'unit' parameter.
        
        Args:
            unit (str): The unit to format the Frequency. Default is 'Hertz'.
            fractional_digits (int, optional): The number of fractional digits to keep.

        Returns:
            str: The string format of the Angle.
        """
        
        if unit == FrequencyUnits.Hertz:
            return f"""{super()._truncate_fraction_digits(self.hertz, fractional_digits)} Hz"""
        
        if unit == FrequencyUnits.RadianPerSecond:
            return f"""{super()._truncate_fraction_digits(self.radians_per_second, fractional_digits)} rad/s"""
        
        if unit == FrequencyUnits.CyclePerMinute:
            return f"""{super()._truncate_fraction_digits(self.cycles_per_minute, fractional_digits)} cpm"""
        
        if unit == FrequencyUnits.CyclePerHour:
            return f"""{super()._truncate_fraction_digits(self.cycles_per_hour, fractional_digits)} cph"""
        
        if unit == FrequencyUnits.BeatPerMinute:
            return f"""{super()._truncate_fraction_digits(self.beats_per_minute, fractional_digits)} bpm"""
        
        if unit == FrequencyUnits.PerSecond:
            return f"""{super()._truncate_fraction_digits(self.per_second, fractional_digits)} s⁻¹"""
        
        if unit == FrequencyUnits.BUnit:
            return f"""{super()._truncate_fraction_digits(self.b_units, fractional_digits)} B Units"""
        
        if unit == FrequencyUnits.Microhertz:
            return f"""{super()._truncate_fraction_digits(self.microhertz, fractional_digits)} μHz"""
        
        if unit == FrequencyUnits.Millihertz:
            return f"""{super()._truncate_fraction_digits(self.millihertz, fractional_digits)} mHz"""
        
        if unit == FrequencyUnits.Kilohertz:
            return f"""{super()._truncate_fraction_digits(self.kilohertz, fractional_digits)} kHz"""
        
        if unit == FrequencyUnits.Megahertz:
            return f"""{super()._truncate_fraction_digits(self.megahertz, fractional_digits)} MHz"""
        
        if unit == FrequencyUnits.Gigahertz:
            return f"""{super()._truncate_fraction_digits(self.gigahertz, fractional_digits)} GHz"""
        
        if unit == FrequencyUnits.Terahertz:
            return f"""{super()._truncate_fraction_digits(self.terahertz, fractional_digits)} THz"""
        
        return f'{self._value}'


    def get_unit_abbreviation(self, unit_abbreviation: FrequencyUnits = FrequencyUnits.Hertz) -> str:
        """
        Get Frequency unit abbreviation.
        Note! the default abbreviation for Frequency is Hertz.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == FrequencyUnits.Hertz:
            return """Hz"""
        
        if unit_abbreviation == FrequencyUnits.RadianPerSecond:
            return """rad/s"""
        
        if unit_abbreviation == FrequencyUnits.CyclePerMinute:
            return """cpm"""
        
        if unit_abbreviation == FrequencyUnits.CyclePerHour:
            return """cph"""
        
        if unit_abbreviation == FrequencyUnits.BeatPerMinute:
            return """bpm"""
        
        if unit_abbreviation == FrequencyUnits.PerSecond:
            return """s⁻¹"""
        
        if unit_abbreviation == FrequencyUnits.BUnit:
            return """B Units"""
        
        if unit_abbreviation == FrequencyUnits.Microhertz:
            return """μHz"""
        
        if unit_abbreviation == FrequencyUnits.Millihertz:
            return """mHz"""
        
        if unit_abbreviation == FrequencyUnits.Kilohertz:
            return """kHz"""
        
        if unit_abbreviation == FrequencyUnits.Megahertz:
            return """MHz"""
        
        if unit_abbreviation == FrequencyUnits.Gigahertz:
            return """GHz"""
        
        if unit_abbreviation == FrequencyUnits.Terahertz:
            return """THz"""
        