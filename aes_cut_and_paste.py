m1 = 'Deposit amount: 5 dollars'
c1 = '5797791557579e322e619f12b0ccdee8802015ee0467c419e7a38bd0a254da54'
m2 = 'One million dolls is quite the collection'
c2 = 'b1e952572d6b8e00b626be86552376e2d529a1b9cafaeb3ba7533d2699636323e7e433c10a9dcdab2ed4bee54da684ca'
m3 = 'Hey nice binoculars'
c3 = '35d0c02036354fdf6082285e0f7bd6d2fdf526bd557b045bce65a3b3e300b55e'


c1 = [c1[i : i + 32] for i in range(0, len(c1), 32)]
c2 = [c2[i : i + 32] for i in range(0, len(c2), 32)]
c3 = [c3[i : i + 32] for i in range(0, len(c3), 32)]

m1 = [m1[i : i + 16] for i in range(0, len(m1), 16)]
m2 = [m2[i : i + 16] for i in range(0, len(m2), 16)]
m3 = [m3[i : i + 16] for i in range(0, len(m3), 16)]

print c1[0]+c2[0]+c3[1]
print m1[0]+m2[0]+m3[1]