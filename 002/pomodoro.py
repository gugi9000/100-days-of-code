from datetime import datetime
from datetime import timedelta

print('How long should your proverbial tomatoes cook?')
print("I'm going to assume, that if you input garbage it means zero.")


hours = input('Hours (<enter> for none): ')
cooking_time = 0
if hours.isdigit():
    hours = int(hours)
    print(f'Okay, {hours} hours. Got it.')
    cooking_time = hours * 60 * 60


minutes = input('And minutes?: ')
if minutes.isdigit():
    print(f'Okay, {minutes} minutes. Got it.')
    minutes = int(minutes)
    cooking_time = cooking_time + (minutes * 60)


seconds = input(f'Seconds? (the time unit - cook your tomatoes first): ')
if seconds.isdigit():
    seconds = int(seconds)
    print(f'Okay, {seconds} seconds. Got it.')
    cooking_time = cooking_time + seconds

start = datetime.now()
print(f'Cooking timer is set - will expire in {cooking_time} seconds..')
print('You can press enter and q to stop -- or just wait')
print('..no ctrl-c to break - that\'s it.')
cooking_time = timedelta(0, cooking_time)

while True:

    # print(f'{datetime.now()-start} lapsed .. {cooking_time} - {datetime.now()}')
    if start+cooking_time < datetime.now():
        print(f'Ding ding ding!')
        break
