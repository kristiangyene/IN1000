from clockwork import clockwork
api = clockwork.API('58e9ab3962aad466a70f82c8f010296afea659be', from_name = 'Sparebank1')
message = clockwork.SMS(to = '4798232848', message = 'Sikkerhetsbrudd i banken. Kom snarest.')
response = api.send(message)

if response.success:
    print (response.id)
else:
    print (response.error_code)
    print (response.error_message)
