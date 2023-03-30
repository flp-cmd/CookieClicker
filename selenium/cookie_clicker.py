from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CookieClicker:
    def __init__(self):
        self.SITE_LINK = 'https://orteil.dashnet.org/cookieclicker/'
        self.SITE_MAP = {"botoes":{
                         "biscoito":{
                            "xpath": '/html/body/div/div[2]/div[15]/div[8]/button'
                         },
                         "lingua":{
                            "xpath": "/html/body/div/div[2]/div[12]/div/div[1]/div[1]/div[2]"
                         },
                         "upgrade":{
                            "xpath": "/html/body/div/div[2]/div[19]/div[3]/div[6]/div[$$NUMBER$$]"
                         }
                    }
                }

        self.driver = webdriver.Chrome(executable_path="C:\\Webdriver\\chromedriver.exe")
        self.driver.maximize_window()

    def abrirSite(self):
        self.driver.get(self.SITE_LINK)
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.SITE_MAP['botoes']['lingua']['xpath']).click()
        time.sleep(5)
        i = 0
        while True:
            if i % 500 == 0 and i != 0:
                time.sleep(1)
                self.compraUpgrade()
                time.sleep(1)
            self.clicaCookie()
            i += 1


    def clicaCookie(self):
        self.driver.find_element(By.XPATH,self.SITE_MAP['botoes']['biscoito']['xpath']).click()

    def pegaMelhorUpgrade(self):
        encontrei = False
        elementoAtual = 2

        while not encontrei:
            objeto = self.SITE_MAP["botoes"]["upgrade"]["xpath"].replace("$$NUMBER$$",str(elementoAtual))
            classeObjeto = self.driver.find_element(By.XPATH,objeto).get_attribute("class")

            if not "enabled" in classeObjeto:
                encontrei = True
            else:
                elementoAtual += 1
        return elementoAtual - 1

    def compraUpgrade(self):
        objeto = self.SITE_MAP["botoes"]["upgrade"]["xpath"].replace("$$NUMBER$$",str(self.pegaMelhorUpgrade()))
        self.driver.find_element(By.XPATH,objeto).click()

cookie = CookieClicker()
cookie.abrirSite()


