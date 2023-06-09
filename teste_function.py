from utils.add_and_check_worksheet_currenty import add_and_check_worksheet_currenty
from utils.data_filter_sheet import data_filter_sheet
data = 'TOX // 455.22 // 07/06/23 // MANGUEIRA(ORC 326971) // 1 // 019861 // LINHA GVV // FLVV10 // BAIXO // 63303 // 25215 // 270340 // 30/07/23 // ADRIEL // BOTELHO // PREVISAO AGOSTO'
new_data = data_filter_sheet(data, max_column=21)      
#data = [None,None, 'TOX', 84523.51, '07/06/23','Compra do fuso do BR_0068452', 1, None ,19860, 'LINHA FLVV', 'FLVV15', 'ALTO',63303,25214,None,None,270340,'30/07/23','Adriel', 'Marcelo', 'Previsão para 30/JULHO' ]

add_and_check_worksheet_currenty(
    file='Relatorio.xlsx',
    data= new_data,
    worksheet='JUNHO',
    max_row=58,
    min_row=17,
    max_column=21,
    min_column=1
)
