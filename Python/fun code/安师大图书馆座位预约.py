from math import floor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import re

url = 'http://libzwxt.ahnu.edu.cn/SeatWx/login.aspx?url=http%3a%2f%2flibzwxt.ahnu.edu.cn%2fSeatWx%2findex.aspx'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# 给定的基本信息
type_dict = {
    '2楼电子阅览室': [2, 'href="Room.aspx?rid=18&fid=1"'],
    '2楼报刊阅览室': [2, 'href="Room.aspx?rid=1&fid=1"'],
    '3楼公共·东': [3, 'href="Room.aspx?rid=13&fid=3"'],
    '3楼公共·西': [3, 'href="Room.aspx?rid=14&fid=3"'],
    '社科一': [3, 'href="Room.aspx?rid=5&fid=3"'],
    '4楼公共·东': [4, 'href="Room.aspx?rid=15&fid=5"'],
    '4楼公共·西': [4, 'href="Room.aspx?rid=16&fid=5"']
}
user_name = '21111202046'
pass_word = 'qwertyuiop0420!'
# floor_num, room_type = type_dict['2楼电子阅览室']
# floor_num, room_type = type_dict['3楼公共·东']
# floor_num, room_type = type_dict['3楼公共·西']
# floor_num, room_type = type_dict['社科一']
# floor_num, room_type = type_dict['4楼公共·东']
floor_num, room_type = type_dict['4楼公共·西']
specific_seat = ''
# likes_seats = ['ndz185', 'ndz184']
# likes_seats = ['ngg3e001']
# likes_seats = ['ngg3w001']
# likes_seats = ['nsk1026', 'nsk1027']
# likes_seats = ['ngg4e001']
likes_seats = ['ngg4w001']
unlike_seats = ['ngg3w026', 'ngg3w027']
select_time = ['20', '00', '22', '00']
select_date = ['00', '2024', '03', '1']
select_date = ''.join(select_date)
re_pattern = re.compile(r'\d+')
sid_pattern = re.compile(r'sid=(\d+)')
accept_all = '预约成功!'


try_cnt = 0

while try_cnt < 100:
    try:
        try_cnt += 1
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        user_name_input = driver.find_element(
            By.CSS_SELECTOR, '[id="tbUserName"]')
        break
    except Exception as e:
        driver.quit()
        print(f"An error occurred: {e}")
        time.sleep(0.1)


# 登陆窗口
user_name_input = driver.find_element(By.CSS_SELECTOR, '[id="tbUserName"]')
pass_word_input = driver.find_element(By.CSS_SELECTOR, '[id="tbPassWord"]')
signup = driver.find_element(By.CSS_SELECTOR, '[id="Button1"]')

# 登陆操作
user_name_input.clear()
user_name_input.send_keys(user_name)
pass_word_input.clear()
pass_word_input.send_keys(pass_word)
time.sleep(0.1)
signup.click()

# 进入选定楼层和房间
appoint = driver.find_element(By.CSS_SELECTOR, '[href="Order.aspx"]')
appoint.click()
time.sleep(0.1)
floor_in = driver.find_element(By.CSS_SELECTOR, '[href="Order.aspx?fid={}"]'.format(floor_num * 2 - 3))
floor_in.click()
time.sleep(0.1)
room_in = driver.find_element(By.CSS_SELECTOR, '[%s]' % room_type)
room_in.click()
time.sleep(0.1)


def get_seat_name(elem):
    return elem.text.strip()


def get_specific_seat(seat_name, seats):
    seat_idx = int(re_pattern.findall(seat_name)[-1][-3:])
    res_seat = seats[seat_idx - 1]
    if get_seat_name(res_seat) == seat_name:
        return res_seat
    return None


def see_elem(driver, elem):
    element_location = elem.location
    driver.execute_script(
        f"window.scrollTo(0, {element_location['y'] - 300});")
    time.sleep(0.1)


def set_time(driver, select_time):
    sttime1 = driver.find_element(By.CSS_SELECTOR, '[id="stTime1"]')
    sttime2 = driver.find_element(By.CSS_SELECTOR, '[id="stTime2"]')
    ettime1 = driver.find_element(By.CSS_SELECTOR, '[id="etTime1"]')
    ettime2 = driver.find_element(By.CSS_SELECTOR, '[id="etTime2"]')
    see_elem(driver, sttime1)
    select0 = Select(sttime1)
    select0.select_by_visible_text(select_time[0])
    select1 = Select(sttime2)
    select1.select_by_visible_text(select_time[1])
    select2 = Select(ettime1)
    select2.select_by_visible_text(select_time[2])
    select3 = Select(ettime2)
    select3.select_by_visible_text(select_time[3])


def set_date(driver, select_date):
    dateui = driver.find_element(By.CSS_SELECTOR, '[id="OrderDate"]')
    see_elem(driver, dateui)
    dateui.send_keys(select_date)


def get_seat(driver, seat):
    print('正在抢座位：%s\t' % get_seat_name(seat), end='')
    see_elem(driver, seat)
    time.sleep(0.1)
    seat.click()
    set_date(driver, select_date)
    set_time(driver, select_time)

    apply = driver.find_element(By.CSS_SELECTOR, '[class="apply-btn"]')
    see_elem(driver, apply)
    apply.click()
    confirm = driver.find_element(By.CSS_SELECTOR, '[class="pop-btn"]')
    see_elem(driver, confirm)
    confirm.click()
    alert = driver.switch_to.alert
    alert_text = alert.text  # 获取警告框的文本
    time.sleep(0.1)
    alert.accept()  # 点击"确定"按钮

    if alert_text == accept_all:
        print('预约成功，座位为: %s' % get_seat_name(seat))
        return True
    else:
        driver.back()
        print(alert_text)
        return False


# 抢座位
def Get_myseat():
    # 优先选择喜欢的座位
    for lks in likes_seats:
        seats = driver.find_element(
            By.CSS_SELECTOR, '[id="ulSeat"]').find_elements(By.XPATH, './*')
        elem = get_specific_seat(lks, seats)
        if get_seat(driver, elem):
            return
    seats_temp = driver.find_element(
        By.CSS_SELECTOR, '[id="ulSeat"]').find_elements(By.XPATH, './*')
    length = len(seats_temp)
    for i in range(length):
        seats = driver.find_element(
            By.CSS_SELECTOR, '[id="ulSeat"]').find_elements(By.XPATH, './*')
        if get_seat_name(seats[i]) in likes_seats+unlike_seats:
            continue
        if get_seat(driver, seats[i]):
            return
    print('预约失败！！！')


Get_myseat()
driver.quit()
