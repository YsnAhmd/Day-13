import datetime
d = datetime.date.today()
print(d)

x = datetime.datetime.now()

print(x.strftime("Date: %d/%m/%Y \
     Time: %I:%M:%S %p"))