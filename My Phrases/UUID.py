from datetime import datetime

# Obter o timestamp atual
agora = datetime.now()

# Converter para string
timestamp_str = agora.strftime("%Y%m%d%H%M%S")
keyboard.send_keys(timestamp_str)# Enter script code