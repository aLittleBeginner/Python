# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 18:37:22 2021

@author: 10304
"""

#assumption: fixed annual salary, and fixed total house cost
# =============================================================================
# annual_salary = int(input("Enter your annual salary: "))
# monthly_salary = annual_salary / 12
# portion_saved =float(input("Enter the portion of salary for down payment you want to saved every month:"))
# total_cost = int(input("Enter the total cost of your dream house: "))
# portion_down_payment = 0.25
# down_payment = portion_down_payment * total_cost
# current_savings = 0
# r = 0.04
# months_count = 0
# 
# while current_savings < down_payment:
#     monthly_return = current_savings * r / 12
#     current_savings += (monthly_return + portion_saved * monthly_salary)
#     months_count += 1
# else:
#     print(months_count)
# =============================================================================
    


# assumption: saving, with a raise of your salary every 6 months
# =============================================================================
# annual_salary = int(input("Enter your annual salary: "))
# monthly_salary = annual_salary / 12
# portion_saved =float(input("Enter the portion of salary for down payment you want to saved every month: "))
# total_cost = int(input("Enter the total cost of your dream house: "))
# portion_down_payment = 0.25
# down_payment = portion_down_payment * total_cost
# current_savings = 0
# r = 0.04
# months_count = 0
# semi_annual_rise = float(input("Enter your semi annual raise: "))
# 
# while current_savings < down_payment:
#     months_count += 1
#     monthly_return = current_savings * r / 12
#     current_savings += (monthly_return + portion_saved * monthly_salary)
#     if months_count % 6 == 0:
#         monthly_salary += semi_annual_rise * monthly_salary
# else:
#     print(months_count)
# =============================================================================
    


#assumption: fixed time 36 months, calculate the monthly portion you need to save
annual_salary = int(input("Enter your annual salary: "))
def money_saved(salary, portion_saved):
    total_cost = 1000000
    portion_down_payment = 0.25
    down_payment = portion_down_payment * total_cost
    current_savings = 0
    r = 0.04
    months_count = 0
    semi_annual_rise = 0.07
    monthly_salary = annual_salary / 12
    while months_count < 36:
        months_count += 1
        monthly_return = current_savings * r / 12
        current_savings += monthly_return + portion_saved * monthly_salary
        if months_count % 6 == 0:
            monthly_salary += semi_annual_rise * monthly_salary
        if current_savings >= down_payment - 100:
            return True
    return False

left = 0
right = 10000
#判断portion_saved最大时是否满足36个月条件，如果不，三年不可能完成
if money_saved(annual_salary, right/10000) == False:
    print("It's not possible to pay the down payment in three years.")
#如果portion_saved最大时满足计划条件，使用二分算法寻找best portion_saved
else:
    bi_count = 0
    while left <= right:
        bi_count += 1
        mid = (left + right) // 2
        if money_saved(annual_salary, mid/10000):
            right = mid - 1
        else:
            left = mid + 1
    print("Best saving rate is :", '%.4f' % (left/10000))
    print("Steps in bisection search:", bi_count)
