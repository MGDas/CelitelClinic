import asyncio
import requests
from doctor.models import Doctor, Specialization
from organization.models import Department


def connect(url):
    response = requests.get(url)
    return response.json()

def special(special_code):

    special_list = []
    if special_code:
        for code in special_code:
            try:
                special = Specialization.objects.get(code=code)
                special_list.append(special)
            except Specialization.DoesNotExist:
                continue


    return special_list


async def save_in_db(code, main_code, full_name, adult, childish, gender, depart_code, special_code):

    try:
        department = Department.objects.get(code=depart_code)
    except Exception as e:
        department = False

    special_list = special(special_code)

    if main_code:
        try:
            doctor_with_main_code = Doctor.objects.get(main_code=main_code)
            if department and department not in doctor_with_main_code.department.all():
                doctor_with_main_code.department.add(department)

            if special_list:
                for spec in special_list:
                    if spec not in doctor_with_main_code.specialization.all():
                        doctor_with_main_code.specialization.add(spec)
            doctor_with_main_code.save()
            print(f"{doctor_with_main_code}......ОБНОВЛЕНО!")

        except Doctor.DoesNotExist:
            doctor = Doctor.objects.create(
                code=code,
                main_code=main_code,
                full_name=full_name,
                gender=gender,
                adult=adult,
                childish=childish,
            )
            if special_list:
                doctor.specialization.add(*special_list)
            if department:
                doctor.department.add(department)

            doctor.save()
            print(f"{doctor}......СОЗДАНО!")


    else:
        doctor, status = Doctor.objects.update_or_create(
            code=code,
            defaults={
                'main_code': main_code if main_code else '-----',
                'full_name': full_name,
                'gender': gender if gender else 'н',
                'childish': childish,
                'adult': adult
                }
        )
        if department:
            doctor.department.add(department)

        if special_list:
            doctor.specialization.add(*special_list)

        if not status:
            print(f"{doctor}......ОБНОВЛЕНО!")
        else:
            print(f"{doctor}......СОЗДАНО!")

async def main():

    url = 'https://celitel05.ru/json/GetDoctors.json'
    data = connect(url)

    tasks = []
    for d in data:
        task = asyncio.create_task(
            save_in_db(
                d['code'],
                d['main_code'],
                d['full_name'],
                d['adult'],
                d['childish'],
                d['gender'],
                d['department_id'],
                d['specialization_id']
                )
            )
        tasks.append(task)

    await asyncio.gather(*tasks)
