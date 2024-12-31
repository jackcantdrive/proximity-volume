Automatically adjust volume based on the distance to your phone estimated based on bluetooth strength.

For when you're playing music on a speaker and wandering around, so need loud volume when you're in other rooms in order to hear but don't want to be deafened while you're near.


## Usage

Requires MacOS [^0].

Connect your phone to your laptop's bluetooth.

Set phone bluetooth name under `# config` in `main.py`.

run `python3 main.py`

Play some music via platform of your choice.

[^0]: As we use `system_profiler SPBluetoothDataType` and set the volume via AppleScript. Both of these would be simple to replace on other systems if wanted.

## Config

A logs endpoint is served at http://localhost:5000 to allow seeing the current and recent volumes, and detected signal strengths.

### The volume level adjusting is terrible how do I fix

Change `rssi_to_distance: rssi -> dist` or `dist_to_vol: dist -> vol` in `main.py`.