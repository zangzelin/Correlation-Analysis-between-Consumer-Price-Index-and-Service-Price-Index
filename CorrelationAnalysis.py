import xlrd
import math
import matplotlib.pyplot as plt


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
    data['ConsumerPriceIndex_2016'] = GetDataYear1(2016, 18, 5)

    data['TotalIndex_2017'] = GetDataYear1(2017, 11, 5)
    data['ServicePriceIndex_2017'] = GetDataYear1(2017, 15, 5)
    data['ConsumerPriceIndex_2017'] = GetDataYear1(2017, 18, 5)

    data['TotalIndex_2011'] = GetDataYear2(2011, 8, 5)
    data['ServicePriceIndex_2011'] = GetDataYear2(2011, 12, 5)
    data['ConsumerPriceIndex_2011'] = GetDataYear2(2011, 16, 5)

    data['TotalIndex_2012'] = GetDataYear2(2012, 8, 5)
    data['ServicePriceIndex_2012'] = GetDataYear2(2012, 12, 5)
    data['ConsumerPriceIndex_2012'] = GetDataYear2(2012, 16, 5)

    data['TotalIndex_2013'] = GetDataYear2(2013, 8, 5)
    data['ServicePriceIndex_2013'] = GetDataYear2(2013, 12, 5)
    data['ConsumerPriceIndex_2013'] = GetDataYear2(2013, 16, 5)

    data['TotalIndex_2014'] = GetDataYear2(2014, 8, 5)
    data['ServicePriceIndex_2014'] = GetDataYear2(2014, 12, 5)
    data['ConsumerPriceIndex_2014'] = GetDataYear2(2014, 16, 5)

    data['TotalIndex_2015'] = GetDataYear2(2015, 8, 5)
    data['ServicePriceIndex_2015'] = GetDataYear2(2015, 12, 5)
    data['ConsumerPriceIndex_2015'] = GetDataYear2(2015, 16, 5)

    TotalIndex = []
    ServicePriceIndex = []
    ConsumerPriceIndex = []
    for i in range(7):
        for j in range(12):
            TotalIndex.append(data['TotalIndex_201'+str(i+1)][j])
            ServicePriceIndex.append(data['ServicePriceIndex_201'+str(i+1)][j])
            ConsumerPriceIndex.append(
                data['ConsumerPriceIndex_201'+str(i+1)][j])

    for i in range(len(TotalIndex)):
        if i > 0:
            TotalIndex[i] = TotalIndex[i-1] * TotalIndex[i]/100
            ServicePriceIndex[i] = ServicePriceIndex[i-1] * \
                ServicePriceIndex[i]/100
            ConsumerPriceIndex[i] = ConsumerPriceIndex[i -
                                                       1] * ConsumerPriceIndex[i]/100

        else:
            TotalIndex[i] = TotalIndex[i]

    # print(TotalIndex)

    return data, TotalIndex, ServicePriceIndex, ConsumerPriceIndex


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
    data, TotalIndex, ServicePriceIndex, ConsumerPriceIndex = loaddata()

    print(TotalIndex)
    print(ServicePriceIndex)
    print(ConsumerPriceIndex)

    cov_between_total_and_ser = []
    for i in range(len(TotalIndex)-12):
        cov_between_total_and_ser.append(covariance(
            TotalIndex[i:i+12], ServicePriceIndex[i:i+12]))

    cov_between_total_and_con = []
    for i in range(len(TotalIndex)-12):
        cov_between_total_and_con.append(covariance(
            TotalIndex[i:i+12], ConsumerPriceIndex[i:i+12]))

    print(cov_between_total_and_ser)
    print(cov_between_total_and_con)

    plt.plot(cov_between_total_and_con, 'r')
    plt.plot(cov_between_total_and_ser, 'k')
    plt.show()



  
if __name__ == '__main__':
    main()

