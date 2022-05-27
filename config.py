from os import getenv
from dotenv import load_dotenv
import os

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
SESSION_NAME = getenv("SESSION_NAME", "BQCdZUPVqWdHudEeVSwMaYj2FoNB7x5LMGmFBTSe603Zo8shg0e_pxyqAJ59lxCvBblBOg-yn3nxNkzleIuv3q4poErGNQLNy2QL11BBjiZv2FK47xWn522ECLgWUg4Tnxhs_gkOZQjWkLkP1NWibeaxy0y5ufTaDS905u7ksMedBw_XBjeZHFkL4kLdRbnerhijU2UP1aJ0QfEN9nrSSDJj6NxxrFpg53nnlT4H9MXyZkGvMa9_CERrgCVlyz4bKcEOqw9RrQk6PhwnawfbkP3ESgFLT3FtBCvmZGFDTY2-1wFQzla9mK00KluI2n_266KZJqFnHLXIbR329-Yyy2ddbAMQnwA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ".").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
OWNER_IDS = list(map(int, getenv("OWNER_IDS", "5174965229").split()))
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)
