from address import Address
from mailing import Mailing

address_to = Address(index=111111, town='Город 1', street='Улица 1', house='Дом 1', flat='Квартира 1')
address_from = Address(index=222222, town='Город 2', street='Улица 2', house='Дом 2', flat='Квартира 2')

mailing = Mailing(to_address=address_to, from_address=address_from, cost=1000, track='147852369')


print(f'Отправление {mailing.track} из {mailing.from_addres.index}, {mailing.from_addres.town}, '
      f'{mailing.from_addres.street}, {mailing.from_addres.house}, - {mailing.from_addres.flat}, '
      f'в {mailing.to_address.index}, {mailing.to_address.town}, {mailing.to_address.street}, '
      f'{mailing.to_address.house}, - {mailing.to_address.flat}. Стоимость {mailing.cost} рублей.')
