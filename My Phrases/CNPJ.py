import random

def calcula_digito(digs, pesos):
   s = sum([digs[i]*pesos[i] for i in range(len(digs))]) % 11
   return 0 if s < 2 else 11 - s

def gera_cnpj():
   # Gera os primeiros 12 dígitos do CNPJ
   cnpj = [random.randint(0, 9) for _ in range(8)] + [0, 0, 0, 1]
   
   # Calcula o primeiro dígito de verificação
   pesos = list(range(5, 1, -1)) + list(range(9, 1, -1))
   cnpj.append(calcula_digito(cnpj, pesos))
   
   # Calcula o segundo dígito de verificação
   pesos = list(range(6, 1, -1)) + list(range(9, 1, -1))
   cnpj.append(calcula_digito(cnpj, pesos))
   
   return "%d%d%d%d%d%d%d%d%d%d%d%d%d%d" % tuple(cnpj)

# Gera o CNPJ e copia para a área de transferência
cnpj = gera_cnpj()

keyboard.send_keys(cnpj)
clipboard.fill_clipboard(cnpj)

#clipboard.fill_clipboard(cnpj)