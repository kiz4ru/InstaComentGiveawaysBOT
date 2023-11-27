import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


ASCII = '''
\n\n
██ ▄█▀ ██▓▒███████▒ ██▀███   █    ██ 
 ██▄█▒ ▓██▒▒ ▒ ▒ ▄▀░▓██ ▒ ██▒ ██  ▓██▒
▓███▄░ ▒██▒░ ▒ ▄▀▒░ ▓██ ░▄█ ▒▓██  ▒██░
▓██ █▄ ░██░  ▄▀▒   ░▒██▀▀█▄  ▓▓█  ░██░
▒██▒ █▄░██░▒███████▒░██▓ ▒██▒▒▒█████▓ 
▒ ▒▒ ▓▒░▓  ░▒▒ ▓░▒░▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ 
░ ░▒ ▒░ ▒ ░░░▒ ▒ ░ ▒  ░▒ ░ ▒░░░▒░ ░ ░ 
░ ░░ ░  ▒ ░░ ░ ░ ░ ░  ░░   ░  ░░░ ░ ░ 
░  ░    ░    ░ ░       ░        ░     
           ░
\n\n\n\t\t\t\t\t\t\t\t\tCreated by: kiz4ru\n\n\n
'''

print(ASCII)

# Configura las opciones para usar Chrome en modo sin cabeza
options = Options()
options.add_argument("--headless")

# Inicia el navegador en modo sin cabeza
driver = webdriver.Chrome(options=options)


# Lee las configuraciones
config = configparser.ConfigParser()
config.read('config.ini')

# Configura y lanza el navegador
options = Options()
options.headless = config.getboolean('Browser', 'headless')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Navega a Instagram y inicia sesión
driver.get('https://www.instagram.com/')
# Aquí va el código para iniciar sesión...
username = driver.find_element(By.NAME, 'username')
username.send_keys(config['Credentials']['username'])
password = driver.find_element(By.NAME, 'password')
password.send_keys(config['Credentials']['password'])
login = driver.find_element(By.XPATH, '//button[@type="submit"]')
login.click()


# Navega a la página de seguidores y recoge los nombres de usuario
# Aquí va el código para recoger los nombres de usuario...
followers = driver.find_elements(By.XPATH, '//div[@class="username"]/a')
usernames = [follower.text for follower in followers]

# Navega a la página de la publicación y publica comentarios
# Aquí va el código para publicar comentarios...

# Navega a la página de la publicación
driver.get('https://www.instagram.com/p/POST_ID/')  # Reemplaza POST_ID con el ID de tu publicación

# Publica comentarios
for username in usernames:
    comment_box = driver.find_element(By.XPATH, '//textarea[@aria-label="Añade un comentario..."]')
    comment_box.click()
    comment_box = driver.find_element(By.XPATH, '//textarea[@aria-label="Añade un comentario..."]')
    comment_box.clear()
    comment = f'Hola @{username}, participa en este sorteo!'
    comment_box.send_keys(comment)
    comment_box.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)

