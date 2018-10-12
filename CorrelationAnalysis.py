import xlrd
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['STSong']


def GetDataMonth1(year, month, row, column):
    worksheet = xlrd.open_workbook('data/' +
                                   str(year)+str(month)+'.xls')
    sheet_names = worksheet.sheet_names()
    sheet2 = worksheet.sheet_by_name('指数')
    rows = sheet2.row_values(row-1)

    return rows[column-1]


def GetDataMonth2(year, month, row, column):
    txt = '河北省—'+str(year)+'年'+str(month)+'月居民消费价格涨跌构成表'
    worksheet = xlrd.open_workbook('data/'+str(year)+str(month)+'.xls')
    sheet_names = worksheet.sheet_names()
    sheet2 = worksheet.sheet_by_name(txt[4:])
    rows = sheet2.row_values(row-1)

    return rows[column-1]


def GetDataYear1(year, row, column):
    data2016 = []
    for i in range(12):
        monthdata = GetDataMonth1(year, i+1, row, column)
        data2016.append(monthdata)
    return data2016


def GetDataYear2(year, row, column):
    data2016 = []
    for i in range(12):
        monthdata = GetDataMonth2(year, i+1, row, column)
        data2016.append(monthdata)
    return data2016


def loaddata():
    data = {}

    data['TotalIndex_2016'] = GetDataYear1(2016, 11, 5)
    data['ServicePriceIndex_2016'] = GetDataYear1(2016, 15, 5)
    data['IndustryPriceIndex_2016'] = GetDataYear1(2016, 16, 5)
    data['EatingPriceIndex_2016'] = GetDataYear1(2016, 25, 5)

    data['TotalIndex_2017'] = GetDataYear1(2017, 11, 5)
    data['ServicePriceIndex_2017'] = GetDataYear1(2017, 15, 5)
    data['IndustryPriceIndex_2017'] = GetDataYear1(2017, 16, 5)
    data['EatingPriceIndex_2017'] = GetDataYear1(2017, 25, 5)

    data['TotalIndex_2011'] = GetDataYear2(2011, 8, 5)
    data['ServicePriceIndex_2011'] = GetDataYear2(2011, 12, 5)
    data['IndustryPriceIndex_2011'] = GetDataYear2(2011, 13, 5)
    data['EatingPriceIndex_2011'] = GetDataYear2(2011, 17, 5)

    data['TotalIndex_2012'] = GetDataYear2(2012, 8, 5)
    data['ServicePriceIndex_2012'] = GetDataYear2(2012, 12, 5)
    data['IndustryPriceIndex_2012'] = GetDataYear2(2012, 13, 5)
    data['EatingPriceIndex_2012'] = GetDataYear2(2012, 17, 5)

    data['TotalIndex_2013'] = GetDataYear2(2013, 8, 5)
    data['ServicePriceIndex_2013'] = GetDataYear2(2013, 12, 5)
    data['IndustryPriceIndex_2013'] = GetDataYear2(2013, 13, 5)
    data['EatingPriceIndex_2013'] = GetDataYear2(2013, 17, 5)

    data['TotalIndex_2014'] = GetDataYear2(2014, 8, 5)
    data['ServicePriceIndex_2014'] = GetDataYear2(2014, 12, 5)
    data['IndustryPriceIndex_2014'] = GetDataYear2(2014, 13, 5)
    data['EatingPriceIndex_2014'] = GetDataYear2(2014, 17, 5)

    data['TotalIndex_2015'] = GetDataYear2(2015, 8, 5)
    data['ServicePriceIndex_2015'] = GetDataYear2(2015, 12, 5)
    data['IndustryPriceIndex_2015'] = GetDataYear2(2015, 13, 5)
    data['EatingPriceIndex_2015'] = GetDataYear2(2015, 17, 5)

    TotalIndex = []
    ServicePriceIndex = []
    IndustryPriceIndex = []
    EatingPriceIndex = []
    for i in range(7):
        for j in range(12):
            TotalIndex.append(data['TotalIndex_201'+str(i+1)][j])
            ServicePriceIndex.append(data['ServicePriceIndex_201'+str(i+1)][j])
            IndustryPriceIndex.append(
                data['IndustryPriceIndex_201'+str(i+1)][j])
            EatingPriceIndex.append(
                data['EatingPriceIndex_201'+str(i+1)][j])

    for i in range(len(TotalIndex)):
        if i > 0:
            TotalIndex[i] = TotalIndex[i-1] * TotalIndex[i]/100
            ServicePriceIndex[i] = ServicePriceIndex[i-1] * \
                ServicePriceIndex[i]/100
            IndustryPriceIndex[i] = IndustryPriceIndex[i-1] * \
                IndustryPriceIndex[i]/100
            EatingPriceIndex[i] = EatingPriceIndex[i - 1] * \
                EatingPriceIndex[i]/100
        else:
            TotalIndex[i] = TotalIndex[i]

    # print(TotalIndex)

    return data, TotalIndex, ServicePriceIndex, EatingPriceIndex, IndustryPriceIndex


