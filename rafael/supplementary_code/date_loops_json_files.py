import datetime

start_date = datetime.datetime.strptime('2007-06-18', '%Y-%m-%d')
print(start_date.strftime('%Y-%m-%d'))

# adds a week to the start date
end_date = start_date + datetime.timedelta(days=7)


print(end_date.strftime('%Y-%m-%d'))

#today's date
print(datetime.datetime.today().strftime('%Y-%m-%d'))


    