from app.routers import BaseModel, By, webdriver, APIRouter, status, HTTPException
from app.auth.auth import gerar_token
from app.config import options
from app.logging import logging

url_pagina_login = "https://practicetestautomation.com/practice-test-login/"

router = APIRouter(tags=["login"])

class FormUser(BaseModel):
    username : str
    password : str

@router.post("/login", status_code=status.HTTP_200_OK)
def login(user : FormUser):
    logging.info("Iniciou-se funcao de login de usuario")
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url_pagina_login)
        driver.implicitly_wait(0.5)
        form = driver.find_element(By.ID, "form")

        username_input = form.find_element(By.NAME, "username")
        username_input.send_keys(user.username)

        password_input = form.find_element(By.NAME, "password")
        password_input.send_keys(user.password)

        submit_button = form.find_element(By.ID, "submit")
        submit_button.click()

        driver.implicitly_wait(1)
        url_atual = driver.current_url

        driver.quit()

    except:
        logging.error("Erro ao automatizar navegador em funcoes com Selenium")
        raise HTTPException(status_code=500, detail="Erro ao automatizar navegador")

    if url_atual == url_pagina_login:
        logging.error("Credenciais invalidas de username ou password de usuario")
        raise HTTPException(status_code=401, detail="Credenciais inválidas") 
    
    token = gerar_token(user.username)

    logging.info("Finalizou-se funcção de login de usuario")
    return token