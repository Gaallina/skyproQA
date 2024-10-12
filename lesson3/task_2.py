from smartphone import Smartphone

catalog = []

smartphone1 = Smartphone(marka='Samsung', model='Galaxy A14', number='(+79..)')
smartphone2 = Smartphone(marka='Apple', model='iPhone 14', number='(+79..)')
smartphone3 = Smartphone(marka='Xiaomi', model='Redmi', number='(+79..)')
smartphone4 = Smartphone(marka='OPPO', model='Reno', number='(+79..)')
smartphone5 = Smartphone(marka='Huawei', model='Nova', number='(+79..)')

catalog = [smartphone1, smartphone2, smartphone3, smartphone4, smartphone5]

for phone in catalog:
    phone.print_info()
