"""
Created on Sat Jul 29 13:54:53 2023

@author: sandy
"""
import numpy as np
import math

#For rounding later on:
def find_mantissa(num):
    scale = int(round(np.log10(num),0))-3
    mantissa = int(round(num/10**scale,0))
    rounded_num = mantissa*10**scale
    rounded_num = round(rounded_num,3)
    return rounded_num

def report_million(num):
    if num >= 1000000:
        num = int(round(num/1000000))
        return f'{num} Million'
    if num < 1000000:
        return num

#Build data report
def build_data_list(data):
    data_list_0 = []
    data_list_1 = []
    for i in range(len(data)):
        data_list_0.append(data[i][0])
        data_list_1.append(data[i][1])
    return data_list_0,data_list_1
        
#Question 3:
def find_sell_day(data,sell_height):
    for i in range(len(data)):
        if data[i][1] >= sell_height:
            max_day = data[i][0]
            min_day = data[i-1][0]
            grow_max = data[i][1]
            grow_min = data[i-1][1]
            mom_at_3 = min_day+((max_day-min_day)/(grow_max-grow_min)*(sell_height-grow_min))
            return mom_at_3
    raise Exception("Did not reach 3 meters in observed duration. Expand duration or adjust expected height.")
    
def find_sell_moment(data,sell_day):
    extra = sell_day - int(sell_day)
    extra = 24*extra
    extra = round(extra,0)
    return extra

def find_pointwise_growth_rate(data, sell_day):
    for i in range(len(data)):
        if data[i][0] >= sell_day:
            if i == 0:
                raise Exception("Your plant is eligible to sell at point of purchase.")
            if i == len(data)-1:
                raise Exception("Your plant never grew tall enough to sell. Consider a longer duration of growth.")
            dh = data[i+1][1] - data[i-1][1]
            dt = data[i+1][0] - data[i-1][0]
            rate = dh/dt
            return rate
        
def find_growth_rates(data):
    growth_rates = []
    dh0 = data[1][1] - data[0][1]
    dt0 = data[1][0] - data[0][0]
    growth_rates.append(dh0/dt0)
    dh1 = data[2][1] - data[0][1]
    dt1 = data[2][0] - data[0][0]
    growth_rates.append(dh1/dt1)
    dh2 = data[4][1] - data[0][1]
    dt2 = data[4][0] - data[0][0]
    growth_rates.append(dh2/dt2)
    for i in range(3,len(data)-3):
        dh = data[i+3][1] - data[i-3][1]
        dt = data[i+3][0] - data[i-3][0]
        growth_rates.append(dh/dt)
    dhe = data[len(data)-1][1] - data[len(data)-5][1]
    dte = data[len(data)-1][0] - data[len(data)-5][0]
    growth_rates.append(dhe/dte)
    dhe = data[len(data)-1][1] - data[len(data)-3][1]
    dte = data[len(data)-1][0] - data[len(data)-3][0]
    growth_rates.append(dhe/dte)
    dhe = data[len(data)-1][1] - data[len(data)-2][1]
    dte = data[len(data)-1][0] - data[len(data)-2][0]
    growth_rates.append(dhe/dte)
    return growth_rates

def find_peak_growth(data,growth_rates):
    new_max_rate = 0
    for i in range(len(growth_rates)):
        max_rate = new_max_rate
        if growth_rates[i] > max_rate:
            max_rate = growth_rates[i]
            max_day = data[i][0]
        new_max_rate = max_rate
    return max_rate, max_day

def find_optimal_duration(data,cost,dollar_per_m,sell_day):
    t_max = len(data)
    profit = []
    max_day = 0
    new_max = 0
    for i in range(int(round(sell_day,0)),t_max):
        max_profit = new_max
        profit.append((data[i][1]*dollar_per_m-cost)/data[i][0])
        new_max = max(profit)
        if new_max > max_profit:
            max_day = data[i][0]
    return max_day,max_profit

#Bonus Question
def find_actual_profit(data,sell_day,dollar_per_m,cost):
    cycles = int(math.trunc(len(data)/int(round(sell_day,0))))
    max_profit = 0
    for i in range(1,cycles+1):
        days = int(math.trunc(len(data)/i))
        height = data[days-1][1]
        profit = height*dollar_per_m - cost
        if profit*i >= max_profit:
            max_profit = profit*i
            optimal_cycles = i
    return max_profit, optimal_cycles

#For building a histogram
def find_actual_profit_cycles(data,sell_day,dollar_per_m,cost,days):
    if sell_day > days:
        raise Exception("The requested duration is shorter than the eligible sell day. Choose a longer duration or different fertilizer.")
    cycles = int(math.trunc(len(data)/int(round(days,0))))
    height = data[int(round(days,0))-1][1]
    profit = cycles*(height*dollar_per_m - cost)
    return find_mantissa(profit)

def find_optimal_lists(data,optimal_cycles):
    x_list_optimal_0 = []
    x_list_optimal_1 = []
    for i in range(int(len(data)/optimal_cycles)):
        x_list_optimal_0.append(data[i][0])
        x_list_optimal_1.append(data[i][1])
    return x_list_optimal_0,x_list_optimal_1

def find_profit_data(data,sell_day,dollar_per_m,cost):
    num = len(data)
    nums = [num]
    profits = []
    for i in range(2,len(data)):
        if num/i < sell_day:
            break
        nums.append(num/i)
    for i in range(len(nums)):
        profits.append(2*find_actual_profit_cycles(data,sell_day,dollar_per_m,cost,nums[i]))
    return profits, nums

def find_optimal_average_growth(list_optimal_1):
    summands1 = sum(list_optimal_1)
    optimal_average_growth = summands1/len(list_optimal_1)
    return optimal_average_growth

def find_risk(cost,sell_day,optimal_cycles,num_plants,dollar_per_m,list_optimal_0,list_optimal_1):
    risks = []
    summands = np.zeros(optimal_cycles)
    for i in range(optimal_cycles):
        if i > 0:
            summands[i]=risks[-1]
        for j in range(len(list_optimal_1)):
            if list_optimal_0[j] < sell_day:
                risks.append(-cost*num_plants+summands[i])
            else:
                profit = dollar_per_m*list_optimal_1[j]*num_plants
                risks.append(profit-cost*num_plants+summands[i])
    return risks

def find_risks(cost,sell_day,optimal_cycles,list_optimal_0,list_optimal_1,dollar_per_m,num_plants):
    risks = []
    for j in range(optimal_cycles):
        for i in range(len(list_optimal_0)):
            if list_optimal_0[i] < sell_day:
                risks.append(cost*num_plants)
            if list_optimal_0[i] >= sell_day:
                profit = dollar_per_m*list_optimal_1[i]*num_plants
                risks.append(profit-cost*num_plants)
    return risks
