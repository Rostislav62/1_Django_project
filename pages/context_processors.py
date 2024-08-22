# my_site/pages/context_processors.py
from .contact_info import CONTACT_INFO

def contact_info_processor(request):
    return {
        'contact_info': CONTACT_INFO
    }
