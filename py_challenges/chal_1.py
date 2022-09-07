"""
과제 1
"""
monthly_revenue = 5500000 # 수입
monthly_expenses = 2700000 # 지출
tax_credits = 0.01 # 세율

# 1. 연간 매출 계산
def get_yearly_revenue(revenue):
    return revenue * 12

# 2. 연간 비용 계산
def get_yearly_expenses(expenses):
    return expenses * 12

profit = get_yearly_revenue(monthly_revenue) - get_yearly_expenses(monthly_expenses) # 이익

# 3. 세금 계산
def get_tax_amount(tax):
    if tax >= 100000:
        tax = tax * 0.25
    else:
        tax = tax * 0.15
    return tax

tax_amount = get_tax_amount(profit) # 세금 금액

# 4. 세액 공제 적용
def apply_tax_credits(amount, credits):
    return amount * credits

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is : ${final_tax_amount}")