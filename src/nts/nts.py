from enum import Enum

import rtmidi

FILTER_TYPE_CC: int = 42
FILTER_CUTOFF_CC: int = 43
FILTER_RESONANCE_CC: int = 44

ENEVELOPE_TYPE_CC: int = 14
ENEVELOPE_ATTACK_CC: int = 16
ENVELOPE_RELEASE_CC: int = 19

OSCILLATOR_SHAPE_CC: int = 54
OSCILLATOR_ALT_CC: int = 55


def construct_midi_message(channel: int, control_change: int, value: int) -> tuple:
    """Constructs a tuple that can be send as a MIDI Message via rtmidi.

    :param channel: MIDI Channel
    :type channel: int
    :param control_change: Control Change
    :type control_change: int
    :param value: Message Value
    :type value: int
    :return: tuple containing the status and data bytes
    :rtype: tuple
    """
    return (0xB0 | channel, control_change, value)


class FilterType(Enum):
    """Enum that represents the filter type and maps it to it's corresponding value."""

    LP2 = 0
    LP4 = 18
    BP2 = 36
    BP4 = 54
    HP2 = 72
    HP4 = 90
    OFF = 127


class EnvelopeType(Enum):
    """Enum representing the Envelope Type and the corresponding MIDI value."""

    ADSR = 0
    AHR = 25
    AR = 50
    ARLOOP = 75
    OPEN = 127


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

        self._eg_type: EnvelopeType = EnvelopeType.ADSR
        self._eg_attack: int = 0
        self._eg_release: int = 0

        self._osc_shape: int = 0
        self._osc_alt: int = 0

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
    def filter_type(self, val: FilterType):
        """Change the filter type.

        :param value: new filter type
        :type value: int
        """
        self._filter_type = val
        self.__midi_out.send_message(
            construct_midi_message(
                self.channel, FILTER_TYPE_CC, self._filter_type.value
            )
        )

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
        self.__midi_out.send_message(
            construct_midi_message(self.channel, FILTER_CUTOFF_CC, self._filter_cutoff)
        )

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
            construct_midi_message(
                self.channel, FILTER_RESONANCE_CC, self._filter_resonance
            )
        )

    @property
    def envelope_type(self) -> EnvelopeType:
        """Returns the envelope type.

        :return: The current envelope type as a EnvelopeType Enum.
        :rtype: EnvelopeType
        """
        return self._eg_type

    @envelope_type.setter
    def envelope_type(self, value: EnvelopeType):
        """Set the envelope type.

        :param value: New envelope Type
        :type value: EnvelopeType
        """
        self._eg_type = value
        self.__midi_out.send_message(
            construct_midi_message(
                self.channel, ENEVELOPE_TYPE_CC, self.envelope_type.value
            )
        )

    @property
    def envelope_attack(self) -> int:
        """Returns the envelope attack value.

        :return: envelope attack
        :rtype: int
        """
        return self._eg_attack

    @envelope_attack.setter
    def envelope_attack(self, value: int):
        """Sets the envelope attack value.

        :param value: new envelope attack
        :type value: int
        """
        self._eg_attack = value
        self.__midi_out.send_message(
            construct_midi_message(self.channel, ENEVELOPE_ATTACK_CC, self._eg_attack)
        )

    @property
    def envelope_release(self) -> int:
        """Returns the envelope release value.

        :return: envelope release
        :rtype: int
        """
        return self._eg_release

    @envelope_release.setter
    def envelope_release(self, value: int):
        """Sets the envelope release value.

        :param value: new envelope release value
        :type value: int
        """
        self._eg_release = value
        self.__midi_out.send_message(
            construct_midi_message(self.channel, ENVELOPE_RELEASE_CC, self._eg_release)
        )

    @property
    def shape(self) -> int:
        """Returns the oscillator shape value.

        :return: oscillator shape
        :rtype: int
        """
        return self._osc_shape

    @shape.setter
    def shape(self, value: int):
        """Sets the oscillator shape value.

        :param value: new oscillator shape
        :type value: int
        """
        self._osc_shape = value
        self.__midi_out.send_message(
            construct_midi_message(self.channel, OSCILLATOR_SHAPE_CC, self._osc_shape)
        )

    @property
    def alt(self) -> int:
        """Returns oscillator alt value.

        :return: oscillator alt
        :rtype: int
        """
        return self._osc_alt

    @alt.setter
    def alt(self, value: int):
        """Sets oscillator alt value.

        :param value: new oscillator alt
        :type value: int
        """
        self._osc_alt = value
        self.__midi_out.send_message(
            construct_midi_message(self.channel, OSCILLATOR_ALT_CC, self._osc_alt)
        )
