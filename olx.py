from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep

options = Options()
#options.binary_location = "/usr/bin/firefox"
options.headless = False #Eu preciso ver a janela aberta até agora 

#perguntar qual o produto 
produto = input('Qual produto você quer pesquiar ?')


#Acessando o site 
driver = webdriver.Firefox(options=options)
driver.get(f"https://www.olx.com.br/estado-ce?q={produto}")
print(driver.title)
sleep(5)

#pegar os elementos:
produtos = driver.find_elements(By.XPATH,"//h2[@class='olx-text olx-text--body-large olx-text--block olx-text--semibold olx-adcard__title']")
precos = driver.find_elements(By.XPATH,"//h3[@class='olx-text olx-text--body-large olx-text--block olx-text--semibold olx-adcard__price']")
links = driver.find_elements(By.XPATH,"//a[@class='olx-adcard__link']")

for produto,preco,link in zip(produtos,precos,links):
    with open('resultado.csv','a',encoding='utf-8') as arquivo:
        arquivo.write(f'{produto.text},{preco.text},{link.get_attribute("href")}{os.linesep}')
input('')