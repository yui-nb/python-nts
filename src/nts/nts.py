from enum import Enum
import rtmidi


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
        self.__midi_out = rtmidi.MidiOut()
        self.__midi_out.open_port(self.get_port_index())
        self.channel = channel

    def get_port_index(self) -> int:
        for index, port in enumerate(self.__midi_out.get_ports()):
            if "NTS" in port:
                return index
        return -1

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

