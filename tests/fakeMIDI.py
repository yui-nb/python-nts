"""fakeMIDI Test Module.

Supplies classes for testing purposes.
"""
import rtmidi


class FakeMIDIReceiver:
    """A 'fake MIDI device' used for testing purposes.

    This class uses a virtual MIDI Port to intercept MIDI Messages.
    """

    def __init__(self):
        """Constructor."""
        self.midi_in = rtmidi.MidiIn()
        self.midi_in.open_virtual_port("Korg NTS-1 digital kit MIDI 1")
        self.received = []
        self.midi_in.set_callback(midi_callback, data=self.received)

    def __del__(self):
        """Destructor method closes port and destroys rtmidi instance."""
        self.midi_in.close_port()
        self.midi_in.delete()


def midi_callback(event, data):
    """MIDI callback function."""
    message, _ = event
    data.append(message)
