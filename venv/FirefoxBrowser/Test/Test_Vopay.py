import time
import allure
from Vopay_pages import iframe
from Vopay_pages.Flinkspages import Flinkspages
from Vopay_pages.iframe import Iframe
from resources.variables import *
from selenium import webdriver

"""Vopay Iframe URL"""

"""Outer Html page"""

@allure.suite('Vopay')
@allure.title('Launch vopay iframe outer page')
def test_cases(browser):
    global launch
    launch = Iframe(browser)
    launch.browser_load()
    launch.switchtoiframe()


#
# @allure.title('To loadmore banks and get counts of all bank')
# def test_countbank(browser):
#     assert launch.verify_loadMore()==False,"Proceed not displayed"
#     launch.showall_banklist()

@allure.suite('Vopay')
@allure.title('User is able to search and select bank')
def test_selectbank(browser):
    global launch1
    launch1 = Flinkspages(browser)
    launch.searchBank(bankName)
    assert launch1.selectBankClick() == True, "bank not displayed"



@allure.title('User is able to click manual bank link and redirect properly')
def test_verify_manualBanklink(browser):
    assert launch.verify_manualBank()==True,"manual link not displayed"
    assert launch.verify_manualmsg()=='Add your Bank Information', "not matched"
    launch.Accept_manualterms()

@allure.title('User is able to click online bank link and select checkbox')
def test_verify_onlinBanklink(browser):
    assert launch.redirect_onlinebank()=='Connect my Bank Online', "not matched"
    launch.AcceptVopayTerms()

