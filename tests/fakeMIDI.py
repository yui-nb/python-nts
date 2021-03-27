import rtmidi


class FakeMIDIReceiver:
    def __init__(self):
        self.midi_in = rtmidi.MidiIn()
        self.midi_in.open_virtual_port("Korg NTS-1 digital kit MIDI 1")
        self.received = []
        self.midi_in.set_callback(midi_callback, data=self.received)

    def __del__(self):
        self.midi_in.close_port()
        self.midi_in.delete()


def midi_callback(event, data):
    message, _ = event
    data.append(message)
