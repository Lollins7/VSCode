from math import floor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# import logging
import time
import re

url = 'http://libzwxt.ahnu.edu.cn/SeatWx/login.aspx?url=http%3a%2f%2flibzwxt.ahnu.edu.cn%2fSeatWx%2findex.aspx'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# 给定的基本信息
type_dict = {
    '2楼电子阅览室': [2, 'href="Room.aspx?rid=18&fid=1"'],
    '2楼报刊阅览室': [2, 'href="Room.aspx?rid=1&fid=1"'],
    '3楼公共·东': [3, 'href="Room.aspx?rid=13&fid=3"']
}
user_name = '21111202046'
pass_word = 'qwertyuiop0420!'
# floor_num, room_type = type_dict['2楼电子阅览室']
floor_num, room_type = type_dict['3楼公共·东']
specific_seat = ''
# likes_seats = ['ndz185', 'ndz184']
likes_seats = ['ngg3e063', 'ngg3e064']
select_time = ['19', '00', '20', '00']
select_date = ['00', '2024', '02', '26']
select_date = ''.join(select_date)
re_pattern = re.compile(r'\d+')
sid_pattern = re.compile(r'sid=(\d+)')
accept_all = '预约成功!'

# # 配置日志记录
# logging.basicConfig(filename='log/user_%s.log' % user_name,
#                     level=logging.INFO, format='%(asctime)s - %(message)s')
# logger = logging.getLogger(__name__)

try_cnt = 0
# logger.info('开始执行程序')

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

# logger.info('成功获取网页')
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
    seat_idx = int(re_pattern.findall(seat_name)[-1])
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
            # logger.info('座位获取成功：%s' % get_seat_name(elem))
            return
    # logger.info('未获得喜欢的座位')
    seats_temp = driver.find_element(
        By.CSS_SELECTOR, '[id="ulSeat"]').find_elements(By.XPATH, './*')
    length = len(seats_temp)
    for i in range(length):
        seats = driver.find_element(
            By.CSS_SELECTOR, '[id="ulSeat"]').find_elements(By.XPATH, './*')
        if get_seat_name(seats[i]) in likes_seats:
            continue
        if get_seat(driver, seats[i]):
            # logger.info('座位获取成功：%s' % get_seat_name(elem))
            return
    print('预约失败！！！')
    # logger.info('座位爬取失败')


Get_myseat()
driver.quit()
