*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
Baidu search case
    Open Browser    http://www.baidu.com    chrome
    Input text    id=kw    robot framework
    sleep   5
    click button    id=su
    close Browser