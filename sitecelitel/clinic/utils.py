from slugify import slugify

def get_image_pc(instance, filename):
    format = filename.split('.')[-1]
    slug = slugify(instance.title[:30])
    file_name = f"{slug}_pc.{format}"

    return "/".join(["sliders", f"{slug}", file_name])


def get_image_mob(instance, filename):
    format = filename.split('.')[-1]
    slug = slugify(instance.title[:30])
    file_name = f"{slug}_mob.{format}"

    return "/".join(["sliders", f"{slug}", file_name])


def get_image_partner(instance, filename):
    format = filename.split('.')[-1]
    slug = slugify(instance.name[:30])
    file_name = f"{slug}_mob.{format}"

    return "/".join(["partners", f"{slug}", file_name])
