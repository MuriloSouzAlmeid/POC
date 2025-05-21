from app.routers import APIRouter, webdriver, By, BaseModel, datetime, Annotated, Depends, HTTPException
from app.config import options
from app.auth.auth import User, get_current_user 
from app.crud.crud import create_ncm_entrie
from datetime import datetime, timedelta, timezone
from app.logging import logging

class Ncms_List(BaseModel):
    ncms : list[str] = []

class Ncm_Item(BaseModel):
    user : str
    ipi : str | None = None
    ncm : str
    description : str


router = APIRouter(tags=["automation"], prefix="/ncm")

@router.post("/start-automation", 
             status_code=201, 
             response_description="Ncms gravados na tabela com sucesso")
def start_automation(ncms_list : Ncms_List, current_user: Annotated[User, Depends(get_current_user)]):
    logging.info("Iniciou-se operacao de busca e registro de ncms na tabela ncm_entries")
    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.contabilizei.com.br/contabilidade-online/ncm/")
        table = driver.find_elements(By.TAG_NAME, "tr")
    
        table_list = []

        for i in range(1, len(table)):
            table_row = table[i].find_elements(By.TAG_NAME, "td")

            if len(ncms_list.ncms) == 0 or table_row[1].text in ncms_list.ncms:
                ncm = Ncm_Item(user=current_user.sub, ipi=table_row[0].text, ncm=table_row[1].text, description=table_row[2].text)
           
                table_list.append(ncm)
        
        driver.quit()
    except:
        logging.error("Ocorreu um erro ao acessar e salvar dados da tabela ncm com a ferramenta Selenium")
        raise HTTPException(status_code=500, detail="Erro ao automatizar navegador")

    for item_list in table_list:
        ncm = create_ncm_entrie(item_list.user, item_list.ipi, item_list.ncm, item_list.description, datetime.now().astimezone(timezone(timedelta(hours=-3))))

    logging.info("Iniciou-se operacao de busca e registro de ncms na tabela ncm_entries")
    return {"ncms registrados" : table_list}