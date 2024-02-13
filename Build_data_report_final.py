"""
Created on Sat Jul 29 13:54:53 2023

@author: sandy
"""
import numpy as np
import math

#For rounding later on:
def find_mantissa(num):
    """
    Finds optimal rounded values for report printing.

    Parameters
    ----------
    num : float
        number you are trying to round.

    Returns
    -------
    rounded_num : float
        rounded number to three decimal places.

    """
    scale = int(round(np.log10(num),0))-3
    mantissa = int(round(num/10**scale,0))
    rounded_num = mantissa*10**scale
    rounded_num = round(rounded_num,3)
    return rounded_num

def report_million(num):
    """
    Rounds numbers for ploting to reflect per million.

    Parameters
    ----------
    num : float
        number you are trying to round.

    Returns
    -------
    float
        number per million.

    """
    if num >= 1000000:
        num = int(round(num/1000000))
        return f'{num} Million'
    if num < 1000000:
        return num

#Build data report
def build_data_list(data):
    """
    Builds a list from a set of numbers.

    Parameters
    ----------
    data : array of array of floats
        arrays of data generated from data file with two columns.

    Returns
    -------
    data_list_0 : list of floats
        list of data from first column of data file.
    data_list_1 : list of floats
        list of data from second column of data file.

    """
    data_list_0 = []
    data_list_1 = []
    for i in range(len(data)):
        data_list_0.append(data[i][0])
        data_list_1.append(data[i][1])
    return data_list_0,data_list_1
        
#Question 3:
def find_sell_day(data,sell_height):
    """
    Finds day you can sell plants per input specifications.

    Parameters
    ----------
    data : array of array of floats
        arrays of data generated from data file with two columns.
    sell_height : float
        input parameter by business owner, the height we can sell plants at.

    Raises
    ------
    Exception
        Plant never grew tall enough to sell.

    Returns
    -------
    mom_at_3 : float
        moment plant grew tall enough to sell.

    """
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
    """
    Finds moment we can sell plants discretizing data given in days to data given in minutes.

    Parameters
    ----------
    data : array of array of floats
        arrays of data generated from data file with two columns.
    sell_day : float
        day that plant grows tall enough to sell.

    Returns
    -------
    extra : float
        extra part of the day that should be accounted for to find moment in day we can sell plant.

    """
    extra = sell_day - int(sell_day)
    extra = 24*extra
    extra = round(extra,0)
    return extra

def find_pointwise_growth_rate(data, sell_day):
    """
    Finds rate of growth in meters of growth per day.

    Parameters
    ----------
    data : array of array of floats
        arrays of data generated from data file with two columns.
    sell_day : float
        day that plant grows tall enough to sell.

    Raises
    ------
    Exception
        plant was bought tall enough to sell.

    Returns
    -------
    rate : float
        rate of growth in meters per day.

    """
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
    """
    Finds rate of growth for plant at each day.

    Parameters
    ----------
    data : array of array of floats
        arrays of data generated from data file with two columns.

    Returns
    -------
    growth_rates : list of floats
        rates of growth in meters per day for each point in the data.

    """
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
    """
    Finds where plant will reach its peak height.

    Parameters
    ----------
    data : array of array of floats
        arrays of data generated from data file with two columns.
    growth_rates : list of floats
        rates of growth in meters per day for each point in the data.

    Returns
    -------
    max_rate : float
        max rate of growth for plant.
    max_day : float
        day that max growth rate is achieved for the plant.

    """
    new_max_rate = 0
    for i in range(len(growth_rates)):
        max_rate = new_max_rate
        if growth_rates[i] > max_rate:
            max_rate = growth_rates[i]
            max_day = data[i][0]
        new_max_rate = max_rate
    return max_rate, max_day

