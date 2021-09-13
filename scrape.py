import requests
import json
import random
import base64
import sys


def GetLogin():
    DUMMY_PHPSESSID = random.randint(111111,999999)
    # print(DUMMY_PHPSESSID)
    username="sarthak"
    password="Mayank@3211"
    url = "http://trace.csatransportation.com/inc/tm_ajax.msw"
    payload='func=SubmitLogin&remember_password=1&tm4web_pwd=Vansh%403211&tm4web_usr=sarthak'
    headers = {
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'Cookie': 'PHPSESSID='+str(DUMMY_PHPSESSID)
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return DUMMY_PHPSESSID
def GetQuoteId(length,width,height,weight,FROM,TO):
    url = "http://trace.csatransportation.com/rating/rq_ajax.msw"

    payload = json.dumps({
    "LBL_HEADING": "",
    "setRateBy": "",
    "TLORDER": {
        "SERVICE_LEVEL": "CONSOLIDAT",
        "SITE_ID": "SITE 1",
        "START_ZONE": FROM,
        "END_ZONE": TO,
        "DECLARED_VALUE": "0",
        "CUSTOMER": "CSALA",
        "CALLNAME": "CSA-FONTANA TERMINAL",
        "CALLADDR1": "",
        "CALLADDR2": "10847 POPLAR AVENUE",
        "CALLCITY": "FONTANA",
        "CALLPROV": "CA",
        "CALLPC": "92337",
        "CALLCOUNTRY": "US",
        "CALLPHONE": "562-483-8780",
        "CALLFAX": "562-483-8781",
        "CALLCONTACT": "MICHAEL SERRANO",
        "CALLCELL": "866-483-8780",
        "CALLEMAIL": "TEST@CSATRANSPORTATION.COM",
        "CURRENT_ZONE": "CSALA",
        "CALLER_currency_code": "USD",
        "CALLER_default_commodity": "",
        "CALLER_default_uom": "SKD",
        "CALLER_bill_to": "True ",
        "CURRENCY_CODE": "USD",
        "CALLER_commodity_client_id": "-1asdf",
        "BILL_TO_CODE": "",
        "BILL_TO_NAME": "",
        "DESTCITY": "",
        "DESTPROV": "",
        "DESTPC": "",
        "DEST_zone_desc": ""
    },
    "TLDTL": [
        {
        "SEQUENCE": -1,
        "densityCalculatorAccess": None,
        "COMMODITY": "COM",
        "REQUESTED_EQUIPMEN": "LTL",
        "LENGTH_1": int(length),
        "WIDTH": int(width),
        "HEIGHT": int(height),
        "WEIGHT": int(weight),
        "DESCRIPTION": "item 1",
        "PIECES": 1,
        "PIECES_UNITS": "SKD"
        }
    ],
    "TLDTL_DELETE": [],
    "DG_DTL": [],
    "DG_DTL_DELETE": [],
    "CONTAINER_TLORDER": [],
    "LTL_DEL_OPTIONS": {},
    "ACHARGE_TLORDER": [],
    "xcharges": {
        "all": [],
        "p": [],
        "d": [],
        "c": [],
        "o": []
    },
    "ORDER_INTERLINER": {
        "INTERLINER_ID": "",
        "NAME": "",
        "EMAIL_NOTIFY": "",
        "FUNCTIONAL_AMT": "",
        "CURRENCY_CODE": "",
        "CARGO": "",
        "FUEL_DATE": ""
    },
    "TLSHIPINSTRUCT": [],
    "shipInstruct": {
        "p": [],
        "d": [],
        "o": []
    },
    "WEB_DENSITY_CALC_SUMMARY_HISTORY": [
        {
        "TOTAL_CUBE": "",
        "TOTAL_WEIGHT": "",
        "TOTAL_DENSITY": "",
        "ACTUAL_CLASS": ""
        }
    ],
    "attachFiles": [],
    "email_options": {
        "email_pdf_pur": False,
        "email_html_pur": False,
        "email_pdf_to_pur": "none",
        "email_html_to_pur": "none",
        "email_pdf_ship": False,
        "email_html_ship": False,
        "email_pdf_to_ship": "none",
        "email_html_to_ship": "none"
    },
    "func": "RateQuote"
    })
    headers = {
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'Cookie': 'PHPSESSID='+ACTUAL_PHPSESSIONID
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response.json()['DETAIL_LINE_ID']
def GetQuote(length,width,height,weight,FROM,TO):

    url = "http://trace.csatransportation.com/rating/rq_ajax.msw?func=RateResult&dld="+str(GetQuoteId(length,width,height,weight,FROM,TO))

    payload={}
    headers = {
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'Cookie': 'PHPSESSID='+ACTUAL_PHPSESSIONID
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    quoteData=response.json()
    grandTotal=quoteData['selectedOrder']['GRAND_TOTAL']
    print("Grand Total ",grandTotal)
def GetLocation(FROM):
    base64_string ="aHR0cDovL3RyYWNlLmNzYXRyYW5zcG9ydGF0aW9uLmNvbS9pbmMvdG1fYWpheC5tc3c/U0VSVklDRV9MRVZFTD1DT05TT0xJREFUJlNJVEVfSUQ9U0lURSAxJlNUQVJUX1pPTkU9QkNWQU4mRU5EX1pPTkU9JkRFQ0xBUkVEX1ZBTFVFPTAmQ1VTVE9NRVI9Q1NBTEEmQ0FMTE5BTUU9Q1NBLUZPTlRBTkEgVEVSTUlOQUwmQ0FMTEFERFIxPSZDQUxMQUREUjI9MTA4NDcgUE9QTEFSIEFWRU5VRSZDQUxMQ0lUWT1GT05UQU5BJkNBTExQUk9WPUNBJkNBTExQQz05MjMzNyZDQUxMQ09VTlRSWT1VUyZDQUxMUEhPTkU9NTYyLTQ4My04NzgwJkNBTExGQVg9NTYyLTQ4My04NzgxJkNBTExDT05UQUNUPU1JQ0hBRUwgU0VSUkFOTyZDQUxMQ0VMTD04NjYtNDgzLTg3ODAmQ0FMTEVNQUlMPVRFU1RAQ1NBVFJBTlNQT1JUQVRJT04uQ09NJkNVUlJFTlRfWk9ORT1DU0FMQSZDQUxMRVJfY3VycmVuY3lfY29kZT1VU0QmQ0FMTEVSX2RlZmF1bHRfY29tbW9kaXR5PSZDQUxMRVJfZGVmYXVsdF91b209U0tEJkNBTExFUl9iaWxsX3RvPVRydWUgJkNVUlJFTkNZX0NPREU9VVNEJkNBTExFUl9jb21tb2RpdHlfY2xpZW50X2lkPS0xYXNkZiZCSUxMX1RPX0NPREU9JkJJTExfVE9fTkFNRT0mT1JJR0NJVFk9Jk9SSUdQUk9WPSZPUklHUEM9Jk9SSUdfem9uZV9kZXNjPSZmdW5jPUxvb2t1cFpvbmVzJmZlYXR1cmU9MiZ2bUZpZWxkPVNUQVJUX1pPTkUmbW92ZW1lbnRUeXBlPXsiU0VSVklDRV9MRVZFTCI6IkNPTlNPTElEQVQiLCJTSVRFX0lEIjoiU0lURSAxIiwiU1RBUlRfWk9ORSI6IkJDVkFOIiwiRU5EX1pPTkUiOiIiLCJERUNMQVJFRF9WQUxVRSI6IjAiLCJDVVNUT01FUiI6IkNTQUxBIiwiQ0FMTE5BTUUiOiJDU0EtRk9OVEFOQSBURVJNSU5BTCIsIkNBTExBRERSMSI6IiIsIkNBTExBRERSMiI6IjEwODQ3IFBPUExBUiBBVkVOVUUiLCJDQUxMQ0lUWSI6IkZPTlRBTkEiLCJDQUxMUFJPViI6IkNBIiwiQ0FMTFBDIjoiOTIzMzciLCJDQUxMQ09VTlRSWSI6IlVTIiwiQ0FMTFBIT05FIjoiNTYyLTQ4My04NzgwIiwiQ0FMTEZBWCI6IjU2Mi00ODMtODc4MSIsIkNBTExDT05UQUNUIjoiTUlDSEFFTCBTRVJSQU5PIiwiQ0FMTENFTEwiOiI4NjYtNDgzLTg3ODAiLCJDQUxMRU1BSUwiOiJURVNUQENTQVRSQU5TUE9SVEFUSU9OLkNPTSIsIkNVUlJFTlRfWk9ORSI6IkNTQUxBIiwiQ0FMTEVSX2N1cnJlbmN5X2NvZGUiOiJVU0QiLCJDQUxMRVJfZGVmYXVsdF9jb21tb2RpdHkiOiIiLCJDQUxMRVJfZGVmYXVsdF91b20iOiJTS0QiLCJDQUxMRVJfYmlsbF90byI6IlRydWUgIiwiQ1VSUkVOQ1lfQ09ERSI6IlVTRCIsIkNBTExFUl9jb21tb2RpdHlfY2xpZW50X2lkIjoiLTFhc2RmIiwiQklMTF9UT19DT0RFIjoiIiwiQklMTF9UT19OQU1FIjoiIiwiT1JJR0NJVFkiOiIiLCJPUklHUFJPViI6IiIsIk9SSUdQQyI6IiIsIk9SSUdfem9uZV9kZXNjIjoiIn0mdGFrZT0zMCZza2lwPTAmcGFnZT0xJnBhZ2VTaXplPTMwJmZpbHRlcltmaWx0ZXJzXVswXVtvcGVyYXRvcl09c3RhcnRzd2l0aCZmaWx0ZXJbZmlsdGVyc11bMF1bdmFsdWVdPQ=="
    base64_bytes = base64_string.encode("ascii")
    
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    
    url = sample_string+FROM
    payload={}
    headers = {
    'Cookie': 'rstring=8P8zVXvUjHgnMabw5Ci1W5ADHNU6Uv3NqeBBnxddJg4ZWguVTp; uid=SARTHAK; PHPSESSID=rddsin3tive3c67h78ip7d8g9c'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # print (response.json())
    return response.json()['data'][0]['ZONE_ID']


def RunProgram():
    # username=input('Enter Username To Login : ')
    # password=input('Enter Password To Login : ')
    TEMP_FROM=input('Enter From Location : ') 
    TEMP_TO = input('Enter To Location : ')
    length=input("Enter Length : ")
    width=input("Enter Width : ")
    height=input("Enter Height : ")
    weight=input("Enter Weight : ")
    FROM=GetLocation(TEMP_FROM)
    TO= GetLocation(TEMP_TO)
    GetQuote(length,width,height,weight,FROM,TO)
   

def RunProgramThroughCMD():
    # username=input('Enter Username To Login : ')
    # password=input('Enter Password To Login : ')
    TEMP_FROM=sys.argv[1]
    TEMP_TO = sys.argv[2]
    length=sys.argv[3]
    width=sys.argv[4]
    height=sys.argv[5]
    weight=sys.argv[6]
    FROM=GetLocation(TEMP_FROM)
    TO= GetLocation(TEMP_TO)
    GetQuote(length,width,height,weight,FROM,TO)
   
ACTUAL_PHPSESSIONID=str(GetLogin())


RunProgramThroughCMD()

# RunProgram()
# GetLocation('CALGARY, AB')
# print()