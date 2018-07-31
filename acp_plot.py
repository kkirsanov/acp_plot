import pylab

#f = open("/home/kkirsanov/arm/acplog_new.log", "r")
f = open("/home/kkirsanov/arm/acplog.log", "r")


def flti(s):
    return filter(lambda x: x in "01234567889", s)

times = []
d1 = []
d2 = []
d3 = []
d4 = []
d5 = []
for l in f:
    t, d = l[:-1].split("\t")
    times.append(float(t))
    s = d.split(",")
    s = map(flti, s)
    x1, x2, x3, x4, x5 = map(int, s)
    d1.append(x1)
    d2.append(x2)
    d3.append(x3)
    d4.append(x4)
    d5.append(x5)

m = min(times)
times = map(lambda x:x - m, times)
#print times
T=[]
for x in range(len(times)):
    if x>1:
        T.append(times[x]- times[x-1])

#T=sorted(T)

#exit()
t = [0]
for i, x in enumerate(times):
    if i > 1:
        t.append((x - times[i - 1])* 100) 
#pylab.plot(d1)
pylab.plot(d2, label="V")
#pylab.plot(d3)
#pylab.plot(d4)
pylab.plot(d5, "o-", label='current')
pylab.plot(t, "+-",label='dT*100 ms')
pylab.legend()

pylab.show()
