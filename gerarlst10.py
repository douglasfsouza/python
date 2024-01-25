#bas = "@abcdefghi&jklmnopr-0123456789.qstuvwxyz#_ABCDEFGHIJK*LMNOPQR$STUVWXYZ!"#from datetime import date
from datetime import datetime
#date.today()
#datetime.now()
bas = "0123456789"
cont=0
cgeral=0
ai = 0
bi = 0
ci = 0
di = 0
ei = 0
fi = 0
gi = 0
hi = 0
ii = 0
ji = 0
#carregar dados do log
temlog = 0
try:
    flog = open("log10.log","r")
    temlog = 1
except IOError:
    temlog = 0
if (temlog ==1):
    llog = str.split(flog.readline(),",")
    ai = int(llog[0])
    bi = int(llog[1])
    ci = int(llog[2])
    di = int(llog[3])
    ei = int(llog[4])
    fi = int(llog[5])
    gi = int(llog[6])
    hi = int(llog[7])
    ii = int(llog[8])
    ji = int(llog[9])
    cgeral = int(llog[11])
    flog.close()

for a in range(ai,len(bas)):
    for b in range(bi,len(bas)):
        for c in range(ci,len(bas)):
            for d in range(di,len(bas)):
                for e in range(ei,len(bas)):
                    for f in range(fi,len(bas)):
                        for g in range(gi,len(bas)):
                            for h in range(hi,len(bas)):
                                for i in range(ii,len(bas)):
                                    for j in range(ji,len(bas)):
                                        t = "%s%s%s%s%s%s%s%s%s%s" % ( bas[a], bas[b], bas[c], bas[d], bas[e], bas[f], bas[g],bas[h],bas[i],bas[j])
                                        cont = cont + 1
                                        cgeral = cgeral + 1
                                        if (cont ==100000):
                                            ntime = datetime.now()
                                            ttime = ntime.strftime("%d-%m-%y %H:%M")


                                            flog=open("log10.log","w")
                                            flog.writelines("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, - %s, %s, keys \n" % (a,b,c,d,e,f,g,h,i,j,ttime,cgeral))
                                            flog.close()
                                            cont = 0
                                
                                        print(t)
                                    ji = 0
                                ii = 0
                            hi = 0
                        gi = 0
                    fi = 0
                ei = 0
            di = 0
        ci = 0
    bi = 0
ai = 0