#
# @allure.title('User is able to click change my bank link and redirect properly to search Bank page')
# def test_Clickchangebanklink(browser):
#     assert launch.verify_msg() == 'Enter Your Credentials', "online bank credential tab not displayed"
#     launch.verify_changemybank()
#     assert launch1.selectBankClick()== True, "tanger not displayed"
#
#
#
# @allure.title('Click chngmybank in secure accountpage and To accept Vopay Terms in credentail page')
# def test_acceptterms(browser):
#     launch.changebank_differpage()
#     assert launch.selectbankmethod_online()== True, "selected bank not changed"
#     launch.AcceptVopayTerms()
#
#
# @allure.title('Verify conditions link(terms) is working and User can only access the "Proceed" button if all required fields are informed')
# def test_VopayTerms(browser):
#     assert launch.click_VopayTermslink()=='Terms of use',"Vopay terms not opened"
#     assert launch.verify_msg() == 'Enter Your Credentials', "online bank credential tab not displayed"
#     launch.usernameTransit(user)
#     launch.LoginTransit(pwd)
#     # launch.ChooseQues(value)
#
#
# """Inner URL(Vopay)"""
#
# @allure.title('User is able to open new tab in the same browser and load INNER URL')
# def test_newtab(browser):
#     assert launch.switchwindow()=='https://dev2.vopay.com/iframe/new/inner.html',"New tab not opened with inner url"
#     launch.switchtoInnerIframe()
#
#
# @allure.title('To loadmore banks and get counts of all bank(INNER URL)')
# def test_countbank_inner(browser):
#         assert launch.verify_loadMore()==False,"Proceed not displayed"
#         launch.showall_banklist()
#
# @allure.title('User is able to searchbank and select bank(INNER URL)')
# def test_selectbank_inner(browser):
#         global launch1
#         launch1 = Flinkspages(browser)
#         launch.searchBank(bankName)
#         assert launch1.selectBankClick() == True, "bank not displayed"
#
# @allure.title('User is able to click manual bank link and redirect properly(INNER URL)')
# def test_verify_manualBanklink_inner(browser):
#         assert launch.verify_manualBank() == True, "manual link not displayed"
#         assert launch.verify_manualmsg() == 'Add your Bank Information', "not matched"
#         launch.Accept_manualterms()
#
# @allure.title('User is able to click online bank link and select checkbox(INNER URL)')
# def test_verify_onlinBanklink_inner(browser):
#         assert launch.redirect_onlinebank() == 'Connect my Bank Online', "not matched"
#         launch.AcceptVopayTerms()
#
# @allure.title('User is able to click change my bank link and redirect properly to search Bank page(INNER URL)')
# def test_Clickchangebanklink_inner(browser):
#         assert launch.verify_msg() == 'Enter Your Credentials', "online bank credential tab not displayed"
#         launch.verify_changemybank()
#         assert launch1.selectBankClick() == True, "tanger not displayed"
#
# @allure.title('Click chngmybank in secure accountpage and To accept Vopay Terms in credentail page(INNER URL)')
# def test_acceptterms_inner(browser):
#         launch.changebank_differpage()
#         assert launch.selectbankmethod_online() == True, "selected bank not changed"
#         launch.AcceptVopayTerms()
#
# @allure.title('Verify conditions link(terms) is working and User can only access the "Proceed" button if all required fields are informed(INNER URL)')
# def test_VopayTerms_inner(browser):
#         assert launch.click_VopayTermslink() == 'Terms of use', "Vopay terms not opened"
#         assert launch.verify_msg() == 'Enter Your Credentials', "online bank credential tab not displayed"
#         launch.usernameTransit(user)
#         launch.LoginTransit(pwd)
#         # launch.ChooseQues(value)
#
#
# """JS URL(Vopay)"""
#
# @allure.title('User is able to open new tab2 in the same browserr and load JS url')
# def test_newtab_js_sameoperation(browser):
#     assert launch.switchagain_jsbrowser()=='https://dev2.vopay.com/iframe/new/js.html',"wrong url"
#     launch.switchtoiframe()
#
#
# @allure.title('To loadmore banks and get counts of all bank(JS URL)')
# def test_countbank_js(browser):
#         assert launch.verify_loadMore()==False,"Proceed not displayed"
#         launch.showall_banklist()
#
# @allure.title('User is able to searchbank and select bank(JS URL)')
# def test_selectbank_js(browser):
#         global launch1
#         launch1 = Flinkspages(browser)
#         launch.searchBank(bankName)
#         assert launch1.selectBankClick() == True, "bank not displayed"
#
# @allure.title('User is able to click manual bank link and redirect properly(JS URL)')
# def test_verify_manualBanklink_js(browser):
#         assert launch.verify_manualBank() == True, "manual link not displayed"
#         assert launch.verify_manualmsg() == 'Add your Bank Information', "not matched"
#         launch.Accept_manualterms()
#
# @allure.title('User is able to click online bank link and select checkbox(JS URL)')
# def test_verify_onlinBanklink_js(browser):
#         assert launch.redirect_onlinebank() == 'Connect my Bank Online', "not matched"
#         launch.AcceptVopayTerms()
#
# @allure.title('User is able to click change my bank link and redirect properly to search Bank page(js URL)')
# def test_Clickchangebanklink_js(browser):
#         assert launch.verify_msg() == 'Enter Your Credentials', "online bank credential tab not displayed"
#         launch.verify_changemybank()
#         assert launch1.selectBankClick() == True, "tanger not displayed"
#
#
# @allure.title('Click chngmybank in secure accountpage and To accept Vopay Terms in credentail page(JS URL)')
# def test_acceptterms_js(browser):
#         launch.changebank_differpage()
#         assert launch.selectbankmethod_online() == True, "selected bank not changed"
#         launch.AcceptVopayTerms()
#
# @allure.title('Verify conditions link(terms) is working and User can only access the "Proceed" button if all required fields are informed(JS URL)')
# def test_VopayTerms_js(browser):
#         assert launch.click_VopayTermslink() == 'Terms of use', "Vopay terms not opened"
#         assert launch.verify_msg() == 'Enter Your Credentials', "online bank credential tab not displayed"
#         launch.usernameTransit(user)
#         launch.LoginTransit(pwd)
#         # launch.ChooseQues(value)
#
#
# """Flinks URL"""
# """Outer url"""
#
# @allure.title('To open newtab3 and Hide redLine in flinks url')
# def test_FlinkpageURL_newbrowser(browser):
#     assert launch1.switchagain_oldouter()=='https://dev2.vopay.com/iframe/old/outer.html', "URL not matched"
#     launch1.switchtoiframe()
#     assert launch1.VerifyonHide()==False,"Hide button not working"
#
#
# @allure.title('switch to iframe again and search tan Bank')
# def test_searchbankFlinkURLr(browser):
#     launch1.refreshpage()
#     launch1.switchtoiframe()
#     assert launch1.switchtoiframe2()==True,"Hidebutton not display"
#     assert launch1.searchBank1(TanName)==True,"Tan Bank not display"
#
#
# @allure.title('select bank and naviagate agree and continue')
# def test_selectbankFlinkURLr(browser):
#     assert launch1.selectTan_flink()=="Click 'AGREE and CONTINUE' to allow username test to proceed.","Agree and continue page not displayed"
#     assert launch1.verifyAgreepage()=='Access your account number', "text not matched"
#
#
# @allure.title('verify text on agree page and click on cancel button page redirected to HomePage ')
# def test_verifyText_AgreeContinuePage(browser):
#     time.sleep(2)
#     assert launch1.verifyTextAgree()=='Access your account transaction history',"text not matched"
#     assert launch1.verifyTextAgree2()=='Access your name, email, address and phone number',"text not matched"
#     assert launch1.ClickCancelbutton()=='Connect with your bank',"page not redirected to homepage"
#
#
# @allure.title('Click AgreeContinue button navigate to login page and click on back arrow on loginpage back to homepage')
# def test_RedirectLoginPage(browser):
#     launch1.selectTan_flink()
#     assert launch1.Click_agreeButton()==True,"Tangerine Logo not displayed on Agreecontinue page "
#     assert launch1.clickonBackarrow()=='Connect with your bank',"page not redirected to homepage"
#     assert launch1.search_flinknamedBank(flinkName)==True,"Flink bank not display"
#
#
# @allure.title('Validate username and password with invalid credentails')
# def test_Validate_UserandPass_invalid(browser):
#     launch1.Click_agreeButton()
#     launch1.verifyinvalidusername(invalidUser)
#     launch1.verifyinvalidPass(invalidPass)
#     assert launch1.loginFlinks()==True,"submit button disabled"
#     assert launch1.Clickretrybutton()==True,"button not displayed"
#
#
# @allure.title('Validate username and password with more comination')
# def test_Validate_UserandPass(browser):
#     launch1.verifyvalidusername(validuser)
#     launch1.verifyinvalidPass(invalidPass)
#     assert launch1.loginFlinks()==True,"submit button disabled"
#     assert launch1.Clickretrybutton()==True, "invalid login"
#     time.sleep(3)
#
# @allure.title('Validate invalidusername and valid password ')
# def test_Validate_invalidUser_validPass(browser):
#     launch1.verifyinvalidusername(invalidUser)
#     launch1.verifyvalidpass(validpass)
#     assert launch1.loginFlinks()==True,"submit button disabled"
#     assert launch1.Clickretrybutton()==True, "invalid login"
#
#
# @allure.title('Click on resetpass and get url to redirected page')
# def test_ClickresetPass(browser):
#     launch1.verifyvalidusername(validuser)
#     launch1.verifyvalidpass(validpass)
#     assert launch1.Clickresetpassword_button()=='https://flinks.io/',"navigate wrong url"
#
#
# @allure.title('login with valid credentail and login succesfully')
# def test_Afterlogin_verify(browser):
#     launch1.switchtab()
#     launch1.switchtoiframe()
#     launch1.switchtoiframe2()
#     launch1.search_flinknamedBank(flinkName)
#     launch1.Click_agreeButton()
#     launch1.verifyvalidusername(validuser)
#     launch1.verifyvalidpass(validpass)
#     assert launch1.loginFlinks()==True,"submit button disabled"
#
# @allure.title('User provide invalid security question')
# def test_Verify_invalidsecurity(browser):
#     launch1.verify_invalidsecurityans()
#     time.sleep(2)
#     assert launch1.verify_invalidsecurityans()=='Invalid answer',"answer correct"
#
# @allure.title('User provide valid security question and click continue to account select')
# def test_validsecurity(browser):
#     launch1.verify_security()
#     assert launch1.selectAccount()=='Please select an account',"invalid security"
#
# @allure.title('To verify the outer redirect')
# def test_verifyouterredirect(browser):
#     assert launch1.verify_outertoken() == True, "token not display"
#
#
#     # @allure.title('Cliick on simulate login and verify the token ')
#     # def test_verifyToken_Onsimulateclick(browser):
#     #     assert launch1.Clicksimulatebutton()=='Thank You!',"Token page not reached"
#     #     assert launch1.verify_token()==True,"token not display"


