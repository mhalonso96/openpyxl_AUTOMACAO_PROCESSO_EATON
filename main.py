from services.openpyxl_services import *
from utils.data_filter_sheet import data_filter_sheet
try:
    data = 'TOX // 455.22 // JUNHO // MANGUEIRA(ORC 326971) // 1 // 019861 // LINHA GVV // FLVV10 // BAIXO // 63303 // 25215 // 270340 // 04/07 // ADRIEL // BOTELHO // PREVISAO AGOSTO'
    new_data = data_filter_sheet(data, 21)
        #print('NOVOS DADOS: ', new_data)
    openService = OpenpyxlService(
            Workbook(),
            filename='Relatorio',
            data = new_data,
            worksheet= 'JUNHO',
            max_row=50,
            min_row=18,
            max_column=21,
            min_column=1
        )
    openService.controller_sheet_v2(last_row=33)

except Exception as error:
  print(error)