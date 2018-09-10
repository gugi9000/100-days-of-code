from datetime import datetime

start = datetime.now()
lap_timestamp = start
print('Stopwatch is running. Press enter for lap time.')
print('Input anything else to stop the watch.')

laps = 0

while True:
    key = input()
    if len(key) == 0:
        previous_lap = lap_timestamp
        lap_timestamp = datetime.now()
        laps = laps + 1
        print(f'Time lapsed is {lap_timestamp-start}')
        print(f'Lap {laps} time: {lap_timestamp - previous_lap}')
        if laps > 1:
            avg = (lap_timestamp - start)/laps
            print(f'Average lap time is {avg}')
    else:
        print(f'Watch stopped after {datetime.now() - start}')
        break

