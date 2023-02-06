import mido
from mido import Message

# Enumerate all available MIDI ports
input_ports = mido.get_input_names()
print("Available input ports:", input_ports)

# Connect to the first available input port
input_port = mido.open_input(input_ports[0])

# Listen for incoming MIDI messages
while True:
    msg = input_port.receive()
    if msg.type == "note_on":
        print("Note On:", msg.note, msg.velocity)
    elif msg.type == "note_off":
        print("Note Off:", msg.note)
