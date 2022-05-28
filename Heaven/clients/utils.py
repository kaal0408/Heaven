import logging
import platform
import time

from pyrogram import __version__ as pyro_version
from telegraph import Telegraph

from Heaven.database import Database
from Heaven.helpers import Helpers
from Heaven.pyrogramx.methods import Methods
from config import Config


class Utils(Methods, Config, Database, Helpers):
    # versions /

    userbot_version = "v.0.0.1"
    assistant_version = "v.0.0.1"
    python_version = str(platform.python_version())
    pyrogram_version = str(pyro_version)

    # containers /

    CMD_HELP = {}

    # owner details /

    owner_name = "Manjeet"
    owner_username = "@Hayat_Murat_30"

    # other /

    Repo = "https://github.com/kaal0408/Heaven.git"
    StartTime = time.time()

    # debugging /

    logging.getLogger("pyrogram.syncer").setLevel(
        logging.CRITICAL
    )  # turn off pyrogram logging
    logging.getLogger("pyrogram").setLevel(logging.CRITICAL)

    logging.basicConfig(format="%(asctime)s %(message)s")
    log = logging.getLogger("———")

    # telegraph /

    telegraph = Telegraph()
    telegraph.create_account(
        short_name=Config.TL_NAME if Config.TL_NAME else "Heaven Userbot"
    )
