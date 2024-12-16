from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import datetime
import time
import urllib.parse as parse


def quote(qstr: str):
    return parse.quote(qstr, encoding="shift-jis")

def make_5489_url(
    depSta = "京都",
    arrSta = "下関",
    inputDate = "20250110",
    inputHour = "21",
    inputMinute = "00",
    inputType= "0",
    inputUniqueDepartSt = "1",
    inputUniqueArriveSt = "1",
    inputSearchType = "2",
    inputSpecificBriefTrainKana1 = 'ｷﾖｳｸｼ',
    inputTransferDepartStName1 = "京都",
    inputTransferArriveStName1 = "下関",
    inputTransferDepartStUnique1 = "1",
    inputTransferArriveStUnique1 = "1",
    inputTransferTrainType1 = "0001",
    inputSpecificTrainType1 = "2",
):
    base_url = "https://e5489.jr-odekake.net/e5489/cspc/CBDayTimeArriveSelRsvMyDiaPC?"
    str_attrs = [
        f"&inputDepartStName={quote(depSta)}",
        f"&inputArriveStName={quote(arrSta)}",
        f"&inputDate={inputDate}",
        f"&inputHour={inputHour}",
        f"&inputMinute={inputMinute}",
        f"&inputType={inputType}",
        f"&inputUniqueDepartSt={inputUniqueDepartSt}",        
        f"&inputUniqueArriveSt={inputUniqueArriveSt}",
        f"&inputSearchType={inputSearchType}",
        f"&inputSpecificBriefTrainKana1={quote(inputSpecificBriefTrainKana1.ljust(5, " ") + "000")}",
        f"&inputTransferDepartStName1={quote(inputTransferDepartStName1)}",
        f"&inputTransferArriveStName1={quote(inputTransferArriveStName1)}",
        f"&inputTransferDepartStUnique1={inputTransferDepartStUnique1}",
        f"&inputTransferArriveStUnique1={inputTransferArriveStUnique1}",
        f"&inputTransferTrainType1={inputTransferTrainType1}",
        f"&inputSpecificTrainType1={inputSpecificTrainType1}",        
    ]
    return base_url + ''.join(str_attrs)

def wait_1000():
    t_delta = datetime.timedelta(hours=9)  # 9時間
    JST = datetime.timezone(t_delta, 'JST')
    while True:
        dt = datetime.datetime.now(JST)
        if dt.hour == 10 and dt.minute == 0:
            break
        else:
            time.sleep(0.1)

def set_driver(
    s,
):
    url = make_5489_url(s.inputDepartStName,
                s.inputArriveStName,
                s.inputDate,
                s.inputHour,
                s.inputMinute,
                s.inputType,
                s.inputUniqueDepartSt,
                s.inputUniqueArriveSt,
                s.inputSearchType,
                s.inputSpecificBriefTrainKana1,
                s.inputTransferDepartStName1,
                s.inputTransferArriveStName1,
                s.inputTransferDepartStUnique1,
                s.inputTransferArriveStUnique1,
                s.inputTransferTrainType1,
                s.inputSpecificTrainType1,
             )
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    if s.wait_10_o_clock:
        wait_1000()
    driver.get(url)
    return driver

def keiro_setsubi(driver):
    driver.find_element(By.XPATH, "//span[.//img[@alt='空席あり']]").click()
    driver.find_element(By.CLASS_NAME, "decide-button").click()
   
def kippu_select(driver):
    driver.find_element(By.CLASS_NAME, "decide-button").click()
    
def login(driver, s):
    driver.find_element(By.ID, "name1").send_keys(s.name1)
    driver.find_element(By.ID, "name2").send_keys(s.name2)
    driver.find_element(By.ID, "tel1").send_keys(s.tel1)
    driver.find_element(By.ID, "tel1conf").send_keys(s.tel1)
    driver.find_element(By.ID, "tel2").send_keys(s.tel2)
    driver.find_element(By.ID, "tel2conf").send_keys(s.tel2)
    driver.find_element(By.ID, "tel3").send_keys(s.tel3)
    driver.find_element(By.ID, "tel3conf").send_keys(s.tel3)
    driver.find_element(By.ID, "email1").send_keys(s.email)
    driver.find_element(By.ID, "email2").send_keys(s.email)
    driver.find_element(By.CLASS_NAME, "check").click()
    driver.find_element(By.CLASS_NAME, "decide-button").click()

def kiyaku(driver):
    driver.find_element(By.CLASS_NAME, "check").click()
    driver.find_element(By.CLASS_NAME, "decide-button").click()

def zaseki(driver, skip_zaseki=False):
    Select(driver.find_element(By.ID, "number-of-adult-passengers")).select_by_value("4")
    driver.find_element(By.XPATH, "//span[text()='離れた席でもよい']").click()
    driver.find_element(By.XPATH, "//span[text()='乗車券なし']").click()
    driver.find_element(By.CLASS_NAME, "decide-button").click()

def yoyaku(driver):
    driver.find_element(By.XPATH, "//div[@data-id='select2']").click()
    driver.find_element(By.XPATH, "//input[@type='radio' and @name='settlemthdKbn' and @value='4']").click()
    driver.find_element(By.XPATH, "//span[text()='予約する']").click()


