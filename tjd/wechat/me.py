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
    browser.execute_script('sessionStorage.isTest=1;')
    loginButton.click();
def go2MyCar():
    browser.find_link_by_partial_href('go2Car')[0].click();

#删除当前用户下所有汽车
def deleteCars():
    loginByPhone('18601965856');
    browser.execute_script('sessionStorage.isTest=1;')
    go2MyCar();
    cars=browser.find_by_css('.delete img');
    print("车辆总数:",len(cars))
    if(len(cars)>0):
        for car in cars:
            nowcars = browser.find_by_css('.delete img');
            time.sleep(1)
            nowcars.first.click();
            time.sleep(2)
            btn = browser.find_by_css('.modal_confirm_btn')[0];
            btn.click();
            time.sleep(1)
            cancel = browser.find_by_css('.modal_cancel_btn')[0];
            cancel.click();
            time.sleep(1)

    cars = browser.find_by_css('.delete img');
    print("剩余汽车数量：",len(cars))

def fillCarNum(carNum):
    count=0;
    for c in carNum:
        browser.find_by_value(c).last.click()
        time.sleep(0.3);
def fillCarColor(color):
    browser.execute_script("$(\"span[color='" + color + "']:visible\").click()");
    # browser.find_by_css("span[color='" + color + "']:visible").first.click();
    time.sleep(0.5)
#添加汽车
def addCar(carNum,color):
    time.sleep(1)
    addBtn = browser.find_by_css('.con a img');
    if len(addBtn) > 0:
        addBtn = addBtn.first;
        if addBtn.visible:
            addBtn.click();
        else:
            return;
    else:
        return;

    time.sleep(1)
    fillCarNum(carNum)
    # //车牌颜色
    fillCarColor(color);
    browser.find_by_css(".revise").first.click();
    time.sleep(0.5)
    browser.find_by_css(".modal_confirm_btn").last.click();
    time.sleep(2)
    browser.find_by_css(".modal_cancel_btn").last.click();
def modalConfirm():
    oneConfirmBtn=browser.find_by_css(".modal_cancel_btn").first;
    twoConfirmBtn=browser.find_by_css(".modal_confirm_btn").first;
    if twoConfirmBtn.visible:
        twoConfirmBtn.click();
    else:
        oneConfirmBtn.click();
def uptCar(oldCarNum,newCarNum,newColor):
    old=browser.find_by_text(oldCarNum);
    if(len(old)>0):
        old=old.first;
        if(old.visible):
            browser.execute_script("$('p:contains(\""+oldCarNum+"\")').parent().find('.carstate:visible').find('a:last').find('span').click()");
            time.sleep(1)
            fillCarNum(newCarNum)
            time.sleep(1)
            fillCarColor(newColor)
            time.sleep(0.5)
            browser.find_by_css(".revise").first.click();
            time.sleep(0.5)
            modalConfirm();
            time.sleep(3)
            modalConfirm();
    else:
        print("要修改的车牌号不存在！！！")
def verifyCar(carNum,motorNum,viNum):
    old=browser.find_by_text(carNum);
    if(len(old)>0):
        old=old.first;
        if(old.visible):
            m=browser.execute_script("$('p:contains(\""+carNum+"\")').parent().find('.carstate:visible').find('a:first').find('span').click()");
            motorNumInput=browser.find_by_css('.motorNum');
            viNumInput=browser.find_by_css('.viNumInput');
            if (len(motorNumInput)<1 and len(viNumInput)<1):
                print("请先激活车辆！！！")
                return;

            if len(motorNumInput)==1:
                if motorNumInput.first.visible:
                    motorNumInput.first.fill(motorNum)
            if len(viNumInput)==1:
                if viNumInput.first.visible:
                    viNumInput.first.fill(viNum)
            if motorNumInput.first.visible==False and viNumInput.first.visible==False:
                return;
            time.sleep(1);
            browser.find_by_css(".revise").last.click();
            time.sleep(1)
            modalConfirm()
            time.sleep(5)
            modalConfirm()
        else:
            print("输入的车牌号不可见！！！")
    else:
        print("要验证的车牌号不存在！！！")
def activateCar(carNum):
    old=browser.find_by_text(carNum);
    if(len(old)>0):
        old=old.first;
        if(old.visible):
            m=browser.execute_script("$('p:contains(\""+carNum+"\")').parent().find('.carstate:visible').find('a:last').find('span').click()");
            time.sleep(1)
            modalConfirm()
            time.sleep(5)
            modalConfirm()
        else:
            print("输入的车牌号不可见！！！")
    else:
        print("要验证的车牌号不存在！！！")

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
# autoPayMachineTest({
#     'selfMacId':'1aca5a1fd245493scb124b38bfa96880d',
#     'toSearchCarNum':'晋BRQ444',
#     'phone':'19421025121',
#     'isExhangeAllTickets':False, #是否兑换所有停车券
#     'commonTicketsNum':6,   #兑换普通停车券的张数,
#     'isOld':True#是否老版本的缴费机（无会员积分系统）
# });

loginByPhone('18601965856');
go2MyCar();
# addCar("鲁A961T7",'blue')

# uptCar("苏B90878",'苏M10878','black')
# verifyCar("鲁A961T7",'A9ND03414','L6T7844SXAN044880')
activateCar("鲁A961T7")





