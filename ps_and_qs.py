from fractions import gcd
from libnum import modular

N1 = 9055404640500300109405801152935663267176218320785348541566663982172162265778445107320065187449062375525002632043722734566593185461999286625234528036605141
N2 = 3367646059138877442579820972831876412006279917097809082279412851693123955964282545145500497393579598954859534731890460229194372339215098506788375050698427369

c = 0xf5ed9da29d8d260f22657e091f34eb930bc42f26f1e023f863ba13bee39071d1ea988ca62b9ad59d4f234fa7d682e22ce3194bbe5b801df3bd976db06b944da
e = 65537

q = gcd(N1, N2)

d = modular.invmod(e, (q-1)*(N1/q-1))

print hex(pow(c, d, N1))[2:-1]