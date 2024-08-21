import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


_options = Options()
#_options.add_argument('--headless') --Para O Navegador Não Aparecer na Tela
#_options.add_argument('window-size=800,800')

_browser = webdriver.Chrome(options=_options)
_browser.get('https://www.med4.com.br/')

#Aqui Está o Segredo, Colocar um Sleep Para Deixar A Página fazer Todas as Requisições e Depois Trazer o HTML
sleep(3)

wait = WebDriverWait(_browser, 10)
_inputSearch = _browser.find_element(By.CLASS_NAME, 'js-search-input')
_inputSearch.send_keys('Creme')
sleep(1)
_inputSearch.submit()

_product_link = _browser.find_element(By.CSS_SELECTOR, '.js-item-product .item-link')
_product_link.click()

#Pegar O Conteúdo HTML e Passar Para o BeaufifulSoup
_site = BeautifulSoup(_browser.page_source, 'html.parser')


_productName = _site.select_one('h1.js-product-name')
if _productName:
    print('Produto: ', _productName.text.strip())

_productPrice = _site.select_one('h2.js-price-display')
if _productPrice:
    print(f'Preço:', _productPrice.text.strip())

sleep(3)

input('Deseja Comprar?')
_zip_code = input('Digite o CEP:')

_addCar = _browser.find_element(By.CSS_SELECTOR, '.js-addtocart')
_addCar.click()

_cart_link = _browser.find_element(By.ID, 'ajax-cart')
_cart_link.click()

_zipcode_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.js-shipping-input[name="zipcode"]')))
_zipcode_input.send_keys(_zip_code) 
_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="go_to_checkout"]')))
_checkout_button.click()

input("Pressione Enter para fechar o navegador...")
_browser.quit()
