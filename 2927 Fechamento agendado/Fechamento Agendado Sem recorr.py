# Enter script code
import datetime
import subprocess

# Obter a data e hora atual
agora = datetime.datetime.now()
ontem = agora - datetime.timedelta(days=1)
amanha = agora + datetime.timedelta(days=1)
agora = agora + datetime.timedelta(minutes=2)

# Adicionar 5 minutos à hora atual
daqui_a_cinco_minutos = agora + datetime.timedelta(minutes=5)

# Formatar a data e hora para uma string
data_atual = agora.strftime("%d/%m/%Y")
data_ontem = ontem.strftime("%d/%m/%Y")
data_amanha = amanha.strftime("%d/%m/%Y")
hora_atual = agora.strftime("%H:%M")


def get_date_time():
    return subprocess.check_output(["date", "+%Y-%m-%d %H:%M:%S"]).decode('utf-8').strip()

keyboard.send_keys('JHK DCTCRRT-2927 ' + get_date_time())
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys(data_atual)
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("<tab>") # pressiona tab

keyboard.send_keys(hora_atual)
time.sleep(0.3)  # espera por 300 milissegundos
keyboard.send_keys("<left>")
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys(data_ontem)
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys(data_amanha)