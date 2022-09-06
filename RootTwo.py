import math

precision = int(1000000)

target = int(2 * 10 ** (2 * precision))

x = int(10 ** precision)

for i in range(math.ceil(math.log2(precision))):
    x = int((x + (target // x)) // 2)

out = str(x)

print(out)