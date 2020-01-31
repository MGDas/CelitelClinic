import os
from slugify import slugify
from django.conf import settings

def get_title(instance):

    """Узнаем название переменной и возвращаем её."""

    try:
        title = instance.title
    except AttributeError:
        try:
            title = instance.full_name
        except AttributeError:
            title = instance.name

    if len(title) > 15:
        title = title[:15]

    return slugify(title)


def get_photo(instance, filename):

    """Создаем путь к файлу и имя."""

    format = filename.split('.')[-1]        # format    ex: ".jpg"
    title = get_title(instance)     # title, name, or full_name

    folder_name = "{0}".format(title)     # folder name ex: "magomedov-magomed"
    file_name = "{0}.{1}".format(title, format)       # filename ex: "magomedov-magomed.jpg"

    class_name = instance.__class__.__name__.lower() + 's'       # имя класса для названия папки    # ex: "doctors", "articles", ...

    full_path = "/".join([class_name, folder_name, file_name])    # full path to image ex: "doctors/magomedov-magomed/magomedov-magomed.jpg"

    if not os.path.exists(os.path.join(settings.MEDIA_ROOT, class_name, folder_name)):            # Проверяем есть ли такой путь
        os.makedirs(os.path.join(settings.MEDIA_ROOT, class_name, folder_name))     # Есди нет создаем новый

    return full_path
