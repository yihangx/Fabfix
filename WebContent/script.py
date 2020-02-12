from sys import argv
s = argv[0]


oneThread = [0,0,0]
tenThread = [0,0,0]
tenThreadHttps = [0,0,0]
tenThreadNoPS = [0,0,0]
tenThreadNoCP = [0,0,0]
balanceOneThread = [0,0,0]
balanceTenThread = [0,0,0]
balanceTenThreadNoPS = [0,0,0]
balanceTenThreadNoCP = [0,0,0]

for i in argv[1:]:
    log = open(i, 'r')
    for lines in log:
        if 'oneThread' in lines:
            t = (lines.strip().split(':'))[1]
            t = t.strip().split(',')
            oneThread[0] += int(t[0])
            oneThread[1] += int(t[1])
            oneThread[2] += 1
        if 'tenThread' in lines:
            t = (lines.strip().split(':'))[1]
            t = t.strip().split(',')
            tenThread[0] += int(t[0])
            tenThread[1] += int(t[1])
            tenThread[2] += 1
        if 'tenThreadHttps' in lines:
            t = (lines.strip().split(':'))[1]
            t = t.strip().split(',')
            tenThreadHttps[0] += int(t[0])
            tenThreadHttps[1] += int(t[1])
            tenThreadHttps[2] += 1
        if 'tenThreadNoPS' in lines:
            t = (lines.strip().split(':'))[1]
            t = t.strip().split(',')
            tenThreadNoPS[0] += int(t[0])
            tenThreadNoPS[1] += int(t[1])
            tenThreadNoPS[2] += 1
        if 'tenThreadNoCP' in lines:
            t = (lines.strip().split(':'))[1]
            t = t.strip().split(',')
            tenThreadNoCP[0] += int(t[0])
            tenThreadNoCP[1] += int(t[1])
            tenThreadNoCP[2] += 1
        if 'balanceOneThread' in lines:
            t = (lines.strip().split(':'))[1]
            t = t.strip().split(',')
            balanceOneThread[0] += int(t[0])
            balanceOneThread[1] += int(t[1])
            balanceOneThread[2] += 1
        if 'balanceTenThread' in lines:
            t = (lines.strip().split(':'))[1]
            t = t.strip().split(',')
            balanceTenThread[0] += int(t[0])
            balanceTenThread[1] += int(t[1])
            balanceTenThread[2] += 1
        if 'balanceTenThreadNoPS' in lines:
            t = (lines.strip().split(':'))[1]
            t = t.strip().split(',')
            balanceTenThreadNoPS[0] += int(t[0])
            balanceTenThreadNoPS[1] += int(t[1])
            balanceTenThreadNoPS[2] += 1
        if 'balanceTenThreadNoCP' in lines:
            t = (lines.strip().split(':'))[1]
            t = t.strip().split(',')
            balanceTenThreadNoCP[0] += int(t[0])
            balanceTenThreadNoCP[1] += int(t[1])
            balanceTenThreadNoCP[2] += 1

#TS: average time takes for the search servlet to run completely for a query
#TJ: average time spent on the parts that use JDBC per query

print("Single-instance cases: ")
print("\n\t Use HTTP, 1 thread in JMeter: \n")
print("\t\t TS: ", oneThread[0]/oneThread[2]/1000000 ,"\n\t\t TJ: ", oneThread[1]/oneThread[2]/1000000)
print("\n\t Use HTTP, 10 threads in JMeter: \n")
print("\t\t TS: ", tenThread[0]/tenThread[2]/1000000 ,"\n\t\t TJ: ", tenThread[1]/tenThread[2]/1000000)
print("\n\t Use HTTPS, 10 threads in JMeter: \n")
print("\t\t TS: ", tenThreadHttps[0]/tenThreadHttps[2]/1000000 ,"\n\t\t TJ: ", tenThreadHttps[1]/tenThreadHttps[2]/1000000)
print("\n\t Use HTTP, 10 threads in JMeter without using prepared statements: \n")
print("\t\t TS: ", tenThreadNoPS[0]/tenThreadNoPS[2]/1000000 ,"\n\t\t TJ: ", tenThreadNoPS[1]/tenThreadNoPS[2]/1000000)
print("\n\t Use HTTP, 10 threads in JMeter without using conneciton pooling: \n")
print("\t\t TS: ", tenThreadNoCP[0]/tenThreadNoCP[2]/1000000 ,"\n\t\t TJ: ", tenThreadNoCP[1]/tenThreadNoCP[2]/1000000)

print("\n Scaled-version cases: ")
print("\n\t Use HTTP, 1 threads in JMeter: \n")
print("\t\t TS: ", balanceOneThread[0]/balanceOneThread[2]/1000000 ,"\n\t\t TJ: ", balanceOneThread[1]/balanceOneThread[2]/1000000)
print("\n\t Use HTTP, 10 threads in JMeter: \n")
print("\t\t TS: ", balanceTenThread[0]/balanceTenThread[2]/1000000 ,"\n\t\t TJ: ", balanceTenThread[1]/balanceTenThread[2]/1000000)
print("\n\t Use HTTP, 10 threads in JMeter without using prepared statements: \n")
print("\t\t TS: ", balanceTenThreadNoPS[0]/balanceTenThreadNoPS[2]/1000000 ,"\n\t\t TJ: ", balanceTenThreadNoPS[1]/balanceTenThreadNoPS[2]/1000000)
print("\n\t Use HTTP, 10 threads in JMeter without using conneciton pooling: \n")
print("\t\t TS: ", balanceTenThreadNoCP[0]/balanceTenThreadNoCP[2]/1000000 ,"\n\t\t TJ: ", balanceTenThreadNoCP[1]/balanceTenThreadNoCP[2]/1000000)