"""Inner url (Flinks)"""

@allure.suite('test tag part1')
@allure.title('inner url')
def test_Flinkinnerurl_newbrowser(browser):
    assert launch1.switchwindow_oldjs() == 'https://dev2.vopay.com/iframe/old/js.html', "URL not matched"
    # launch1.switchtoiframe()
    # assert launch1.VerifyonHide()==False,"Hide button not working"


@allure.suite('test tag part1')
@allure.title('inner 3 url')
def test_searchbankFlinkURL_inner(browser):
    launch1.refreshpage()
    launch1.switchtoiframe()
    assert launch1.switchtoiframe2() == True, "Hidebutton not display"
    assert launch1.searchBank1(TanName) == True, "Tan Bank not display"



@allure.title('select bank and naviagate agree and continue page(Inner url)')
def test_selectbankFlinkURL_inner(browser):
    assert launch1.selectTan_flink() == "Click 'AGREE and CONTINUE' to allow application to proceed.", "Agree and continue page not displayed"
    assert launch1.verifyAgreepage() == 'Access your account number', "text not matched"


@allure.title('verify text on agree page and click on cancel button page redirected to HomePage(Inner url) ')
def test_verifyText_AgreeContinuePage_inner(browser):
    time.sleep(2)
    assert launch1.verifyTextAgree()=='Access your account transaction history',"text not matched"
    assert launch1.verifyTextAgree2()=='Access your name, email, address and phone number',"text not matched"
    assert launch1.ClickCancelbutton()=='Connect with your bank',"page not redirected to homepage"
