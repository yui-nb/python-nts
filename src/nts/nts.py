from enum import Enum
import rtmidi

FILTER_TYPE_CC = 42
FILTER_CUTOFF_CC = 43
FILTER_RESONANCE_CC = 44


class FilterType(Enum):
    LP2 = 0
    LP4 = 18
    BP2 = 36
    BP4 = 54
    HP2 = 72
    HP4 = 90
    OFF = 127


class NTS:
    def __init__(self, channel: int = 0):
        self.__midi_out = rtmidi.MidiOut()
        self.__midi_out.open_port(self.get_port_index())
        self.channel: int = channel

        self._filter_type: FilterType = FilterType.OFF
        self._filter_cutoff: int = 0
        self._filter_resonance: int = 0

    def get_port_index(self) -> int:
        for index, port in enumerate(self.__midi_out.get_ports()):
            if "NTS" in port:
                return index
        return -1

    @property
    def filter_type(self) -> FilterType:
        return self._filter_type

    @filter_type.setter
    def filter_type(self, value: int):
        self._filter_type = FilterType(value)
        self.__midi_out.send_message([0xB0, FILTER_TYPE_CC, self._filter_type.value])

    @property
    def filter_cutoff(self) -> int:
        return self._filter_cutoff

    @filter_cutoff.setter
    def filter_cutoff(self, value: int):
        self._filter_cutoff = value
        self.__midi_out.send_message([0xB0, FILTER_CUTOFF_CC, self._filter_cutoff])

    @property
    def filter_resonance(self) -> int:
        return self._filter_resonance

    @filter_resonance.setter
    def filter_resonance(self, value: int):
        self._filter_resonance = value
        self.__midi_out.send_message(
            [0xB0, FILTER_RESONANCE_CC, self._filter_resonance]
        )
