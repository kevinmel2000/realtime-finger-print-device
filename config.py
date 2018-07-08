import os
from dotenv import load_dotenv
load_dotenv(verbose=True, dotenv_path="./.env")

#define device configuration
DEVICE_IP=os.getenv("DEVICE_IP")
DEVICE_PORT=int(os.getenv("DEVICE_PORT"))
DEVICE_TIMEOUT=float(os.getenv("DEVICE_TIMEOUT")) #10second

MYSQL_DATABASE=os.getenv("MYSQL_DATABASE")
MYSQL_HOST=str(os.getenv("MYSQL_HOST"))
MYSQL_PORT=int(os.getenv("MYSQL_PORT"))
MYSQL_USERNAME=os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD")