import random
from datetime import datetime, timedelta
from data.order import rent_days, scooter_colour
from faker import Faker

faker = Faker('ru_RU')

def generate_info_client():
    return {
        'name': faker.first_name(),
        'last_name': faker.last_name(),
        'address': faker.street_name(),
        'metro': random.choice(['Марьина роща', 'Планерная', 'Таганская']),
        'phone': f'89{random.randint(100000000, 999999999)}'
    }

def generate_about_scooter_rent():
    return {
        'rent_day': random.choice(rent_days),
        'colour': random.choice(scooter_colour)
    }

def generate_date_rent():
    current_date = datetime.now()
    next_date = current_date + timedelta(days=1)
    return next_date.strftime("%d.%m.%Y")
