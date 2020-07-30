import os
from userbot.utils import clIent as CLIENT 
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from heroku_config import Var as Config
else:
    from local_config import Development as Config


Var = Config
