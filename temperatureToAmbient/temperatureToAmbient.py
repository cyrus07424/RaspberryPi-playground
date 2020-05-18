import ambient
import thermal_zone
import psutil
import requests
import time

# Constants
ambientChannelId = ''
ambientWriteKey = ''

# Initialize Ambient
am = ambient.Ambient(ambientChannelId, ambientWriteKey)

# Upload to Ambient in a loop forever
while True:
    try:
        # Ambient data
        ambientData = {}

        # Get temperatures
        zone_paths = thermal_zone.get_thermal_zone_paths()
        zone_names = thermal_zone.get_thermal_zone_names(zone_paths)
        zone_temps = thermal_zone.get_thermal_zone_temps(zone_paths)
        # Convert to celsius
        zone_temps = [t / 1000.0 for t in zone_temps]

        # Set temperatures to Ambient data
        for i, zone_name in enumerate(zone_names):
            if zone_name == 'cpu-thermal':
                ambientData['d1'] = zone_temps[i]

        # Get CPU usage
        cpu_percent = psutil.cpu_percent(interval = 1)
        ambientData['d2'] = cpu_percent

        # Get memory usage
        memory = psutil.virtual_memory()
        ambientData['d3'] = memory.percent

        # Upload data to Ambient
        print(ambientData)
        r = am.send(ambientData)
    except requests.exceptions.RequestException as e:
        print(e)
    # Wait
    time.sleep(60)
