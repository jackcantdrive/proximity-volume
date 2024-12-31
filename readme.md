
For when you're playing music on a speaker and wandering around, so need loud volume when you're in other rooms in order to hear but don't want to be deafened while you're near.


## Usage

Connect your phone to your laptop's bluetooth.

Set phone bluetooth name under `# config` in `main.py`.

run `python3 main.py`


## Config

A logs endpoint is served at http://localhost:5000 to allow seeing the current and recent volumes, and detected signal strengths.

### The volume level adjusting is terrible how do I fix

Change `rssi_to_distance: rssi -> dist` or `dist_to_vol: dist -> vol` in `main.py`.