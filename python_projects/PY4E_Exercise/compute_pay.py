hours = float(input("Enter Hours: "))
rate = float(input("Enetr Rate: "))

def computepay(hour, rates):
    if hours > 40:
        reg_pay = 40 * rate
        overtime = (hours - 40) * (rate * 1.5)
        total = reg_pay + overtime
        print(total)
    else:
        total = hours * rate
        print(total)

computepay(hours, rate)