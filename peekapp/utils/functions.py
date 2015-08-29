from django.utils.encoding import smart_text

import random
import hashlib


def generateGUID():
    return hashlib.sha1(smart_text(random.random())).hexdigest()
