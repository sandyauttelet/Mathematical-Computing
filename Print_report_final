"""
Created on Sat Jul 29 14:14:19 2023

@author: sandy
"""

import Build_data_report as BDR

def print_sell_day(sell_day_x,sell_mom_x,sell_day_y,sell_mom_y):
    """
    Prints optimal sell days and sell moments for both x-plant and y-plant data.

    Parameters
    ----------
    sell_day_x : float
        optimal day to sell x-plant.
    sell_mom_x : float
        optimal moment to sell x-plant.
    sell_day_y : float
        optimal day to sell y-plant.
    sell_mom_y : float
        optimal moment to sell y-plant.

    Returns
    -------
    None.

    """
    print(f'Can sell bamboo shoots grown with x fertilizer after \
    {int(sell_day_x)} days at roughly {sell_mom_x}.')
    print(f'Can sell bamboo shoots grown with y fertilizer after \
    {int(sell_day_y)} days at roughly {sell_mom_y}.')

def print_growth_rate(x_growth_rate,y_growth_rate):
    """
    Prints growth rates for both x-plant and y-plant data.

    Parameters
    ----------
    x_growth_rate : float
        growth rate of x-plant in meters per day.
    y_growth_rate : float
        growth rate of x-plant in meters per day.

    Returns
    -------
    None.

    """
    print(f'\nThe growth rate of bamboo grown with x fertilizer at \
    point of sell is {BDR.find_mantissa(x_growth_rate)} meters per day.')
    
    print(f'\nThe growth rate of bamboo grown with y fertilizer at \
    point of sell is {BDR.find_mantissa(y_growth_rate)} meters per day.')

#Question 1:
def print_rate_trend(x_max_rate,y_max_rate,x_max_rate_day,y_max_rate_day):
    """
    Prints trend of growth rates for both x-plant and y-plant data.

    Parameters
    ----------
    x_max_rate : flaot
        max growth rate of x-plant in meters per day.
    y_max_rate : flaot
        max growth rate of y-plant in meters per day.
    x_max_rate_day : float
        day where max growth rate for x-plant is hit.
    y_max_rate_day : float
        day where max growth rate for y-plant is hit.

    Returns
    -------
    None.

    """
    print(f'Fertilizer x results in a peak growth rate of {BDR.find_mantissa(x_max_rate)} meters per day on day {round(x_max_rate_day)} and \
    fertilizer y results in a peak growth rate of {BDR.find_mantissa(y_max_rate)} meters per day on day {round(y_max_rate_day)}.')
    print('\nIf you choose to grow with x fertilizer, your plants will \
    grow faster in the beginning of a 60 day cycle, but the growth \
    rate will begin to decline at about 26 days. After about 30 days, \
    both sets will be growing at roughly the same rate. At this \
    point, plants grown with y fertilizer will begin to grow faster. \
    Both plant sets will come to the same average growth rate and \
    thus same height at 53 days, after which y fertilizer grown \
    plants have a faster average growth rate.')
 
def print_optimal_profit(x_optimal_cycle,y_optimal_cycle,x_max_profit_per_day,y_max_profit_per_day):
    """
    Prints optimal profit made with each optimal cycle, maximized profit per day for both x-plant and y-plant data.

    Parameters
    ----------
    x_optimal_cycle : float
        optimal cycle for x-plant data in days.
    y_optimal_cycle : float
        optimal cycle for y-plant data in days.
    x_max_profit_per_day : float
        max profit made per day for x-plant in dollars. 
    y_max_profit_per_day : float
        max profit made per day for y-plant in dollars. 

    Returns
    -------
    None.

    """
    print(f'\nThe maximum profit per {x_optimal_cycle} days, the optimal cycle, per plant \
    grown in x fertilizer will be {BDR.find_mantissa(x_max_profit_per_day*x_optimal_cycle)} dollars.')
    
    #Question 4
    print(f'\nThe maximum profit per {round(y_optimal_cycle,2)} \
    days, the optimal cycle, per plant grown in y fertilizer will be \
    {BDR.find_mantissa(y_max_profit_per_day*y_optimal_cycle)} dollars.')
    if x_max_profit_per_day > y_max_profit_per_day:
        print("\nOptimal fertilizer choice is x because it yields more \
    dollars per day and in the long run pays off.")
    if y_max_profit_per_day > x_max_profit_per_day:
        print("\nOptimal fertilizer choice is y because it yields more \
    dollars per day and in the long run pays off.")
    if x_max_profit_per_day == y_max_profit_per_day:
        print("\nBoth fertilizers are equavalent in optimal profit.")
    
    print('Note that the cost per plant is negligible because the profit is roughly one thousand times larger than the cost.')

def print_final_data(x_data,y_data,x_optimal_cycles,y_optimal_cycles,report_x_profit,report_y_profit,x_max_profit,y_max_profit,num_plants,report_total_profit):       
    """
    Prints final information for report for both x-plant and y-plant data.

    Parameters
    ----------
    x_data : list of list of floats
        original x-plant data.
    y_data : list of list of floats
        original x-plant data.
    x_optimal_cycles : list of floats
        list of optimal cycles for x-plant data.
    y_optimal_cycles : list of floats
        list of optimal cycles for y-plant data.
    report_x_profit : float
        final profit made from x-plant in dollars.
    report_y_profit : float
        final profit made from y-plant in dollars.
    x_max_profit : float
        final maximized profit made from x-plant in dollars.
    y_max_profit : float
        final maxmimized profit made from y-plant in dollars.
    num_plants : int
        total number of plants grown.
    report_total_profit : float
        total profit for both plants utilizing optimal cycles in dollars.

    Returns
    -------
    None.

    """
    print(f'\nAfter {len(x_data)} days as {int(BDR.find_mantissa(x_optimal_cycles))} \
    cycle(s) of {int(BDR.find_mantissa(len(x_data)/x_optimal_cycles))} days in \
    fertilizer x, the profit per plant is {BDR.find_mantissa(x_max_profit)}. \
    Therefore, the total profit for all {num_plants} plants at a time \
    is {report_x_profit}.')
    
    print(f'\nAfter {len(y_data)} days as {int(BDR.find_mantissa(y_optimal_cycles))} \
    cycle(s) of {int(BDR.find_mantissa(len(y_data)/y_optimal_cycles))} days in \
    fertilizer y, the profit per plant is {BDR.find_mantissa(y_max_profit)}. \
    Therefore, the total profit for all {num_plants} plants at a time \
    is {report_y_profit}.')
    
    print(f'\nFinally, the total profit saved from using the optimal \
    fertilizer is {report_total_profit}')
