from datetime import datetime

date1_str = '2015-02-15'
date2 = datetime.now(tz=None).date()

date1 = datetime.strptime(date1_str, '%Y-%m-%d')


d1 = datetime.strptime(str(date2), '%Y-%m-%d')

print(type(datetime.strptime(str(date2), '%Y-%m-%d')), type(date1))
# print(date2 > date1)
