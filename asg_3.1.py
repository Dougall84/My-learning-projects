hrs = input("Enter Hours:")
h = float(hrs)
if h <= 40:
    pay = h * 10.5
    print(pay)
else:
    ovrhrs = h - 40
    ovrpay = 10.5 * 1.5 * ovrhrs
    pay = (h - ovrhrs) * 10.5 + ovrpay
    print(pay)
