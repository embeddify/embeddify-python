from embeddify import index
from embeddify import lib


def configure(api_key_value, sanbox=False, base_url=False):
    lib.api_key = api_key_value
    if sanbox:
        lib.BASE_URL = base_url
