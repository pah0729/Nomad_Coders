def tax_calc(momey):
    return momey * 0.35

def pay_tax(tax):
    print('thank you for paying', tax)

pay_tax(tax_calc(1000))
print()


def make_juicee(fruit):
    return f'{fruit}+🥤'

def add_ice(juice):
    return f'{juice}+🧊'

def add_sugar(iced_juice):
    return f'{iced_juice}+🍬'

juice = make_juicee('🍎')
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice, '= 🧃')