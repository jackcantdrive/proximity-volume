from flask import Flask, jsonify
import subprocess
import math
import threading

# config

DEVICE_NAME = 'J XR'
LOGS_PORT = 5000

def rssi_to_distance(rssi):
    measured_rssi_at_1m = -48
    N = 2.5
    return 10 ** ((measured_rssi_at_1m - rssi) / (10 * N))

def dist_to_vol(dist):
    return math.tanh(dist / 5) * 100

# -*-

app = Flask(__name__)

log_data = []

def get_rssi():
    try:
        result = subprocess.run(
            ["system_profiler", "SPBluetoothDataType"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            output = result.stdout
            index = output.index(f'{DEVICE_NAME}:')
            rest = output[index:]
            rssi_line = rest[rest.index('RSSI: '):]
            rssi = int((rssi_line[len('RSSI: '):rssi_line.index('\n')]).strip())
            return rssi
        else:
            log_data.append(f"Error: {result.stderr.strip()}")
    except Exception as e:
        log_data.append(f"An error occurred: {e}")
    return None

def monitor_devices():
    while True:
        try:
            rssi = get_rssi()
            if rssi is not None:
                dist = rssi_to_distance(rssi)
                vol = dist_to_vol(dist)
                vol = max(0, min(100, vol))
                log_entry = f"RSSI: {rssi}, Distance estimate: {dist:.2f}m, Volume: {vol:.2f}%"
                print(log_entry)
                log_data.append(log_entry)
                subprocess.call([f"osascript -e 'set volume output volume {math.floor(vol)}'"], shell=True)
            else:
                log_data.append("RSSI could not be determined.")
        except Exception as e:
            log_data.append(f"An unexpected error occurred: {e}")

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(log_data[-10:])

if __name__ == "__main__":
    monitor_thread = threading.Thread(target=monitor_devices, daemon=True)
    monitor_thread.start()

    app.run(host="0.0.0.0", port=LOGS_PORT)
