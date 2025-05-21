from app.routers import APIRouter, uuid, Depends, Annotated, FileResponse, HTTPException
from app.crud.crud import get_ncm_by_id, delete_ncm, get_ncms_by_page
from app.auth.auth import get_current_user, User
from app.export.export import preencher_planilha
from app.logging import logging

router = APIRouter(prefix="/ncm-results", tags=["ncm-results"])

@router.get("", status_code=200)
def get_ncms_paged(skip : int, limit : int, current_user : Annotated[User, Depends(get_current_user)]):
    logging.info("Iniciou-se operacao de busca de ncms paginada")
    ncms_list = get_ncms_by_page(skip, limit)
    logging.info("Finalizou-se operacao de busca de ncms paginada")
    return ncms_list

@router.get("/export", status_code=200, tags=["export-data"])
async def export_ncm_entries_data(current_user : Annotated[User, Depends(get_current_user)]):
    logging.info("Iniciou-se operacao de exportacao da tabela ncm_entries para arquivo .xlsx")
    try:
        planilha = preencher_planilha()
    except:
        logging.error("Ocorreu um erro na operacao de exportar arquivo .xlsx")
        raise HTTPException(status_code=400, detail="Erro ao exportar arquivo de planilha")
    
    logging.info("Fizalizou-se operacao de exportação da tabela ncm_entries para arquivo .xlsx")
    return FileResponse(path=planilha, filename="planilha.xlsx",  media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

@router.get("/{ncm_id}", status_code=200)
def search_ncm_by_id(ncm_id : uuid.UUID, current_user : Annotated[User, Depends(get_current_user)]):
    logging.info("Iniciou-se operacao de busca de ncm por ID informado")
    ncm_buscado = get_ncm_by_id(ncm_id)

    if ncm_buscado == None:
        logging.error("Nao foi encontrado ncm com ID fornecido como parametro")
        raise HTTPException(status_code=404, detail="Não encontrado")

    logging.info("Fizalizou-se operacao de busca de ncm por ID informado")
    return ncm_buscado

@router.delete("/{ncm_id}", status_code=204)
def delete_ncm_by_id(ncm_id : uuid.UUID, current_user : Annotated[User, Depends(get_current_user)]):
    logging.info("Iniciou-se operacao de remocao de ncm por ID informado")
    ncm_buscado = get_ncm_by_id(ncm_id)

    if ncm_buscado == None:
        logging.error("Nao foi encontrado ncm com ID fornecido como parametro")
        raise HTTPException(status_code=404, detail="Não encontrado")

    delete_ncm(ncm_id)

    logging.info("Fizalizou-se operacao de remocao de ncm por ID informado")
    return {"message" : "Item deletado com sucesso"}
