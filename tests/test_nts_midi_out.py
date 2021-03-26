import pytest
from .fakeMIDI import FakeMIDIReceiver
from nts import NTS

@pytest.fixture
def midi_receiver():
    aux = FakeMIDIReceiver()
    yield aux
    del aux

@pytest.fixture
def nts():
    aux = NTS()
    yield aux
    del aux


def test_set_filter_type(midi_receiver, nts):
    nts.filter_type = 127
    assert midi_receiver.received == [[0xB0, 42, 127]]

def test_set_filter_cutoff(midi_receiver, nts):
    nts.filter_cutoff = 61
    assert midi_receiver.received == [[0xB0, 43, 61]]

def test_set_filter_resonance(midi_receiver, nts):
    nts.filter_resonance = 42
    assert midi_receiver.received == [[0xB0, 42, 42]]