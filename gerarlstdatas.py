#bas = "@abcdefghi&jklmnopr-0123456789.qstuvwxyz#_ABCDEFGHIJK*LMNOPQR$STUVWXYZ!"#from datetime import date
#from datetime import datetime
from datetime import *
#date.today()
#datetime.now()

d = datetime.now()
d = d - timedelta(days=200)
for i in range(1,200):
    d = d + timedelta(days=1)
    print(d.strftime("%d-%m-%y"))
    print(d.strftime("%d/%m/%y"))
    print(d.strftime("%d.%m.%y"))
    print(d.strftime("%d%m%y"))
    print("%a-%a-%a" % (d.day, d.month,d.year))
    print("%a/%a/%a" % (d.day, d.month,d.year))
    print("%a%a%a" % (d.day, d.month,d.year))
    print("%a%a%a" % (d.year, d.month, d.day))
    print("%a-%a-%a" % (d.year,d.month,d.day))
    print("%a/%a/%a" % (d.year,d.month,d.day))
    print("%a%a%a" % (d.year,d.month,d.day))
    
    #formatando com zeros a esquerda
    print("%s-%s-%s" % (str(d.day).zfill(2), str(d.month).zfill(2),d.year))
    print("%s/%s/%s" % (str(d.day).zfill(2), str(d.month).zfill(2),d.year))
    print("%s%s%s" % (str(d.day).zfill(2), str(d.month).zfill(2),d.year))
    print("%s%s%s" % (d.year, str(d.month).zfill(2), str(d.day).zfill(2)))
    print("%s-%s-%s" % (d.year,str(d.month).zfill(2),str(d.day).zfill(2)))
    print("%s/%s/%s" % (d.year,str(d.month).zfill(2),str(d.day).zfill(2)))
    print("%s%s%s" % (d.year,str(d.month).zfill(2),str(d.day).zfill(2)))





