from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import random as rm
import time

url = 'https://twitter.com/login'

frases = ["frases aqui", "y aqui"]

def crear_driver():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(executable_path='la ubicacion de chromedriver.exe', options = options) #Puede contener algún Path.
    return browser


def navegador_logueo(browser, user_username, user_password):
    browser.get(url)
    browser.implicitly_wait(3)

    user = browser.find_element_by_name('session[username_or_email]')
    password = browser.find_element_by_name('session[password]')

    user.send_keys(user_username)

    password.send_keys(user_password)
    password.send_keys(Keys.ENTER)

    return browser

def twittear(browser, cadena):
    browser.implicitly_wait(3)
    tweet = browser.find_element_by_css_selector("br[data-text='true']")
    tweet.send_keys(cadena)
    button = browser.find_element_by_css_selector("div[data-testid='tweetButtonInline']")
    button.click()

def __main__(index):
    browser = crear_driver()
    cadena = f"[{index}] " + rm.choice(frases) + " frase"
    while True:
        try:
            browser = navegador_logueo(browser, "email" , "password")       
            try:
                twittear(browser, cadena)
                print('Tweet exitoso.')
                break
            except:
                print('Usuario o contraseña incorrectas.')
        except:
            print('Error login, reintentando.')          
    browser.close()


print('Iniciando.')
while True:
    with open ('contador','r') as archivo:
        index = archivo.read()
        print('Iniciando tweet.')
        __main__(index)
    with open ('contador','w') as archivo:
        archivo.write(str(int(index)+1))
    time.sleep(600)
        