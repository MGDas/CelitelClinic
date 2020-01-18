import asyncio
import requests

from doctor.models import Doctor, Specialization
from organization.models import Department

from doctor.parsers.GetDoctorsWithMainCode import main as doctor_with_main_code



def connect(url):
    response = requests.get(url)
    return response.json()

def get_special(spec_data):

    spec_id_list = []
    if spec_data:
        for code in spec_data:
            try:
                special = Specialization.objects.only('id').get(code=code)
                spec_id_list.append(special)
            except Specialization.DoesNotExist:
                continue


    return spec_id_list

def get_depart(depart_data):

    try:
        depart = Department.objects.get(code=depart_data)
    except Exception as e:
        depart = False

    return depart


def save_in_db(**data):

    update_fields = {
        'full_name': data['full_name'],
        'gender': data['gender'],
        'adult': data['adult'],
        'childish': data['childish'],
    }

    depart = get_depart(data['department_id'])
    special_list = get_special(data['specialization_id'])

    doctor, status = Doctor.objects.update_or_create(code=data['code'], defaults=update_fields)

    if depart:
        doctor.department.add(depart)

    if special_list:
        doctor.specialization.add(*special_list)

    if not status:
        print(f"{doctor}......ОБНОВЛЕНО!")
    else:
        print(f"{doctor}......СОЗДАНО!")


def main():

    url = 'https://celitel05.ru/json/GetDoctors.json'
    data = connect(url)

    count = 0
    for d in data:
        if not d['main_code']:
            save_in_db(**d)
            count += 1

    print("============================")
    print(f"Doctors saved. Count {count}.")
    print("============================")

    doctor_with_main_code(data)
