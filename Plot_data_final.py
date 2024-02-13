"""
Created on Sat Jul 29 13:49:56 2023

@author: sandy
"""
import numpy as np
import matplotlib.pyplot as plt

#Functions made for curve fit.
#Will need to change for different data.
#constants = sc.optimize.curve_fit(f_y,y_data_list_0,y_data_list_1)
    
def f_y(t,x0,x1,x2,x3):
    f = x0/(1+np.exp(-x1*t+x2))+x3
    return f

def f_x(t,x0,x1,x2,x3,x4,x5,x6,x7,x8):
    f = x0*t**2 + x1*t**3 + x2*t**4 + x3*t + x4 + x5*t**5 + x6*t**6 + x7*t**7 + x8*t**8
    return f

def plot_curve_fit_x(x_data_list_0,x_data_list_1):
    tx = np.linspace(min(x_data_list_0),max(x_data_list_0),1000)
    fig1 = plt.figure(1)
    fig1.suptitle("Measured and Fit Data for x-grow", fontsize=16)
    plt.plot(x_data_list_0,x_data_list_1)
    plt.xlabel('Days of Growth')
    plt.ylabel('Height (m)')
    plt.scatter(x_data_list_0,x_data_list_1,color='red')
    plt.plot(tx,f_x(tx,-6.51968382e-02,  1.05973801e-02, -6.73468343e-04,  2.59080135e-01,
            3.55047909e-01,  2.16533793e-05, -3.77703269e-07,  3.41898145e-09,
           -1.26162606e-11))
    labels = ('Measurements','Polynomial Curve Fit')
    plt.legend(labels)
    
def plot_curve_fit_y(y_data_list_0,y_data_list_1):
    ty = np.linspace(min(y_data_list_0),max(y_data_list_0),1000)
    fig2= plt.figure(2)
    fig2.suptitle("Measured and Fit Data for y-grow", fontsize=16)
    plt.xlabel('Days of Growth')
    plt.ylabel('Height (m)')
    plt.scatter(y_data_list_0,y_data_list_1,color='red')
    plt.plot(ty,f_y(ty,10.70286051,  0.09901738,  3.46901829,  0.09466854))
    labels = ('Measurements','Logistic Curve Fit')
    plt.legend(labels)
    
#Plot of just x data
def plot_x_data(x_data_list_0,x_data_list_1):    
    fig3 = plt.figure(3)
    fig3.suptitle("Growth with Fertilizer x", fontsize=16)
    plt.plot(x_data_list_0,x_data_list_1)
    plt.xlabel('Days of Growth')
    plt.ylabel('Height (m)')

#Plot of just y data
def plot_y_data(y_data_list_0,y_data_list_1):
    fig4 = plt.figure(4)
    fig4.suptitle("Growth with Fertilizer y", fontsize=16)
    plt.plot(y_data_list_0,y_data_list_1)
    plt.xlabel('Days of Growth')
    plt.ylabel('Height (m)')
    
#Plot of x and y data
def plot_x_y_data(x_data_list_0,x_data_list_1,y_data_list_0,y_data_list_1):
    fig5 = plt.figure(5)
    fig5.suptitle("Growth with Fertilizer x and y", fontsize=16)
    plt.plot(x_data_list_0,x_data_list_1)
    plt.plot(y_data_list_0,y_data_list_1)
    plt.xlabel('Days of Growth')
    plt.ylabel('Height (m)')
    labels = ('x Fertilizer','y Fertilizer')
    plt.legend(labels)
    
#Plot marks where 3m exists to find when we can sell
def plot_sell_day(x_data_list_0,x_data_list_1,y_data_list_0,y_data_list_1):
    fig6 = plt.figure(6)
    fig6.suptitle("When We Can Sell", fontsize=16)
    plt.plot(x_data_list_0,x_data_list_1)
    plt.plot(y_data_list_0,y_data_list_1)
    plt.axhline(3,linestyle='--')
    plt.xlabel('Days of Growth')
    plt.ylabel('Height (m)')
    labels = ('x Fertilizer','y Fertilizer','3m Achievement')
    plt.legend(labels)
    
#Plot Growth Rate
def plot_growth_rate(x_data_list_0,x_data_list_1,y_data_list_0,y_data_list_1,x_growth_rates,y_growth_rates):
    fig7 = plt.figure(7)
    fig7.suptitle("Growth Rates", fontsize=16)
    plt.plot(x_data_list_0,x_growth_rates)
    plt.plot(y_data_list_0,y_growth_rates)
    plt.xlabel('Days of Growth')
    plt.ylabel('Rate of Growth')
    labels = ('x Fertilizer','y Fertilizer')
    plt.legend(labels)

