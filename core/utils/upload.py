import os
import uuid
from datetime import date


def upload_path(instance, name):
    hashed_name = str(uuid.uuid4())
    name, ext = os.path.splitext(name)
    final = hashed_name + ext
    path_sign = "/"
    return path_sign.join([instance.__class__.__name__, date.today().strftime('%Y/%m/%d'), final])
