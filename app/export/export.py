from app.export import openpyxl, Session, select, opxl_styles, get_column_letter, HTTPException
from app.models.models import engine, NcmEntries
from app.logging import logging

def configurar_planilha(file : str):
    workbook = workbook = openpyxl.load_workbook(file)
    workbook.remove(workbook.active)

    workbook.create_sheet("Ncms Entries")
    planilha = workbook.active

    planilha_head = ["ID", "IPI", "NCM", "Descrição", "DATA"]

    planilha.append(planilha_head)

    # deixa o cabeçalho em negrito
    for celula in planilha[1]:
        celula.font = opxl_styles.Font(bold=True)

    workbook.save(file)

    return workbook

def preencher_planilha():
    file_path = "./app/planilha.xlsx"
    workbook = configurar_planilha(file_path)
    planilha = workbook.active

    try:
        with Session(engine) as session:
            query = select(NcmEntries).order_by(NcmEntries.created_at.desc())
            ncms_list = session.exec(query)

            #armazena os valores máximos das colunas
            column_widths = 5*[0]

            for ncm in ncms_list:
                linha_planilha = [str(ncm.id), ncm.ipi, ncm.ncm, ncm.description, str(ncm.created_at)]
                planilha.append(linha_planilha)

                #preenche column_widths com os valores máximos das colunas
                for i in range(len(linha_planilha)):
                    column_widths[i] = max(column_widths[i], len(linha_planilha[i]))
    except:
        logging.error("Ocorreu um erro ao buscar os dados da tabela ncm_entries")
        raise HTTPException(status_code=500, detail="Erro interno de banco de dados")

    #aplica a formatação de acordo com o tamanho máximo (+2 para um espaço extra)
    for i in range(1, 6):
        if(planilha.column_dimensions[get_column_letter(i)].width < (column_widths[i-1] + 2)):
            planilha.column_dimensions[get_column_letter(i)].width = column_widths[i-1] + 2

    workbook.save(file_path)

    return file_path