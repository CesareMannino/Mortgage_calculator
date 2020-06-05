# mortgage.py
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = 1000
extra_month_start = 0
extra_month_finish = 12

while principal > 0:
    month = month + 1
    principal = (principal * (1+rate/12)) - payment
    total_paid = total_paid + payment
    
    if month >= extra_month_start and month <= extra_month_finish:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    elif principal <= 0:
        total_paid = total_paid + (-principal)
        principal = principal + 1973
    



#print(month)


print ('{}'.format('Total months :'),month, '{} $'.format('Total paid :'),round(total_paid,2), '{}'.format('Remaining to be paid: '),round(principal))