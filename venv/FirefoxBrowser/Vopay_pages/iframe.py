import random
import time
import allure
import keyboard
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from resources.variables import bankName


class Iframe:
    URL= "https://dev2.vopay.com/iframe/new/outer.html"
    newURL = "https://dev2.vopay.com/iframe/new/outer.html"
    iframelink= (By.XPATH,"//body/center[1]/iframe[1]")
    iframelinkinner = (By.XPATH, "/html[1]/body[1]/center[1]/iframe[1]")
    loadmore= (By.XPATH,"//button[@id='load-more']")
    banklist= (By.XPATH,"//div[@class='bankList__Item ']")
    searchbar= (By.XPATH,"//input[@id='search-bar']")
    selectBank= (By.XPATH,"//img[@src='/images/logos-banks/98.svg']")
    proceedButton= (By.XPATH,"//button[@id='procced-bank']")
    onlinelBank =(By.XPATH,"//span[contains(text(),'Connect my Bank Online')]")
    connectonlinelBank = (By.XPATH, "//a[contains(text(),'Connect my Bank Online')]")
    manualBank = (By.XPATH, "//span[contains(text(),'Connect my Bank Manually')]")
    TermsOfuse= (By.XPATH,"//h1[contains(text(),'Terms of use')]")
    verifyonlinemsg= (By.XPATH,"//p[@class='bankflow__StepsText']")
    manualmsg= (By.XPATH,"//p[contains(text(),'Add your Bank Information')]")
    changemybank= (By.XPATH,"//a[@data-ember-action='665']")
    Linkyourbankheader= (By.XPATH,"//h1[@class='bankList__Header']")
    acceptTerms=(By.XPATH,"//span[@data-ember-action='661']")
    accepttermsamepage =(By.XPATH,"//a[@data-ember-action='853']")
    acceptProceed= (By.XPATH,"//button[@class='bank__Button bank__Button--big']")
    crossbutton = (By.XPATH,"//span[@class='cross']")
    # VopayTermslink= (By.XPATH,"//a[@data-ember-action='663']")
    VopayTermslink =(By.XPATH,"//a[contains(text(),'Terms of use')]")
    userTransit= (By.XPATH,"//input[@id='username']")
    passTransit= (By.XPATH,"//input[@id='password']")
    loginclick = (By.XPATH,"//button[@data-ember-action='1100']")
    # loginclick=(By.XPATH,"//button[contains(text(),'Proceed')]")
    chngbank=(By.XPATH,"//a[@id='change-bank']")
    Ques1= (By.XPATH,"//h1[@contains(text(),'What is the name of your childhood super hero?')]")
    ans= (By.XPATH,"//input[@id='anwser-question']")
    click= (By.XPATH,"//button[@data-ember-action='951']")
    searchicon = (By.XPATH,"//img[@src='images/search-ico.png']")
    nextpageUrl="http://portal-demo.vopay.com/#/login"



    def __init__(self, driver):
        self.driver= driver


    @allure.description('Launch outer url')
    def browser_load(self):
        self.driver.get(self.URL)
        self.driver.implicitly_wait(150)

    @allure.description('Switch to iframe')
    def switchtoiframe(self):
        time.sleep(6)
        frame= self.driver.find_element(*self.iframelink)
        self.driver.switch_to.frame(frame)

    def switchtoInnerIframe(self):
        time.sleep(6)
        frame= self.driver.find_element(*self.iframelinkinner)
        self.driver.switch_to.frame(frame)

    @allure.description('Click on LoadMore button')
    def verify_loadMore(self):
        time.sleep(3)
        load =self.driver.find_element(*self.loadmore)

        # load.click()
        try:
            for x in range(0, 6):
                # load.click()
                display = self.driver.find_element(*self.loadmore).is_displayed()
                if display==True:
                    load.click()

        except:
            return False

    @allure.step('Show all counts of bank')
    def showall_banklist(self):
        time.sleep(2)
        list= self.driver.find_elements(*self.banklist)
        bank= len(list)
        print(bank)

    @allure.step('Search Tanger Bank')
    def searchBank(self, bankName):
        time.sleep(3)
        self.driver.find_element(*self.searchbar).send_keys(bankName)
        time.sleep(4)

    @allure.description('Select Tanger Bank and click proceed button')
    def selectBankClick(self):
        self.driver.find_element(*self.selectBank).click()
        time.sleep(2)
        self.driver.find_element(*self.proceedButton).click()

    @allure.description('Verify msg for Manualbank page')
    def verify_manualmsg(self):
        manualmsg= self.driver.find_element(*self.manualmsg).text
        # verify= manualmsg.get_attribute('Name')
        print(manualmsg)
        return manualmsg


    def selectbankmethod_online(self):
        online= self.driver.find_element(*self.onlinelBank)
        online1= online.is_displayed()
        online.click()
        time.sleep(3)
        return online1

    @allure.description('Click on CoonectbankOnline link')
    def redirect_onlinebank(self):
        time.sleep(3)
        keyboard.press('pagedown')
        keyboard.press('pagedown')
        time.sleep(2)
        redirect= self.driver.find_element(*self.connectonlinelBank).text
        self.driver.find_element(*self.connectonlinelBank).click()
        time.sleep(3)
        return redirect


    def verify_manualBank(self):
        manual= self.driver.find_element(*self.manualBank)
        manualbank= manual.is_displayed()
        manual.click()
        time.sleep(3)
        return manualbank

    @allure.description('Accept Vopay Terms and policy')
    def AcceptVopayTerms(self):
        data = self.driver.find_element(*self.acceptTerms)
        time.sleep(2)
        try:
            checkbox = data.is_selected()
            if checkbox==False:
                data.click()

        except:
            print("checkbox not selected")


    def click_VopayTermslink(self):
        Terms = self.driver.find_element(*self.VopayTermslink).text
        time.sleep(2)
        self.driver.find_element(*self.VopayTermslink).click()
        time.sleep(3)
        self.driver.find_element(*self.crossbutton).click()
        try:
            checkbox = self.driver.find_element(*self.acceptTerms)
            data= checkbox.is_selected()
            if data==False:
                checkbox.click()
        except:
            data1=False
        return Terms


    @allure.description('Verify msg for bankOnlinepage')
    def verify_msg(self):
        change= self.driver.find_element(*self.verifyonlinemsg).text
        print(change)
        # change1 = change.is_displayed()
        return change

    @allure.description('Enter username in bankOnlinepage')
    def usernameTransit(self,user):
        self.driver.find_element(*self.userTransit).send_keys(user)
        time.sleep(2)

    @allure.description('enter password and click proceed in bankOnlinepage')
    def LoginTransit(self,pwd):
        actionchains = ActionChains(self.driver)
        self.driver.find_element(*self.passTransit).send_keys(pwd)
        time.sleep(2)
        # self.driver.find_element(*self.loginclick).click()

        try:
            login = self.driver.find_element(*self.acceptTerms)
            data= login.is_selected()
            if data == True:
                self.driver.find_element(*self.loginclick).click()

        except:
            # data= False
            self.driver.find_element(*self.acceptTerms).click()
            self.driver.find_element(*self.loginclick).click()

        # if data == True:
        #     login.click()

        self.driver.implicitly_wait(300)
        time.sleep(10)

    def ChooseQues(self,value):
        time.sleep(10)
        self.driver.find_element(*self.selectBank).is_displayed()
        time.sleep(3)
        self.driver.find_element(*self.ans).send_keys(value)
        time.sleep(2)
        self.driver.find_element(*self.click).click()
        self.driver.implicitly_wait(300)
        time.sleep(30)
        get= self.driver.current_url
        print(get)
        time.sleep(4)

    @allure.description('Open new tab and launch Vopay inner url')
    def switchwindow(self):
        time.sleep(2)
        self.driver.implicitly_wait(60)
        self.driver.execute_script("window.open('https://dev2.vopay.com/iframe/new/inner.html','new window')")
        print("open in new tab")
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        get= self.driver.current_url
        print(get)
        return get

    @allure.description('Open new tab and launch Vopay js url')
    def switchagain_jsbrowser(self):
        time.sleep(4)
        self.driver.execute_script("window.open('https://dev2.vopay.com/iframe/new/js.html','new window1')")
        time.sleep(3)
        print("open in new tab2")
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(3)
        get= self.driver.current_url
        print(get)
        return get

    def verify_changemybank(self):
        keyboard.press('pagedown')
        keyboard.press('pagedown')
        time.sleep(2)
        self.driver.find_element(*self.changemybank).click()
        time.sleep(5)
        # Linkyourbank= self.driver.find_element(*self.Linkyourbankheader).text
        # time.sleep(2)
        # return Linkyourbank


    def changebank_differpage(self):
        self.driver.find_element(*self.chngbank).click()
        search= self.driver.find_element(*self.searchicon).is_displayed()
        self.driver.find_element(*self.selectBank).click()
        time.sleep(2)
        self.driver.find_element(*self.proceedButton).click()
        time.sleep(3)

    def Accept_manualterms(self):
        try:
            checkbox = self.driver.find_element(*self.accepttermsamepage)
            data= checkbox.is_selected()
            if data==False:
                checkbox.click()
        except:
            data1=False
        # return Terms
        try:
            cross= self.driver.find_element(*self.crossbutton)
            button = cross.is_displayed()
            if button==True:
                cross.click()
        except:
            print("cross button not displayed")

