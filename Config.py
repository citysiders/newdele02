import os
from dotenv import load_dotenv

class Config(object):
    API_ID = os.environ.get("API_ID", "28045580")
    API_HASH = os.environ.get("API_HASH", "83001e24418ec7f54bfe95d4e390419f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7010331289:AAHi4JikhnYekM5I-H1okx9ZSt-llG1TzOU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIcBu46eUr3hJ2DdavEiCwMyWK29RU6TH_nQNu5Tb1FCfvy0UWhDTSDM_Fqq7-qZVsJDlUdtg6xq-i9NXEi3NgdoIhuRfW2cd7u6lDi8qcQL4D-1iGLpwjcw625nt-Hwo8ve-bLCpagqE-mrA3GvlY9c2PkFyin4dRarwWWYhlLL7JOuN1_lL4v8jv-JyHRcgJOaxv_IusFHAp4aO6h-vkMj65CkfGiD3vMmP9QbLow5ZWdocet-VT9AgcPZUhJWq938TqyBBluHxKT_QYRedcAe0f6UVC74tKRq0HsOlm8Lft71ee0_j5bwO4hTiSYqiEmXtj23gOi_oAvyf01WEAtd3mM=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "testingggsz_bot")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/universe_we_are") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/we_are_universee") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/c7fc58423bbdac8159654.mp4")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/0dfe1b6f8676bf56446b6.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "7029090289")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
    SUDOERS = list(map(int, os.getenv("SUDOERS", "1556830659").split()))  # Assuming you list SUDOERS in your .env
