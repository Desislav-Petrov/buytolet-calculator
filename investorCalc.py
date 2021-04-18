import math

MANAGEMENT_FEE_PERCENT = 10
TAX_FREE_AMOUNT = 1000
TAX_RATE_PERCENT = 40

def per_month_to_period(per_month, period):
  if period == "WEEK":
    return per_month / 4.0
  elif period == "MONTH":
    return per_month
  elif period == "YEAR":
    return per_month*12.0
  else:
    print("Unknown period:" + str(period));

def calc_management_fee(rent_pcm, period):
  fee_pcm = rent_pcm * (MANAGEMENT_FEE_PERCENT / 100.0)
  return per_month_to_period(fee_pcm, period)

def calc_mortgage(property_price, ltv, mortgage_ir, mortgage_term_years, period):
  mortgage_amount = property_price * (ltv/100.0)
  number_of_payments = mortgage_term_years * 12
  ir = mortgage_ir / 100.0
  payment = (mortgage_amount * (ir / 12.0) * math.pow(( 1 + ir / 12.0), number_of_payments)) / (math.pow(( 1 + ir / 12.0), number_of_payments) - 1)
  return round(per_month_to_period(payment, period), 2)

def calc_rent(rent_pcm, period):
  return per_month_to_period(rent_pcm, period)
    
def calc_profit_net(property_price, ltv, mortgage_ir, mortgage_term_years, rent_pcm, period):
    fees = calc_management_fee(rent_pcm, "YEAR")
    mortgage = calc_mortgage(property_price, ltv, mortgage_ir, mortgage_term_years, "YEAR")
    rent = calc_rent(rent_pcm, "YEAR")
    pre_tax_profit = rent - mortgage - fees
    
    if pre_tax_profit <= TAX_FREE_AMOUNT:
        return round(per_month_to_period(pre_tax_profit/12.0, period))
    else:
        taxable_profit = pre_tax_profit - TAX_FREE_AMOUNT
        net_profit = taxable_profit * (100 - TAX_RATE_PERCENT)/100.0 + TAX_FREE_AMOUNT
        return round(per_month_to_period(net_profit/12.0, period), 2)

def calc_yield(rent_pcm, property_price, period):
    monthly_yield  = float(rent_pcm) / property_price
    return round(per_month_to_period(monthly_yield, period)*100, 2)

