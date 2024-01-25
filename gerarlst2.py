#                1         2         3
#      012345678901234567890123456789012345
bas = "0123456789abcdefghijklmnoprqstuvwxyz" #36
i=0
for a in range(0,36):
    for b in range(0,36):
        for c in range(0,36):
            for d in range(0,36):
                for e in range(0,36):
                    for f in range(0,36):
                        for g in range(0,36):
                            t = "@%s%s%s%s%s%s%s" % ( bas[a], bas[b], bas[c], bas[d], bas[e], bas[f], bas[g])
                            i = i + 1
                            if (i ==1000):
                                print("@ndroid1977")
                            else:    
                                print(t)


