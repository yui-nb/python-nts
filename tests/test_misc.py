from nts.nts import construct_midi_message


def test_midi_message_construction():
    assert construct_midi_message(1, 77, 24) == (0xB1, 77, 24)
