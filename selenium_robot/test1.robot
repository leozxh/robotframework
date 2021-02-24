*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
Cxm caiwu login
    Open Browser    http://test.mmp-new.caixm.cn/    chrome
    Input text    id:userName    15868134428
    sleep   2
    Input text    id:password    232323
    sleep   2
    click button    xpth://*[@id="root"]/div/div[2]/div[2]/div/form/div[3]/div/div/span/button
#    close Browser