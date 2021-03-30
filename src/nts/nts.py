from enum import Enum

import rtmidi

FILTER_TYPE_CC = 42
FILTER_CUTOFF_CC = 43
FILTER_RESONANCE_CC = 44


class FilterType(Enum):
    """Enum that represents the filter type and maps it to it's corresponding value."""

    LP2 = 0
    LP4 = 18
    BP2 = 36
    BP4 = 54
    HP2 = 72
    HP4 = 90
    OFF = 127


class NTS:
    """This class represents a NTS-1 and all settings that are accessible via MIDI."""

    def __init__(self, channel: int = 0):
        """Set channel, initializes settings and establishes MIDI Connection.

        :param channel: [description], defaults to 0
        :type channel: int
        """
        # TODO: Add error handling
        self.__midi_out = rtmidi.MidiOut()
        self.__midi_out.open_port(self.get_port_index())
        self.channel: int = channel

        self._filter_type: FilterType = FilterType.OFF
        self._filter_cutoff: int = 0
        self._filter_resonance: int = 0

    # TODO: The constructor should propably take a port instead of searching for one
    def get_port_index(self) -> int:
        """Return the port index of a connected NTS-1.

        :return: Port Index
        :rtype: int
        """
        for index, port in enumerate(self.__midi_out.get_ports()):
            if "NTS" in port:
                return index
        return -1

    @property
    def filter_type(self) -> FilterType:
        """Return the current Filter Type.

        :return: FilterType Enum
        :rtype: FilterType
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, value: int):
        """Change the filter type.

        :param value: new filter type
        :type value: int
        """
        self._filter_type = FilterType(value)
        self.__midi_out.send_message([0xB0, FILTER_TYPE_CC, self._filter_type.value])

    @property
    def filter_cutoff(self) -> int:
        """Return filter cutoff value.

        :return: filter cutoff
        :rtype: int
        """
        return self._filter_cutoff

    @filter_cutoff.setter
    def filter_cutoff(self, value: int):
        """Set filter cutoff.

        :param value: new filter cutoff
        :type value: int
        """
        self._filter_cutoff = value
        self.__midi_out.send_message([0xB0, FILTER_CUTOFF_CC, self._filter_cutoff])

    @property
    def filter_resonance(self) -> int:
        """Return filter resonance value.

        :return: filter resonance
        :rtype: int
        """
        return self._filter_resonance

    @filter_resonance.setter
    def filter_resonance(self, value: int):
        """Set filter resonance.

        :param value: new filter resonance value
        :type value: int
        """
        self._filter_resonance = value
        self.__midi_out.send_message(
            [0xB0, FILTER_RESONANCE_CC, self._filter_resonance]
        )
