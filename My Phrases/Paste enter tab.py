import time

# Obtém o texto atual da área de transferência
text = clipboard.get_clipboard()

# Remove espaços em branco no início e no final do texto
clean_text = text.strip()

# Define o texto limpo como o novo conteúdo da área de transferência
clipboard.fill_clipboard(clean_text)
keyboard.send_keys("<ctrl>+v") # cola o conteúdo da área de transferência
#keyboard.send_keys("<enter>") # pressiona enter
#keyboard.send_keys("<tab>") # pressiona tab
#time.sleep(0.1)  # espera por 300 milissegundos
#keyboard.send_keys("<tab>") # pressiona tab
#time.sleep(0.1)  # espera por 300 milissegundos
#keyboard.send_keys("<tab>") # pressiona tab
#time.sleep(0.1)  # espera por 300 milissegundos
#keyboard.send_keys("<tab>") # pressiona tab
#time.sleep(1)  # espera por 300 milissegundos
#keyboard.send_keys(" ") # pressiona space


