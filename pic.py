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

# print(data)

d1 = []
d2 = []
d3 = []
for i in range(len(data)//2):
    d1.append(data[i*2])
    d2.append(data[i*2+1])
    d3.append(data[i*2]/data[i*2+1]*0.75)
print(d1)
print(d2)


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


n_groups = 7

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, d1, bar_width,
                alpha=opacity, color='b',
                 error_kw=error_config,
                label='服务项目价格指数')

rects2 = ax.bar(index + bar_width, d2, bar_width,
                alpha=opacity, color='r',
                error_kw=error_config,
                label='消费品价格指数')
ax.plot(d3,'r-o')

ax.set_xlabel('时间/ 年')
ax.set_ylabel('与居民消费价格总指数相关度')
# ax.set_title('Scores by group and gender')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('2011', '2012', '2013', '2014', '2015', '2016', '2017'))

ax.legend()
plt.xlim((-0.3, 6.65))
plt.ylim((0.6, 1.2))
fig.tight_layout()
plt.show()