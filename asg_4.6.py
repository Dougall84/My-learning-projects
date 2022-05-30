def computepay(h, r):
    if h <= 40:
    	pay = h * r
    	return pay
    else:
    	ovrhrs = h - 40
    	ovrpay = r * 1.5 * ovrhrs
    	pay = (h - ovrhrs) * r + ovrpay
    return pay

hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input('Enter Rate:')
rate = float(rate)
p = computepay(hrs, rate)
print("Pay", p)
