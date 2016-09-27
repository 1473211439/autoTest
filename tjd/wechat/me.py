#coding=utf-8
from splinter import Browser
import time;

# with Browser() as browser:
# executable_path = {'executable_path': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'}
# browser = Browser('chrome', **executable_path)
browser = Browser()
url = "http://www.baidu.com"
loginUrl="http:test.tingjiandan.com/tcweixin/letter/login/login.html"
# 根据单号查询韵达快递
def queryYundaByNumber(theNumber):
    browser.visit(url)
    browser.fill('wd','韵达快递单号查询');
    button=browser.find_by_id('su');
    button.click()
    browser.find_by_css('.op_express_delivery_input_nu')[0].fill(theNumber)
    browser.find_by_css('.op_express_delivery_submit')[0].click();

# 根据手机号登录
def loginByPhone(phone):
    yzm='1025';
    browser.visit(loginUrl)
    phoneInput=browser.find_by_id('phone');
    getYzmBtn=browser.find_by_id('btnCode');
    yzmInput=browser.find_by_id('yzm');
    loginButton=browser.find_by_id('determine');
    phoneInput[0].fill(phone)
    getYzmBtn[0].click();
    yzmInput.fill(yzm)
    loginButton.click();
def go2MyCar():
    print(6)
    browser.find_link_by_partial_href('go2Car')[0].click();
    print(7)

#删除当前用户下所有汽车
def deleteCars():
    loginByPhone('18601965856');
    browser.execute_script('sessionStorage.isTest=1;')
    print(3)
    go2MyCar();
    print(1)
    cars=browser.find_by_css('.delete img');
    print(2)
    print("车辆总数:",len(cars))
    if(len(cars)>0):
        for car in cars:
            nowcars = browser.find_by_css('.delete img');
            time.sleep(1)
            nowcars.first.click();
            time.sleep(2)
            btn = browser.find_by_css('.modal_confirm_btn')[0];
            print(btn.visible)
            btn.click();
            time.sleep(1)
            cancel = browser.find_by_css('.modal_cancel_btn')[0];
            print(cancel)
            cancel.click();
            time.sleep(1)

    cars = browser.find_by_css('.delete img');
    print("剩余汽车数量：",len(cars))








# queryYundaByNumber('1901604055683');
# loginByPhone('18601965856');
deleteCars();








# browser.Navigate().GoToUrl(url);
# browser.fill('q', 'splinter - python acceptance testing for web applications')
# # Find and click the 'search' button
# button = browser.find_by_name('btnG')
# # Interact with elements
#
# if browser.is_text_present('splinter.cobrateam.info'):
#     print("Yes, the official website was found!")
# else:
#     print("No, it wasn't found... We need to improve our SEO techniques")

