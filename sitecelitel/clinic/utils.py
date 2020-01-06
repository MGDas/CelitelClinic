from service.models import ServiceGroup

def get_service_group_to_alphabet():

    alphabet = [i.upper() for i in 'абвгдеёжзиклмнопрстуфхцчшщэюя']
    service_group = {}
    for alph in alphabet:
        try:
            sg = ServiceGroup.pub_objects.values_list('id', 'name').filter(name__istartswith=alph)
            if sg:
                service_group[alph] = sg
        except ServiceGroup.DoesNotExist as e:
            continue

    return service_group
