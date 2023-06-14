from utils.send_email import send_email
import re
from services.webscrapping_services import WebScrapingService

# padrao_email = '\w{2,50}@\w{2,15}\.[a-z]{2,3}'
# while True:
#     dest = input(str('Informe o email que deseja enviar o relatório: '))
#     is_email = re.findall(padrao_email, dest)
#     if not is_email:
#         print(f'Email inválido!!\nPor favor insira um email válido [teste@exemplo.com]')
#     else:
#         break

obj = WebScrapingService()
obj.start_scrapping()
#send_email.send_email(dest)