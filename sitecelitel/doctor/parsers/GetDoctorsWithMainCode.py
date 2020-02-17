import requests

from django.core.exceptions import ObjectDoesNotExist

from doctor.models import Doctor
from organization.models import Department

def connect(url):
    response = requests.get(url)
    return response.json()


def check_doctor(main_code):

    try:
        doctor = Doctor.objects.only("id").get(code=main_code)
    except Doctor.DoesNotExist:
        doctor = False

    return doctor


def check_depart(depart_id):

    try:
        depart = Department.objects.only("id").get(code=depart_id)
    except Department.DoesNotExist:
        depart = False

    return depart


def merge_doctor_data(**data):

    doctor = check_doctor(data['main_code'])
    depart = check_depart(data['department_id'])

    if doctor and depart:
        doctor.department.add(depart)
        print(doctor.full_name)
        return True


def main(data):

    count = 0

    for d in data:
        if d['main_code']:
            merge = merge_doctor_data(**d)
            if merge:
                count += 1

    print("============================")
    print(f"Doctors merged. Count {count}.")
    print("============================")
