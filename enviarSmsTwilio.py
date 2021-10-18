from twilio.rest import Client

account_sid = '' # Verificar esta informação no Arquivo de configuração deste Projeto
auth_token = ''  # Verificar esta informação no Arquivo de configuração deste Projeto

# Cliente de envio
client = Client(account_sid, auth_token)

remetente = ''  # Verificar esta informação no Arquivo de configuração deste Projeto
destino = '+5511981150868' #Romilson

sent_body="\n\nBom dia Senhor Romilson Lemes !!!"

message = client.messages.create(
    to=destino,
    from_=remetente,
    body=sent_body
)

print(message.sid)

