import yagmail
import json

def send_email(destinatario):
    with open("info_email.json", "r") as file:
        content_file = json.load(file)
        email = content_file['email']
        password = content_file['password']

    user = yagmail.SMTP(user=email, password=password)

    user.send(
        to=destinatario, 
        subject='Relatório de Preços', 
        contents='Em anexo, segue relatório atualizado', 
        attachments='Relatorio.xlsx')

    print('\nEMAIL ENVIADO !!!!\n')