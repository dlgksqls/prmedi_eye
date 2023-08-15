from selenium import webdriver
from selenium.webdriver.common.by import By


def medi_selenium(name):
    driver = webdriver.Chrome()
    driver.get('https://www.health.kr/main.asp')

    