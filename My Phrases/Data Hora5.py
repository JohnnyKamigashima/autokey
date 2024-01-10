import datetime

# Obter a data e hora atual
agora = datetime.datetime.now()
agora = agora + datetime.timedelta(minutes=2)

# Adicionar 5 minutos à hora atual
daqui_a_cinco_minutos = agora + datetime.timedelta(minutes=5)
amanha = agora + datetime.timedelta(days=1)

# Formatar a data e hora para uma string
data_atual = agora.strftime("%d/%m/%Y")
hora_atual = agora.strftime("%H:%M")
#data_futura = daqui_a_cinco_minutos.strftime("%d/%m/%Y")
data_futura = amanha.strftime("%d/%m/%Y")
hora_futura = daqui_a_cinco_minutos.strftime("%H:%M")

# Digitar a data e hora
keyboard.send_keys(data_atual)
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys(hora_atual)
time.sleep(0.5)
keyboard.send_keys("<left>")

keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys(data_futura)
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys(hora_futura)
time.sleep(0.5)
keyboard.send_keys("<left>")