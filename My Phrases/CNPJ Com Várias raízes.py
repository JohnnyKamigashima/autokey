import random

def calcular_digito_verificador(cnpj):
    multiplicador1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    multiplicador2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    
    soma = 0
    for i in range(len(cnpj)):
        soma += int(cnpj[i]) * multiplicador1[i]
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    
    cnpj_com_digito1 = cnpj + str(digito1)
    
    soma = 0
    for i in range(len(cnpj_com_digito1)):
        soma += int(cnpj_com_digito1[i]) * multiplicador2[i]
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    
    return str(digito1) + str(digito2)

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

cnpj_raiz = cnpj[:8]  # Raiz do CNPJ

# Gerar 10 CNPJs com a mesma raiz
for _ in range(10):
    cnpj = cnpj_raiz + str(random.randint(0, 9)).zfill(4)
    ultimos_digitos = calcular_digito_verificador(cnpj)
    cnpj_completo = cnpj + ultimos_digitos
    
    clipboard.fill_clipboard(cnpj_completo)
    time.sleep(0.2)
    