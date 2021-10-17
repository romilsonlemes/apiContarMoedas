from twilio.rest import Client

account_sid = 'ACec2c68efe231e3d99b8ca5333bc5b72c'
auth_token = 'b0bc1a5ace100cca429ac1db1d7c32e3'

# Cliente de envio
client = Client(account_sid, auth_token)

remetente = '+15155178184'
destino = '+5511981150868' #Romilson
#destino = '+5516988196226' #Darlison

sent_body="\n\nBoa tarde Senhor Engenheiro em Computação !!!"

message = client.messages.create(
    to=destino,
    from_=remetente,
    body=sent_body
)

print(message.sid)

