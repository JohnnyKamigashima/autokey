# Enter script code
import random
numero_aleatorio = random.randint(100, 10000)
pessoa = "JHK Fechamento PJ 20240105172959"
negociacao = "JHK PF 20240108091408"
#negociacao = "JHK PJ 20240108091555"
#negociacao = "JHK PJ 20240108091748"
#negociacao = "JHK PF 20240108101332"

keyboard.send_keys("<tab>") 
keyboard.send_keys("<tab>") 
keyboard.send_keys("<tab>") 
keyboard.send_keys("<tab>") 
keyboard.send_keys("<tab>") 

keyboard.send_keys(" ") 
keyboard.send_keys("<tab>") 
keyboard.send_keys("<tab>") 
time.sleep(0.3) 
#keyboard.send_keys("JHK 20231221113748")
keyboard.send_keys(pessoa) # Pessoa

time.sleep(1) 
keyboard.send_keys("<enter>")
keyboard.send_keys("<tab>") 
time.sleep(0.3) 
keyboard.send_keys(negociacao) # Negociação
time.sleep(1) 
keyboard.send_keys("<enter>")
keyboard.send_keys("<tab>") 
time.sleep(0.3) 
time.sleep(1) 
#keyboard.send_keys("<enter>")
#keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys(str(numero_aleatorio))
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("Teste") # pressiona tab

keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("Teste") # pressiona tab

keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("Acréscimo") # pressiona tab
time.sleep(1) 
keyboard.send_keys("<tab>") # pressiona tab
keyboard.send_keys("<tab>") # pressiona tab
time.sleep(1)
keyboard.send_keys("0") # pressiona tab

keyboard.send_keys("<tab>") # pressiona tab
# keyboard.send_keys("<tab>") # pressiona tab
# keyboard.send_keys("<tab>") # pressiona tab
# keyboard.send_keys("<tab>") # pressiona tab
# keyboard.send_keys("Suporte Técnico") # pressiona tab
# time.sleep(2) 
# keyboard.send_keys("<enter>")
# keyboard.send_keys("<tab>") # pressiona tab
