from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Abrindo o navegador
driver = webdriver.Chrome()# Usa o ChromeDriver

# 2. Acesse o site
driver.get("https://www.saucedemo.com")

# 3. Localiza os campos de Login
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")

# 4. Preenche o login
username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")

# 5. Clica no botão de login
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# 6. Definindo segundos ( para verificar o resultado )
time.sleep(5)

# 7. Verificando se logou com sucessos
assert "inventory" in driver.current_url
print ("Login realizado com sucesso")
