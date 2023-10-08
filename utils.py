from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

class Automacao:
    def __init__(self,jogo):
        self.jogo = jogo
        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service)

    def busca_jogo(self,url, xpath_input_busca, class_name_nome_jogo, class_name_preco_jogo, xpath_filtro=None,steam=None):
        caracteres_especiais = ['™','™:',':','®','Preço p/ você:','-']

        self.browser.get(url)
        input_busca = self.browser.find_element('xpath', xpath_input_busca)
        input_busca.send_keys(self.jogo)
        input_busca.send_keys(Keys.ENTER)

        if (xpath_filtro):
            filtro = self.browser.find_element('xpath','//*[@id="additional_search_options"]/div[1]/div[2]/div[4]/span/span/span[1]')
            filtro.click()

            sleep(2)

        lista = []

        nome_jogo = self.browser.find_elements(By.CLASS_NAME, class_name_nome_jogo)
        preco_jogo = self.browser.find_elements(By.CLASS_NAME, class_name_preco_jogo)

        for jogo, preco in zip(nome_jogo, preco_jogo):
            nome = jogo.text
            for i in caracteres_especiais:
                nome = nome.replace(i, '')
            nome = nome.replace('The Definitive Edition','Edição Definitiva')
            lista.append({'nome': nome, 'preco': preco.text})

        return lista

    def fecha_navegador(self):
        self.browser.close()
        self.browser.quit()