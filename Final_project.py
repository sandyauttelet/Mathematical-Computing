"""
Created on Tue Jul 25 12:37:26 2023

@author: sandy
"""
import numpy as np
import pandas as pd
import Build_data_report as BDR
import Plot_data_figures as PDF


#User input business perameters
x_cost = 1.0
y_cost = 1.25
sell_height = 3
dollar_per_kg = 12
kg_per_m = 10
dollar_per_m = dollar_per_kg*kg_per_m
num_plants = 20000

#x_data = np.loadtxt("x_grow.csv", delimiter=",")
#y_data = np.loadtxt("y_grow.csv", delimiter=",")
x_data = pd.read_csv("C:/Users/sandy/OneDrive/Documents/Summer 2023/Computing - 300/Final/x_grow.csv", delimiter=",")
y_data = pd.read_csv("C:/Users/sandy/OneDrive/Documents/Summer 2023/Computing - 300/Final/y_grow.csv", delimiter=",")
x_data = np.array(x_data)
y_data = np.array(y_data)

x_data_list_0,x_data_list_1 = BDR.build_data_list(x_data)
y_data_list_0,y_data_list_1 = BDR.build_data_list(y_data)
            
sell_day_x = BDR.find_sell_day(x_data,sell_height)
sell_day_y = BDR.find_sell_day(y_data,sell_height)

print(sell_day_x,sell_day_y)
sell_mom_x = BDR.find_sell_moment(x_data,sell_day_x)
sell_mom_y = BDR.find_sell_moment(y_data,sell_day_y)



#Question 2:
        
x_growth_rate = BDR.find_pointwise_growth_rate(x_data, sell_day_x)
y_growth_rate = BDR.find_pointwise_growth_rate(y_data, sell_day_y)
x_growth_rates = BDR.find_growth_rates(x_data)
y_growth_rates = BDR.find_growth_rates(y_data)
x_max_rate, x_max_rate_day = BDR.find_peak_growth(x_data,x_growth_rates)
y_max_rate, y_max_rate_day = BDR.find_peak_growth(y_data,y_growth_rates)

x_optimal_cycle, x_max_profit_per_day = BDR.find_optimal_duration\
    (x_data,x_cost,dollar_per_m,sell_day_x)
y_optimal_cycle, y_max_profit_per_day = BDR.find_optimal_duration\
    (y_data,y_cost,dollar_per_m,sell_day_y)


profit_data_x, cycles_x = BDR.find_profit_data(x_data,sell_day_x,dollar_per_m,x_cost)
profit_data_y, cycles_y = BDR.find_profit_data(y_data,sell_day_y,dollar_per_m,y_cost)

x_max_profit, x_optimal_cycles = BDR.find_actual_profit(x_data, \
    sell_day_x, dollar_per_m, x_cost)
y_max_profit, y_optimal_cycles = BDR.find_actual_profit(y_data, \
    sell_day_y, dollar_per_m, y_cost)
    
x_list_optimal_0,x_list_optimal_1 = BDR.find_optimal_lists(x_data,x_optimal_cycles)
y_list_optimal_0,y_list_optimal_1 = BDR.find_optimal_lists(y_data,y_optimal_cycles)

x_total_profit = x_max_profit*num_plants
y_total_profit = y_max_profit*num_plants

if x_total_profit > y_total_profit:
    total_saved_money = round((x_total_profit - y_total_profit),2)
if y_total_profit > x_total_profit:
    total_saved_money = round((y_total_profit - x_total_profit),2)
if y_total_profit == x_total_profit:
    total_saved_money = 0
    
x_profit_data,x_cycles = BDR.find_profit_data(x_data,sell_day_x,dollar_per_m,x_cost)
y_profit_data,y_cycles = BDR.find_profit_data(y_data,sell_day_y,dollar_per_m,y_cost) 

x_optimal_average_growth = BDR.find_optimal_average_growth(x_list_optimal_1)
y_optimal_average_growth = BDR.find_optimal_average_growth(y_list_optimal_1)

x_risk = BDR.find_risk(x_cost,sell_day_x,x_optimal_cycles,num_plants,dollar_per_m,x_list_optimal_0,x_list_optimal_1)
y_risk = BDR.find_risk(y_cost,sell_day_y,y_optimal_cycles,num_plants,dollar_per_m,y_list_optimal_0,y_list_optimal_1)
x_risks = BDR.find_risks(x_cost,sell_day_x,x_optimal_cycles,x_list_optimal_0,x_list_optimal_1,dollar_per_m,num_plants)
print(x_risks)
print(len(x_risks))

y_risks = BDR.find_risks(y_cost,sell_day_y,y_optimal_cycles,y_list_optimal_0,y_list_optimal_1,dollar_per_m,num_plants)
report_x_profit = BDR.report_million(BDR.find_mantissa(x_total_profit))
report_y_profit = BDR.report_million(BDR.find_mantissa(y_total_profit))
report_total_profit = BDR.report_million(BDR.find_mantissa(total_saved_money))

