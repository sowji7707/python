import math

def cal_future_value(p,r,n):
    """function to calculate the final value amount
    for the given interest rate and number of years

    # FV = p * (1 + r)^n
    """
    print(f"principal:{p}, interest:{r}, years:{n}")
    final_value = round(p*math.pow(1+r, n), 2)
    return final_value

"""
FV = P * [(1 + r)^n - 1] / r
If you invest one lakh every year how much would it would be after specified number years
"""
# 
for n in range(1,11):
    print(cal_future_value(100000,0.07,n))

print(cal_future_value(100000,0.07,15))
