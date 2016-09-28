from splinter import Browser
import time;

# with Browser() as browser:
# executable_path = {'executable_path': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'}
# browser = Browser('chrome', **executable_path)
browser = Browser('chrome')
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

def autoPayMachineTest(params):
    commonYzm="1025";
    url="http://test.tingjiandan.com/tcweixin/letter/autoPayMachine/main.html?selfMacId="+params['selfMacId'];
    browser.visit(url)
    time.sleep(1)

    if len(params['phone']) !=11:
        print('手机号长度不对！');
        return;

    if len(params['toSearchCarNum'])>7:
        print('车牌号过长！');
        return;
    elif len(params['toSearchCarNum'])<3:
        print('车牌号至少3位！')
        return;
    else:
        carNumLen=len(params['toSearchCarNum']);
        count=0;
        while (count<carNumLen):
            browser.find_by_value(params['toSearchCarNum'][count]).last.click();#防止有相同数字或字母后，下次自动点击到上方输入框的值上边
            time.sleep(0.3)
            count=count+1;

    time.sleep(1)
    searchBtn = browser.find_by_id('search');
    searchBtn.click();
    time.sleep(1)
    payBtn = browser.find_by_css('.payBtn').first;
    payBtn.click();
    time.sleep(1)

    # browser.find_by_css('.carscontent li:eq(0)').first;

    browser.execute_script("$('.carscontent li:eq(0) p').click()");
    time.sleep(1)
    # 老版本的话直接返回
    if params['isOld']:
        return;
    # //注册
    registerBtn=browser.find_by_css(".memberLoginRegister a:last-child").first;
    registerBtn.click();
    quickRegisterBtn=browser.find_by_css(".register a").first;
    quickRegisterBtn.click();
    time.sleep(1)
    # 先登陆，如果不存在的话，注册
    phoneInputOfRegister=browser.find_by_css('.joycityRegister .tjdPhone').first;
    getYzmBtnOfRegister=browser.find_by_css('.joycityRegister .tjdYzmBtn').first;
    yzmInputOfRegister=browser.find_by_css('.joycityRegister .tjdYzm').first;
    register=browser.find_by_css('.joycityRegister .sure').first;
    phoneInputOfRegister.type(params['phone'])
    getYzmBtnOfRegister.click();
    yzmInputOfRegister.type(commonYzm);
    time.sleep(1)
    register.click();

    time.sleep(1)
    modalText=browser.find_by_css('.tjdModal_mainTitle').first;
    if modalText.visible:
        print(modalText.value)
        if modalText.value!="注册中，请稍等。。。" and modalText.value=="手机号已经注册过" :
            browser.find_by_css('.modal_cancel_btn').first.click();
            browser.reload();
            time.sleep(1);
            # 先登陆，如果不存在的话，注册
            loginBtn = browser.find_by_css(".memberLoginRegister a:first-child").first;
            loginBtn.click();
            time.sleep(1)
            phoneInputOfLogin = browser.find_by_css('.joycityLogin .tjdPhone').first;
            getYzmBtnOfLogin = browser.find_by_css('.joycityLogin .tjdYzmBtn').first;
            yzmInputOfLogin = browser.find_by_css('.joycityLogin .tjdYzm').first;
            login = browser.find_by_css('.joycityLogin .sure').first;
            phoneInputOfLogin.type(params['phone'])
            getYzmBtnOfLogin.click();
            yzmInputOfLogin.type(commonYzm);
            time.sleep(1)
            login.click();
    time.sleep(1)
    exchangeBtn = browser.find_by_css('.sureScore').first;
    if params['isExhangeAllTickets']:
        allTicketsBtn = browser.find_by_css('.allTickets');
        if len(allTicketsBtn)>0:
            allTicketsBtn = browser.find_by_css('.allTickets').first;
            if allTicketsBtn.visible:
                allTicketsBtn.click();
                time.sleep(1);
                exchangeBtn.click();
    if params['commonTicketsNum'] >0:
        time.sleep(1)
        commonTicketsArea=browser.find_by_css('.hourDeduction');
        if len(commonTicketsArea)>0:
            commonTicketsArea=browser.find_by_css('.hourDeduction').first;
            if commonTicketsArea.visible:
                count=0;
                while count<params['commonTicketsNum'] :
                    plusBtn = browser.find_by_css('.plus_btn').first;
                    plusBtn.click();
                    count=count+1;
                    modalText = browser.find_by_css('.tjdModal_mainTitle');
                    if modalText.visible:

                        modalText = browser.find_by_css('.tjdModal_mainTitle').first;
                        if modalText.value.find('最多能选择')!=-1:
                            browser.find_by_css('.modal_cancel_btn').first.click();
                            time.sleep(1)
                            break;
                    time.sleep(1)
                exchangeBtn.click();



 # adjustClassWhenNoButton


#****************************************************************************************************

# queryYundaByNumber('1901604055683');
# loginByPhone('18601965856');
# deleteCars();
# autoPayMachineTest("e28aa5b26b6942b2a401306f623da0ee","京A23456",'19421025025',1,4);
# autoPayMachineTest({
#     'selfMacId':'e28aa5b26b6942b2a401306f623da0ee',
#     'toSearchCarNum':'京A23456',
#     'phone':'19421025121',
#     'isExhangeAllTickets':False, #是否兑换所有停车券
#     'commonTicketsNum':6     #兑换普通停车券的张数
# });
autoPayMachineTest({
    'selfMacId':'1aca5a1fd245493cb124b38bfa96880d',
    'toSearchCarNum':'晋BRQ444',
    'phone':'19421025121',
    'isExhangeAllTickets':False, #是否兑换所有停车券
    'commonTicketsNum':6,   #兑换普通停车券的张数,
    'isOld':True#是否老版本的缴费机（无会员积分系统）
});








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