def find_optimal_duration(data,cost,dollar_per_m,sell_day):
    """
    Finds optimal duration to keep plant growing.

    Parameters
    ----------
    data : array of array of floats
        arrays of data generated from data file with two columns.
    cost : float
        cost of initial plant.
    dollar_per_m : float
        dollar earned per meter of plant growth.
    sell_day : float
        day you can sell plant for which it has reached initial parameter of growth.

    Returns
    -------
    max_day : float
        optimal day to cut plant for max profit to be obtained.
    max_profit : float
        maximal profit earned per plant in dollars.

    """
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
    """
    Finds actual profit for which you can earn if utilizing optimal calculations.

    Parameters
    ----------
    data : array of array of floats
        arrays of data generated from data file with two columns.
    sell_day : float
        day you can sell plant for which it has reached initial parameter of growth.
    dollar_per_m : float
        dollar earned per meter of plant growth.
    cost : float
        cost of initial plant.

    Returns
    -------
    max_profit : float
        maximal profit earned per plant in dollars.
    optimal_cycles : list of floats
        list of optimal cycles you should run to maximize profit.

    """
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
    """
    Finds actual profit aquired in dollars.

    Parameters
    ----------
    data : array of array of floats
        arrays of data generated from data file with two columns.
    sell_day : float
        day you can sell plant for which it has reached initial parameter of growth.
    dollar_per_m : float
        dollar earned per meter of plant growth.
    cost : float
        cost of initial plant.
    days : float
        days of growth found from optimal cycles calculation.

    Raises
    ------
    Exception
        plant is not tall enough to sell.

    Returns
    -------
    float
        rounded profit.

    """
    if sell_day > days:
        raise Exception("The requested duration is shorter than the eligible sell day. Choose a longer duration or different fertilizer.")
    cycles = int(math.trunc(len(data)/int(round(days,0))))
    height = data[int(round(days,0))-1][1]
    profit = cycles*(height*dollar_per_m - cost)
    return find_mantissa(profit)

def find_optimal_lists(data,optimal_cycles):
    """
    Finds list of optimal cycles from optimal cycles.

    Parameters
    ----------
    data : array of array of floats
        arrays of data generated from data file with two columns.
    optimal_cycles : list of floats
        list of optimal cycles you should run to maximize profit.

    Returns
    -------
    x_list_optimal_0 : list of floats
        list of days of optimal growth for plant data.
        DESCRIPTION.
    x_list_optimal_1 : list of floats
        list of height of optimal growth for plant data.

    """
    x_list_optimal_0 = []
    x_list_optimal_1 = []
    for i in range(int(len(data)/optimal_cycles)):
        x_list_optimal_0.append(data[i][0])
        x_list_optimal_1.append(data[i][1])
    return x_list_optimal_0,x_list_optimal_1

def find_profit_data(data,sell_day,dollar_per_m,cost):
    """
    Builds list of profits utilizing optimal calculations.

    Parameters
    ----------
    data : array of array of floats
        arrays of data generated from data file with two columns.
    sell_day : float
        day you can sell plant for which it has reached initial parameter of growth.
    dollar_per_m : float
        dollar earned per meter of plant growth.
    cost : float
        cost of initial plant.

    Returns
    -------
    profits : list of floats
        profits made for each day.
    nums : list of ints
        number of days we are growing plants.

    """
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
    """
    Finds average growth of each plant utilizing optimal growth data.

    Parameters
    ----------
    list_optimal_1 : list of floats
        list of height of optimal growth for plant data.

    Returns
    -------
    optimal_average_growth : float
        average growth from utilizing optimal cycle in meters.

    """
    summands1 = sum(list_optimal_1)
    optimal_average_growth = summands1/len(list_optimal_1)
    return optimal_average_growth

def find_risk(cost,sell_day,optimal_cycles,num_plants,dollar_per_m,list_optimal_0,list_optimal_1):
    """
    Calculates risk associated with growing these plants.

    Parameters
    ----------
    cost : float
        cost of initial plant.
    sell_day : float
        day you can sell plant for which it has reached initial parameter of growth.
    optimal_cycles : list of floats
        list of optimal cycles you should run to maximize profit.
    num_plants : int
        number of plants grown at one time.
    dollar_per_m : float
        dollar earned per meter of plant growth.
    list_optimal_0 : list of floats
        list of days of optimal growth for plant data.
    list_optimal_1 : list of floats
        list of height of optimal growth for plant data.

    Returns
    -------
    risks : list of floats
        financial risk associated with each day of growth in dollars.

    """
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
    """
    Calculates risks associated with growing these plants.

    Parameters
    ----------
    cost : float
        cost of initial plant.
    sell_day : float
        day you can sell plant for which it has reached initial parameter of growth.
    optimal_cycles : list of floats
        list of optimal cycles you should run to maximize profit.
    list_optimal_0 : list of floats
        list of days of optimal growth for plant data.
    list_optimal_1 : list of floats
        list of height of optimal growth for plant data.
    dollar_per_m : float
        dollar earned per meter of plant growth.
    num_plants : int
        number of plants grown at one time.

    Returns
    -------
    risks : list of floats
        financial risk associated with each day of growth in dollars.

    """
    risks = []
    for j in range(optimal_cycles):
        for i in range(len(list_optimal_0)):
            if list_optimal_0[i] < sell_day:
                risks.append(cost*num_plants)
            if list_optimal_0[i] >= sell_day:
                profit = dollar_per_m*list_optimal_1[i]*num_plants
                risks.append(profit-cost*num_plants)
    return risks
