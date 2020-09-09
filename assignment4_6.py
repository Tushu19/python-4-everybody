def computepay(hrs, rop):
    if hrs > 40:
        othrs = hrs - 40
        otrop = rop * 1.5
        gp = 40 * rop
        otgp = othrs * otrop
        totgp = gp + otgp
    else:
        totgp = hrs * rop
        return()
    print("Pay",totgp)



hours = float(input("Enter Hours:"))
rateofpay = float(input("Enter rate of pay:"))
computepay(hours,rateofpay)
