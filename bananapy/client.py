import aiohttp 
from box import Box

class Error(Exception):
    """
    Error that is caused when the client returns a status code other than 200 (success).
    """
    pass


class Client:
    