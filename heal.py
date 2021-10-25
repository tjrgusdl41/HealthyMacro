import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui


def health_pa(name, birth, pw):
    brow = webdriver.Chrome()
    brow.maximize_window()

    brow.get('https://hcs.eduro.go.kr/')

    # 자가진다 버튼 클릭
    elem = brow.find_element_by_xpath('//*[@id="btnConfirm2"]')
    elem.click()

    elem = brow.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[1]/td/button')
    elem.click()
    # 대구광역시 클릭
    elem = brow.find_element_by_xpath('//*[@id="sidolabel"]/option[4]')
    elem.click()
    # 고등학교 클릭
    brow.find_element_by_xpath('//*[@id="crseScCode"]/option[5]').click()

    elem = brow.find_element_by_xpath('//*[@id="orgname"]')
    elem.send_keys('소프트웨어')
    elem.send_keys(Keys.ENTER)

    time.sleep(1)  # 소프트웨어 검색 하고 나서 바로 안뜰수도 있어서 1초 쉼.

    brow.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p').click()
    time.sleep(0.2)
    brow.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
    time.sleep(0.2)
    # 이름넣기
    elem = brow.find_element_by_xpath('//*[@id="user_name_input"]')
    time.sleep(0.5)
    elem.send_keys(name)

    # 생년월일 넣기
    brow.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(birth)
    time.sleep(0.5)
    brow.find_element_by_xpath('//*[@id="btnConfirm"]').click()

    # 비밀번호 넣기
    time.sleep(2)
    brow.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').click()
    time.sleep(0.5)
    print("시작한다")
    for p in pw:
        time.sleep(0.2)
        img = pyautogui.locateOnScreen('./keyboard/' + str(p) + '.PNG', confidence=0.9)
        pyautogui.click('./keyboard/'+str(p)+'.PNG')
    #
    # print("끝났다")
    brow.find_element_by_xpath('//*[@id="btnConfirm"]').click()


    # 이름 생년월일 비밀번호 사용자 입력받는거...

    time.sleep(2)
    brow.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/span[1]').click()
    time.sleep(2)
    brow.find_element_by_xpath('//*[@id="survey_q1a1"]').click()
    brow.find_element_by_xpath('//*[@id="survey_q2a1"]').click()
    brow.find_element_by_xpath('//*[@id="survey_q3a1"]').click()
    brow.find_element_by_xpath('//*[@id="btnConfirm"]').click()

    time.sleep(2)
    brow.quit()
