"""

If a runner runs 10 miles in 30 minites and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km"""

kilometers = float(10 * 1.6)
percent_hour = float(30.5 / 60)
kph = kilometers * percent_hour
print(f'10 miles in 30 minutes and 30 seconds is equal to %.2f kilometers per hour' % kph)


# or as a function
def mph_to_kph(miles, minutes):
    kilomters = float(1.6 * miles)
    percent_hours = float(minutes / 60)
    kph = kilometers * percent_hours
    print(f'{miles} miles in {minutes} minutes is equal to {kph:.2f}.')


mph_to_kph(10, 30.5)