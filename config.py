## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCad0wg2qW0nAwQeNAqmLDSfYIEhdv15t-ws4LE9bR9guBPFD0u2kxK0yZ9I_y4ir1sLA7YuYwiyn25vl5uiFxDu_LExVdDG1ORluzWTCHJteY9mHEgSFB1hNCOIYoacJspVK-0Rco43sM90NKn7vn0odYqxi9PX87dr2ZTNb70avt8qNPw8pdAcCV4e1MpWP5zpp38d2V0eXHW2ral2p4khr-W6D57LgJiS4GFVo5QegF9rs3OToZHXBtONGm4go8GKPrOcwgwIeaZFmWouUL8oyMLyL2wGfqKl7Z5p_y3wJRyZjA2oo3ous04t_qrD--tSn2ErE0Kg0WaOpsnAPjyAAAAAUd_dboA")
BOT_TOKEN = getenv("BOT_TOKEN", "5455000204:AAGg5ULnTQ7_7itR40NJpRU5mdcb7EbPOEo")
BOT_NAME = getenv("BOT_NAME", "𝖡𝗈𝗌𝗍𝗈𝗇 𝖬𝗎𝗌𝗂𝖼")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Parki")
OWNER_USERNAME = getenv("OWNER_USERNAME", "DBBBDD")
ALIVE_NAME = getenv("ALIVE_NAME", "Parki")
BOT_USERNAME = getenv("BOT_USERNAME", "KK3OKBoT")
OWNER_ID = getenv("OWNER_ID", "1283712566")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "KK3OK")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1283712566").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
