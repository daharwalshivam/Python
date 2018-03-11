x = int(input('enter seconds: '))
day = hr = mint = sec = 0
day = x//86400
rem_day_sec = x%86400
hr = rem_day_sec//3600
rem_hr_sec = rem_day_sec%3600
mint = rem_hr_sec//60
sec = rem_hr_sec%60
print('day',day)
print('hour',hr)
print('minute',mint)
print('seconds',sec)
