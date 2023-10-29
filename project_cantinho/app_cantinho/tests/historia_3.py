from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_browser = webdriver.Chrome(options=chrome_options)

class teste1(LiveServerTestCase):
        chrome_browser.get('http://127.0.0.1:8000/')
        email = chrome_browser.find_element(By.NAME, "email")
        senha = chrome_browser.find_element(By.NAME, "senha")
        email.send_keys("teste25@teste.com")
        senha.send_keys("123")
        entrar = chrome_browser.find_element(By.XPATH, "//button[@value='Entrar']")
        sleep(2)
        entrar.click()
        sleep(2)
        botoes_adicionar = chrome_browser.find_elements(By.CLASS_NAME, "add-to-cart")
        sleep(2)
        for botao in botoes_adicionar:
            botao.click()
            sleep(2)
        horario = chrome_browser.find_element(By.ID, 'hora_retirada')
        horario.send_keys('11:00')
        botao_salvar = chrome_browser.find_element(By.NAME, 'salvar_horario')
        botao_salvar.click()
        sleep(4)
