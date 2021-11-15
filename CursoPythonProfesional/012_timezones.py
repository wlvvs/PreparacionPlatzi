from icecream import ic 
from datetime import datetime
import pytz

bogota_timezone = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_timezone)
mexico_timezone = pytz.timezone('America/Mexico_City')
mexico_date = datetime.now(mexico_timezone)
alaska_timezone = pytz.timezone('US/Alaska')
alaska_date = datetime.now(alaska_timezone)
rusia_timezone = pytz.timezone('Europe/Moscow')
rusia_date = datetime.now(rusia_timezone)
venezuela_timezone = pytz.timezone('America/Caracas')
venezuela_date = datetime.now(venezuela_timezone)

ic(bogota_date.strftime('%d/%m/%Y, %H:%M:%S'))
ic(mexico_date.strftime('%d/%m/%Y, %H:%M:%S'))
ic(alaska_date.strftime('%d/%m/%Y, %H:%M:%S'))
ic(rusia_date.strftime('%d/%m/%Y, %H:%M:%S'))
ic(venezuela_date.strftime('%d/%m/%Y, %H:%M:%S'))