#Plotting data report:

# #Plots curve fit for data
# PDF.plot_curve_fit_x(x_data_list_0,x_data_list_1)
# PDF.plot_curve_fit_y(y_data_list_0,y_data_list_1)

# #Plots data as line segment seperately
# PDF.plot_x_data(x_data_list_0,x_data_list_1)
# PDF.plot_y_data(y_data_list_0,y_data_list_1)

# #Plots both sets together
# PDF.plot_x_y_data(x_data_list_0,x_data_list_1,y_data_list_0,y_data_list_1)
# #Plots together with 3m mark
# PDF.plot_sell_day(x_data_list_0,x_data_list_1,y_data_list_0,y_data_list_1)

# #Plots growth rates by day
# PDF.plot_growth_rate(x_data_list_0,x_data_list_1,y_data_list_0,y_data_list_1,x_growth_rates,y_growth_rates)

# #Plots growth per cycle
# PDF.make_barchart_x(x_profit_data,x_cycles)
# PDF.make_barchart_y(y_profit_data,y_cycles)

# #Plots consistent growth cycles of optimal duration
# PDF.plot_cycle_growth_x(x_list_optimal_0,x_list_optimal_1,x_optimal_cycles,x_optimal_average_growth)
# PDF.plot_cycle_growth_y(y_list_optimal_0,y_list_optimal_1,y_optimal_cycles,y_optimal_average_growth)

# #Plotting Risk per Plant
# PDF.plot_risk_x(x_risk,x_data_list_0)
# PDF.plot_risk_y(y_risk,y_data_list_0)

PDF.plot_risks_x(x_risks,x_optimal_cycles,x_data_list_0)
PDF.plot_risks_y(y_risks,y_optimal_cycles,y_data_list_0)
PDF.plot_risks_x_and_y(x_risks,x_optimal_cycles,x_data_list_0,y_risks,y_optimal_cycles,y_data_list_0)

#Printing report set up for x and y grow brand fertilizer

#Prints sell day information
print(f'We can sell bamboo shoots grown with x fertilizer after \
{int(sell_day_x)} days and roughly {int(sell_mom_x)} hours after planting.')
print(f'\nWe can sell bamboo shoots grown with y fertilizer after \
{int(sell_day_y)} days and roughly {int(sell_mom_y)} hours after planting.')

#Prints groth rates
print(f'\n\nThe growth rate of bamboo grown with x fertilizer at \
point of sell is {BDR.find_mantissa(x_growth_rate)} meters per day.')
print(f'\nThe growth rate of bamboo grown with y fertilizer at \
point of sell is {BDR.find_mantissa(y_growth_rate)} meters per day.')

#Printing max rates and analysis of optimal cycles
print(f'\n\nFertilizer x results in a peak growth rate of {BDR.find_mantissa(x_max_rate)} meters per day on day {round(x_max_rate_day)}')
print(f'\nFertilizer y results in a peak growth rate of {BDR.find_mantissa(y_max_rate)} meters per day on day {round(y_max_rate_day)}.')

#Paragraph specific to this data and visual analysis. Not valid for new data.
print('\nIf you choose to grow with x fertilizer, your plants will \
grow faster in the beginning of a 60 day cycle, but the growth \
rate will begin to decline at about 26 days. After about 30 days, \
both sets will be growing at roughly the same rate. At this \
point, plants grown with y fertilizer will begin to grow faster. \
Both plant sets will come to the same average growth rate and \
thus same height at 53 days, after which y fertilizer grown \
plants have a faster average growth rate.')
 
#Prints optimal cycle days and max profit in that cycle
print(f'\n\nThe maximum profit per {BDR.find_mantissa(x_optimal_cycle)} days, the optimal cycle, per plant \
grown in x fertilizer will be {BDR.find_mantissa(x_max_profit_per_day*x_optimal_cycle)} dollars.')

print(f'\nThe maximum profit per {BDR.find_mantissa(y_optimal_cycle)} days, the optimal cycle, per plant \
grown in y fertilizer will be {BDR.find_mantissa(y_max_profit_per_day*y_optimal_cycle)} dollars.')

#Prints the optimal choice
if x_max_profit_per_day > y_max_profit_per_day:
    print("\nOptimal fertilizer choice is x because it yields more \
dollars per day and in the long run pays off.")
if y_max_profit_per_day > x_max_profit_per_day:
    print("\nOptimal fertilizer choice is y because it yields more \
dollars per day and in the long run pays off.")
if x_max_profit_per_day == y_max_profit_per_day:
    print("\nBoth fertilizers are equavalent in optimal profit.")
 
#Notes irrelevent cost
print('\nNote that the cost per plant is negligible because the profit is roughly one thousand times larger than the cost.')
 
#Prints final data analysis     
print(f'\n\nAfter {len(x_data)} days as {int(BDR.find_mantissa(x_optimal_cycles))} \
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