# Calculate the difference between each item and the mean
def mean(x):
    return sum(x) / len(x)


def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


# Auxiliary calculation function: dot product 、sum_of_squares
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    return dot(v, v)


# variance
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


# standard_deviation
def standard_deviation(x):
    return math.sqrt(variance(x))


# covariance
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


# correlation
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0


def main():
    data, TotalIndex, ServicePriceIndex, EatingPriceIndex, IndustryPriceIndex = loaddata()

    print(TotalIndex)
    print(ServicePriceIndex)
    print(EatingPriceIndex)

    cov_between_total_and_ser = []
    for i in range(len(TotalIndex)-12+1):
        cov_between_total_and_ser.append(correlation(
            TotalIndex[i:i+12], ServicePriceIndex[i:i+12]))

    cov_between_total_and_Ind = []
    for i in range(len(TotalIndex)-12+1):
        cov_between_total_and_Ind.append(correlation(
            TotalIndex[i:i+12], IndustryPriceIndex[i:i+12]))

    cov_between_total_and_con = []
    for i in range(len(TotalIndex)-12+1):
        cov_between_total_and_con.append(correlation(
            TotalIndex[i:i+12], EatingPriceIndex[i:i+12]))

    print(cov_between_total_and_ser)
    print(cov_between_total_and_con)
    print(cov_between_total_and_Ind)

    out1 = ''

    for i in range(6):
        for j in range(12):
            out1 += str(cov_between_total_and_con[i*12+j])+','

        out1 += '\n'
    out1 += str(cov_between_total_and_con[i*12+j+1])+','

    f = open('out1.csv', 'w')
    f.write(out1)
    f.close()

    out2 = ''

    for i in range(6):
        for j in range(12):
            out2 += str(cov_between_total_and_ser[i*12+j])+','

        out2 += '\n'
    out2 += str(cov_between_total_and_ser[i*12+j+1])+','

    out3 = ''

    f = open('out2.csv', 'w')
    f.write(out2)
    f.close()

    for i in range(6):
        for j in range(12):
            out3 += str(cov_between_total_and_Ind[i*12+j])+','

        out3 += '\n'
    out3 += str(cov_between_total_and_Ind[i*12+j+1])+','

    f = open('out3.csv', 'w')
    f.write(out3)
    f.close()

    c1 = []
    c2 = []
    c3 = []

    for i in range(len(TotalIndex)-12):
        c1.append(cov_between_total_and_ser[i]/(cov_between_total_and_Ind[i] +
                                                cov_between_total_and_ser[i]+cov_between_total_and_con[i]))
        c2.append(cov_between_total_and_con[i]/(cov_between_total_and_Ind[i] +
                                                cov_between_total_and_ser[i]+cov_between_total_and_con[i]))
        c3.append(cov_between_total_and_Ind[i]/(cov_between_total_and_Ind[i] +
                                                cov_between_total_and_ser[i]+cov_between_total_and_con[i]))

    plt.figure(1)
    names = []

    for i in range(12*7):
        if i % 12 == 0:
            names.append(str(i//12+2011))
        else:
            names.append('')
    my_x_ticks = np.arange(0, 7*12, 7)
    # plt.xticks(my_x_ticks)
    # plt.yticks(my_y_ticks)
    plt.xticks(range(len(names)), names, rotation=10)

    plt.plot(cov_between_total_and_con, 'r', label='食品价格指数与总指数相关性')
    plt.plot(cov_between_total_and_ser, 'k', label='服务价格指数与总指数相关性')
    plt.plot(cov_between_total_and_Ind, 'y', label='工业品价格指数与总指数相关性')
    plt.legend()
    plt.grid()
    plt.xlabel('时间 / 年')
    plt.ylabel('相关性')

    plt.savefig('pic1.png', dpi=400)

    plt.figure(2)
    # plt.plot(c2,'r')
    plt.plot(c1, 'k')
    f = open('dataout.csv', 'w')
    for i in range(len(TotalIndex)//12):
        f.write(str(cov_between_total_and_ser[i*12]) +
                ','+str(cov_between_total_and_con[i*12])+'\n')

    plt.savefig('pic2.png', dpi=400)


if __name__ == '__main__':
    main()