def make_barchart_x(profit_data,cycles):
    fig8 = plt.figure(8)
    fig8.suptitle("60-Day Profit for Each Cycle Duration in x Fertilizer", fontsize=16)
    plt.bar(cycles,profit_data)
    plt.xlabel('Cycle Duration in Days')
    plt.ylabel('Profit per Plant in Ten Thousand Dollars')
    
def make_barchart_y(profit_data,cycles):
    fig9 = plt.figure(9)
    fig9.suptitle("60-Day Profit for Each Cycle Duration in y Fertilizer", fontsize=16)
    plt.bar(cycles,profit_data)
    plt.xlabel('Cycle Duration in Days')
    plt.ylabel('Profit per Plant in Ten Thousand Dollars')
    
def plot_cycle_growth_x(x_list_optimal_0,x_list_optimal_1,x_optimal_cycles,x_optimal_average_growth):
    fig10 = plt.figure(10)
    fig10.suptitle(f'{x_optimal_cycles} Consistent {len(x_list_optimal_0)}-Day Growth Cycle(s) in x Fertilizer', fontsize=16)
    for i in range(int(x_optimal_cycles)):
        days = x_list_optimal_0 + (i)*len(x_list_optimal_0)*np.ones(len(x_list_optimal_0))
        plt.plot(days,x_list_optimal_1)
    plt.axhline(x_optimal_average_growth,linestyle='--')
    labels = ('x Fertilizer','Average Growth Rate')
    plt.legend(labels)
    plt.xlabel('Days of growth')
    plt.ylabel('Height (m)')
    
def plot_cycle_growth_y(y_list_optimal_0,y_list_optimal_1,y_optimal_cycles,y_optimal_average_growth):
    fig11 = plt.figure(11)
    fig11.suptitle(f'{y_optimal_cycles} Consistent {len(y_list_optimal_0)}-Day Growth Cycle(s) in y Fertilizer', fontsize=16)
    for i in range(int(y_optimal_cycles)):
        days = y_list_optimal_0 + (i)*len(y_list_optimal_0)*np.ones(len(y_list_optimal_0))
        plt.plot(days,y_list_optimal_1)
    plt.axhline(y_optimal_average_growth,linestyle='--')
    labels = ('y Fertilizer','Average Growth Rate')
    plt.legend(labels)
    plt.xlabel('Days of growth')
    plt.ylabel('Height (m)')
    
def plot_risk_x(x_risks,x_list_0):
    fig12 = plt.figure(12)
    fig12.suptitle('Risk per Plant of x fertilizer')
    risks = []
    for i in range(len(x_risks)):
        risks.append(x_risks[i]/100000)
    plt.plot(x_list_0,risks)
    plt.xlabel('Days')
    plt.ylabel('Risk per Plant per One-Hundred Thousand Dollars')
    
def plot_risk_y(y_risks,y_list_0):
    fig13 = plt.figure(13)
    fig13.suptitle('Risk per Plant of x fertilizer')
    risks = []
    for i in range(len(y_risks)):
        risks.append(y_risks[i]/100000)
    plt.plot(y_list_0,risks)
    plt.xlabel('Days')
    plt.ylabel('Risk per Plant per One-Hundred Thousand Dollars')
    
def plot_risks_x(x_risks,x_optimal_cycles,x_list_0):
    fig14 = plt.figure(14)
    #fig14.suptitle('Risk per Plant of x fertilizer')
    risks = []
    for j in range(len(x_risks)):
        risks.append(x_risks[j])
    plt.plot(x_list_0,risks)
    plt.xlabel('Days')
    plt.ylabel('Risk per Plant in Dollars')
    
def plot_risks_y(y_risks,y_optimal_cycles,y_list_0):
    fig15 = plt.figure(15)
    #fig15.suptitle('Risk per Plant of y fertilizer')
    risks = []
    for j in range(len(y_risks)):
        risks.append(y_risks[j])
    plt.plot(y_list_0,risks)
    plt.xlabel('Days')
    plt.ylabel('Risk per Plant in Dollars')
    
def plot_risks_x_and_y(x_risks,x_optimal_cycles,x_list_0,y_risks,y_optimal_cycles,y_list_0):
    fig16 = plt.figure(16)
    #fig16.suptitle('Risk per Plant of x and y fertilizer')
    x_risks_changed = []
    for j in range(len(x_risks)):
        x_risks_changed.append(x_risks[j])
    y_risks_changed = []
    for j in range(len(y_risks)):
        y_risks_changed.append(y_risks[j])
    plt.plot(x_list_0,x_risks_changed)
    plt.plot(y_list_0,y_risks_changed)
    labels = ('x Fertilizer','y Fertilizer')
    plt.legend(labels)
    plt.xlabel('Days')
    plt.ylabel('Risk per Plant in Dollars')
