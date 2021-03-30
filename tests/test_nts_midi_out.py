import time

import pytest

from nts import NTS, FilterType

from .fakeMIDI import FakeMIDIReceiver


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


# TODO: I need to find a better solution for this.
# I'm not sure if its a good idea to put the thread on sleep
def test_set_filter_type(midi_receiver, nts):
    nts.filter_type = FilterType.OFF
    time.sleep(0.1)
    assert midi_receiver.received == [[0xB0, 42, 127]]


def test_set_filter_cutoff(midi_receiver, nts):
    nts.filter_cutoff = 61
    time.sleep(0.1)
    assert midi_receiver.received == [[0xB0, 43, 61]]


def test_set_filter_resonance(midi_receiver, nts):
    nts.filter_resonance = 42
    time.sleep(0.1)
    assert midi_receiver.received == [[0xB0, 44, 42]]
