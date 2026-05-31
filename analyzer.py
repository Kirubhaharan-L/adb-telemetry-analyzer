import json

critical_failures = []

with open('device_sim.log', 'r') as file:
    # reading line by line, instead of file.read() to avoid RAM crash
    for line in file:
        if '[FATAL]' not in line: # Early skip of the line if its not FATAL
            continue

        data = line.split()

        if len(data) >= 5: # validation for junk data
            # validating the right coulmn for the device name
            device = data[4] if data[3] == 'wpa_supplicant' else data[3]
            # removing the device_ from the device name.
            device = device.removeprefix('device_')

            critical_failures.append({'device': device,'status': data[-1]})
    #dumping the data to the report as json data        
    with open('report.json', 'w') as report:
        json.dump(critical_failures, report, indent=4)
