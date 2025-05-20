from app.routers import APIRouter, uuid, Depends, Annotated, FileResponse
from app.crud.crud import get_ncm_by_id, delete_ncm, get_ncms_by_page
from app.auth.auth import get_current_user, User
from app.export.export import preencher_planilha

router = APIRouter(prefix="/ncm-results", tags=["ncm-results"])

@router.get("")
def get_ncms_paged(skip : int, limit : int, current_user : Annotated[User, Depends(get_current_user)]):
    ncms_list = get_ncms_by_page(skip, limit)
    return ncms_list

@router.get("/export")
async def export_ncm_entries_data(current_user : Annotated[User, Depends(get_current_user)]):
    planilha = preencher_planilha()
    
    return FileResponse(path=planilha, filename="planilha.xlsx",  media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

@router.get("/{ncm_id}")
def search_ncm_by_id(ncm_id : uuid.UUID, current_user : Annotated[User, Depends(get_current_user)]):
    ncm_buscado = get_ncm_by_id(ncm_id)
    return ncm_buscado if ncm_buscado != None else {"erro" : "não há registro com esse id"}

@router.delete("/{ncm_id}")
def delete_ncm_by_id(ncm_id : uuid.UUID, current_user : Annotated[User, Depends(get_current_user)]):
    delete_ncm(ncm_id)
    return {"Item deletado com sucesso"}
