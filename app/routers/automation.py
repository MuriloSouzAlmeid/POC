from app.routers import APIRouter, webdriver, By, BaseModel, datetime, Annotated, Depends
from app.config import options
from app.auth.auth import User, get_current_user 
from app.crud.crud import create_ncm_rentrie
from datetime import datetime, timedelta, timezone


class Ncms_List(BaseModel):
    ncms : list[str] = []

class Ncm_Item(BaseModel):
    user : str
    ipi : str | None = None
    ncm : str
    description : str


router = APIRouter(tags=["automation"], prefix="/ncm")

@router.post("/start-automation")
def start_automation(ncms_list : Ncms_List, current_user: Annotated[User, Depends(get_current_user)]):
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.contabilizei.com.br/contabilidade-online/ncm/")
    table = driver.find_elements(By.TAG_NAME, "tr")
    
    table_list = []

    for i in range(1, len(table)):
        table_row = table[i].find_elements(By.TAG_NAME, "td")

        if len(ncms_list.ncms) == 0 or table_row[1].text in ncms_list.ncms:
            ncm = Ncm_Item(user=current_user.sub, ipi=table_row[0].text, ncm=table_row[1].text, description=table_row[2].text)
            table_list.append(ncm)

    for item_list in table_list:
        create_ncm_rentrie(item_list.user, item_list.ipi, item_list.ncm, item_list.description, datetime.now().astimezone(timezone(timedelta(hours=-3))))

    driver.quit()

    return {"Cadastrado"}