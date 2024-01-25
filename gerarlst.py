bas = "0123456789abcdefghijklmnoprqstuvwxyz" #36
fi = open("/home/dg/win/Douglas/HACKER/lst/at8.lst","w")
for a in range(0,36):
    for b in range(0,36):
        for c in range(0,36):
            for d in range(0,36):
                for e in range(0,36):
                    for f in range(0,36):
                        for g in range(0,36):
                            t = "@%s%s%s%s%s%s%s\n" % ( bas[a], bas[b], bas[c], bas[d], bas[e], bas[f], bas[g])
                            fi.writelines(t)

fi.close()

