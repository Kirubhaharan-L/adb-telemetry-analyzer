import random
import datetime

severity = ['[INFO]', '[DEBUG]', '[FATAL]', '[WARNING]']
garbage = ['&', '%', '^', '$', '@', '*']
device = ['Pixel_7', 'Pixel_8a', 'Pixel_9', 'Pixel_10_XL']
device_status = ['Connected', 'Disconnected', 'No Status']
wpa = ['wpa_supplicant', '']

with open('device_sim.log', 'w') as file:
    for i in range(10000):
        now = datetime.datetime.now()
        sev = random.choice(severity)
        w = random.choice(wpa)
        dev = random.choice(device)
        stat = random.choice(device_status)
        
        file.write(f'{now.strftime("%Y-%m-%d %H:%M:%S")} {sev} {w} {dev} {stat}\n')
        
  
        s = random.randint(0, 25)
        if s in range(0, 5):
            file.write(random.choice(garbage) * s + '\n')
