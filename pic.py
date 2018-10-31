import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib as mpl

font = FontProperties(fname=r"", size=14)
mpl.rcParams[u'font.sans-serif'] = ['simhei']
mpl.rcParams['axes.unicode_minus'] = False

data = [0.999036392580471,0.9998684713649801,
0.9905290030978087,0.9997850474002886,
0.9905770273226676,0.9998740904149138,
0.9932029665362749,0.99923821581961,
0.9866969222965276,0.9941881695575714,
0.9507264494494423,0.9371287182012034,
0.9962479535129809,0.8090764708294212,
]

data2 = [
    0.9715540047748966,0.9653088722400138,0.9738280779050008,0.9933614602395705,
    0.38578276993683236,0.6557546205458686,0.9842404839239144,
]

# print(data)

d1 = []
d2 = []
d3 = []
d4 = []
d5 = []
d6 = []
for i in range(len(data)//2):
    d1.append(abs(data[i*2]))
    d2.append(abs(data[i*2+1]))
    d3.append(abs(data2[i]))
    d4.append( d1[i]/(d1[i]+d2[i]+d3[i]) )
    d5.append( d2[i]/(d1[i]+d2[i]+d3[i]) )
    d6.append( d3[i]/(d1[i]+d2[i]+d3[i]) )

print(d1)
print(d2)
print(d3)
print(d4)


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


n_groups = 7

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.25

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, d1, bar_width,
                alpha=opacity, color='b',
                 error_kw=error_config,
                label='服务项目价格指数与总指数相关性')

rects2 = ax.bar(index + bar_width, d2, bar_width,
                alpha=opacity, color='r',
                error_kw=error_config,
                label='食品价格指数与总指数相关性')

rects3 = ax.bar(index + 2* bar_width, d3, bar_width,
                alpha=opacity, color='y',
                error_kw=error_config,
                label='工业品价格指数与总指数相关性')


# ax.plot(d4,'k-o',label='服务项目价格指数占总指数比例')

ax.set_xlabel('时间/ 年')
ax.set_ylabel('与居民消费价格总指数相关度')
# ax.set_title('Scores by group and gender')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('2011', '2012', '2013', '2014', '2015', '2016', '2017'))

ax.legend()
plt.xlim((-0.3, 6.65))
plt.ylim((0.3, 1.2))
fig.tight_layout()
plt.savefig('good.png',dpi = 400)
# plt.show()

# plt.figure(2)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25

opacity = 0.4
error_config = {'ecolor': '0.3'}

ax.plot(d4,'k-o',label='服务项目价格指数与总指数相关性占三种相关性比例')
ax.plot(d5,'g-o',label='工业品价格指数与总指数相关性占三种相关性比例')
ax.plot(d6,'r-o',label='食品价格指数与总指数相关性占三种相关性比例')
ax.set_xticklabels((' ','2011', '2012', '2013', '2014', '2015', '2016', '2017'))
plt.legend()
# plt.xlim((-0.3, 6.65))
plt.ylim((0.15, 0.49))
plt.savefig('good2.png',dpi = 400)