#
#
#
# @allure.title(
#     'Click AgreeContinue button navigate to login page and click on back arrow on loginpage back to homepage(Inner url)')
# def test_RedirectLoginPage_inner(browser):
#     launch1.selectTan_flink()
#     assert launch1.Click_agreeButton() == True, "Logo not displayed on Agreecontinue page "
#     assert launch1.clickonBackarrow() == 'Connect with your bank', "page not redirected to homepage"
#     assert launch1.search_flinknamedBank(flinkName) == True, "Flink bank not display"
#     #
#     #
#     # @allure.title('Validate username and password with invalid credentails(Inner url)')
#     # def test_Validate_UserandPass_invalid_inner(browser):
#     #     launch1.Click_agreeButton()
#     #     launch1.verifyinvalidusername(invalidUser)
#     #     launch1.verifyinvalidPass(invalidPass)
#     #     assert launch1.loginFlinks() == True, "submit button disabled"
#     #     assert launch1.Clickretrybutton() == True, "button not displayed"
#     #
#     #
#     # @allure.title('Validate username and password with more comination(Inner URl)')
#     # def test_Validate_UserandPass_inner(browser):
#     #     launch1.verifyvalidusername(validuser)
#     #     launch1.verifyinvalidPass(invalidPass)
#     #     assert launch1.loginFlinks()==True,"submit button disabled"
#     #     assert launch1.Clickretrybutton()==True, "invalid login"
#     #     time.sleep(3)
#     #
#     # @allure.title('Validate invalidusername and valid password (Inner URl)')
#     # def test_Validate_invalidUser_validPass_inner(browser):
#     #     launch1.verifyinvalidusername(invalidUser)
#     #     launch1.verifyvalidpass(validpass)
#     #     assert launch1.loginFlinks()==True,"submit button disabled"
#     #     assert launch1.Clickretrybutton()==True, "invalid login"
#     #
#     #
#     # @allure.title('Click on resetpass and get url to redirected page(Inner Url)')
#     # def test_ClickresetPass_inner(browser):
#     #     launch1.verifyvalidusername(validuser)
#     #     launch1.verifyvalidpass(validpass)
#     #     assert launch1.Clickresetpassword_button_inner()=='https://flinks.io/',"navigate wrong url"
#     #
#     #
#     #
#     # @allure.title('login with valid credentail and login succesfully(Inner URl)')
#     # def test_Afterlogin_verify_inner(browser):
#     #     launch1.switchtabinner()
#     #     launch1.switchtoiframe()
#     #     launch1.switchtoiframe2()
#     #     launch1.search_flinknamedBank(flinkName)
#     launch1.Click_agreeButton()
#     launch1.verifyvalidusername(validuser)
#     launch1.verifyvalidpass(validpass)
#     assert launch1.loginFlinks() == True, "submit button disabled"
#
#
# @allure.title('User provide invalid security question(Inner URl)')
# def test_Verify_invalidsecurity_inner(browser):
#     launch1.verify_invalidsecurityans()
#     time.sleep(2)
#     # assert launch1.verify_invalidsecurityans()=='Invalid answer',"answer correct"
#
#
# @allure.title('User provide valid security question and click continue to account select(Inner URl)')
# def test_validsecurity_inner(browser):
#     launch1.verify_security()
#     assert launch1.selectAccount() == 'Please select an account', "invalid security"
#
#
# @allure.title('To verify the inner redirect(Inner URl)')
# def test_verifyJSredirect(browser):
#     time.sleep(3)
#     launch1.switchtoiframesimulate()
#     # launch1.JS_tokenvalue()
#     launch1.check_errors_console_log()
#     # launch1.get_browser_console_log()
#     # assert launch1.verify_jstoken()==True,"Token inner not verified"

#
# @allure.title('Click on simulate login and verify the token(Inner URl) ')
# def test_verifyToken_Onsimulateclick_inner(browser):
#     assert launch1.Clicksimulatebutton() == 'og88s44wgswc4gwc4oc00s08kskgw0www440ok8ko44c40c480kcsk8okk480css', "Token page not reached"
#     assert launch1.verify_token()==True,"Token inner not verified"
#
#
