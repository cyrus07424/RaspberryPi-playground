import ambient
import thermal_zone
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
        # Get temperature
        zone_paths = thermal_zone.get_thermal_zone_paths()
        zone_names = thermal_zone.get_thermal_zone_names(zone_paths)
        zone_temps = thermal_zone.get_thermal_zone_temps(zone_paths)
        # Convert to celsius
        zone_temps = [t / 1000.0 for t in zone_temps]

        # Upload data to Ambient
        ambientData = {}
        for i, zone_name in enumerate(zone_names):
            if zone_name == 'cpu-thermal':
                ambientData['d1'] = zone_temps[i]
        r = am.send(ambientData)
    except requests.exceptions.RequestException as e:
        print(e)
    # Wait
    time.sleep(60)
