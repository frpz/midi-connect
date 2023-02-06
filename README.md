# Midi connect

This repo contains scripts that are usefull to make a raspberry pi auto connect usb midi devices.

## main script

to run the script manually:

```
python autoconnect.py
```

> Note: python3 must be installed.

## Autorun

To have the script run everytime a usb device is connected:

```
sudo cp 33-midiusb.rules /etc/udev/rules.d/
sudo udevadm control --reload
sudo service udev restart
```

> Note: edit the path in rule file to match the path of the autoconnect.py script.

> source: https://neuma.studio/rpi-midi-complete.html

## Read-only mode

To be able to turn off raspberry without damaging the sd card:

```
git clone https://gitlab.com/larsfp/rpi-readonly
cd rpi-readonly
sudo ./setup.sh
```

