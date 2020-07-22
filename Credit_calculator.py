import math
import argparse
import sys

parser = argparse.ArgumentParser(description='Credit Calculator')

parser.add_argument('--type', type=str)
parser.add_argument('--payment', type=int)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)

args = parser.parse_args()

if args.type == 'diff' and args.principal is not None and args.periods is not None and args.interest is not None:
    
    i = args.interest / (12 * 100)
    differentiated_payments = []
    
    for m in range(1, args.periods + 1):
        
        d = math.ceil((args.principal / args.periods) + i * (args.principal - args.principal * (m - 1) / args.periods))
        
        differentiated_payments.append(d)
        
        print("Month {0}: paid out {1}".format(m, d))
    
    Overpayment = int(sum(differentiated_payments) - args.principal)
    
    print()
    print("Overpayment = {0}".format(Overpayment))

elif args.type == 'annuity' and args.principal is not None and args.periods is not None and args.interest is not None:
    
    i = args.interest / (12 * 100)
    
    annuity_payment = math.ceil(args.principal * (i * math.pow(1 + i, args.periods) / (math.pow(1 + i, args.periods) - 1)))
    
    Overpayment = int(annuity_payment * args.periods - args.principal)
    
    print("Your annuity payment = {0}!".format(annuity_payment))
    print("Overpayment = {0}".format(Overpayment))

elif args.type == 'diff' and args.principal is not None and args.payment is not None and args.periods is None and args.interest is None:
    
    print('Incorrect parameters')

elif args.type == 'annuity' and args.payment is not None and args.periods is not None and args.interest is not None:
    
    i = args.interest / (12 * 100)
    
    credit_principal = math.floor(args.payment / (i * math.pow(1 + i, args.periods) / (math.pow(1 + i, args.periods) - 1)))
    
    Overpayment = int(args.payment * args.periods - credit_principal)
    
    print("Your credit principal = {0}!".format(credit_principal))
    print("Overpayment = {0}".format(Overpayment))

elif args.type == 'annuity' and args.principal is not None and args.payment is not None and args.interest is not None:
    
    i = args.interest / (12 * 100)
    
    period_per_month = math.log((args.payment / (args.payment - i * args.principal)), (1 + i))
    
    period_per_month = math.ceil(period_per_month)
    
    over = args.payment * period_per_month - args.principal
    
    print(f'You need {period_per_month // 12} years to repay this credit!')
    print(f'Overpayment = {over}')

else:
    print('Incorrect parameters')
