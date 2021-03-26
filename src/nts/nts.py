from enum import Enum

class FilterType(Enum):
    LP2 = 0
    LP4 = 18
    BP2 = 36
    BP4 = 54
    HP2 = 72
    HP4 = 90
    OFF = 127

class NTS:

    def __init__(self, channel:int =0):
        pass

    @property
    def filter_type(self) -> FilterType:
        pass

    @filter_type.setter
    def filter_type(self, value: int):
        pass

    @property
    def filter_cutoff(self) -> int:
        pass

    @filter_cutoff.setter
    def filter_cutoff(self, value: int):
        pass

    @property
    def filter_resonance(self) -> int:
        pass

    @filter_resonance.setter
    def filter_resonance(self, value: int):
        pass

