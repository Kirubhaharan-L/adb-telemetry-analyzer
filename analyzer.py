with open('device_sim.log', 'r') as file:
    for line in file:

        if '[FATAL]' not in line:
            continue

        data = line.split()

        if len(data) >= 4:
            device = data[4] if data[3] == 'wpa_supplicant' else data[3]
            print(f'CRITICAL ALERT: {device} reported {data[-1]}')
