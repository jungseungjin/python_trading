# Response

# 필드명	설명	타입
# market	업비트에서 제공중인 시장 정보	String
# korean_name	거래 대상 암호화폐 한글명	String
# english_name	거래 대상 암호화폐 영문명	String
# market_warning	유의 종목 여부
# NONE (해당 사항 없음), CAUTION(투자유의)	String

import requests
import json
from openpyxl import Workbook
import os


url = "https://api.upbit.com/v1/market/all?isDetails=false"

headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
marketData = json.loads(response.text)

list = {}
execlFileNames = os.listdir('./excel')

for item in marketData:
    market = item["market"]
    if "KRW" in market : 
        list[market] = 1
    

for index,marketName in enumerate(list.keys()):
    if f"{marketName}.xlsx" in execlFileNames : continue
    write_wb = Workbook()
    write_ws = write_wb.create_sheet(marketName,0)
    write_ws = write_wb.active
    write_wb.save(f'./excel/{marketName}.xlsx')


