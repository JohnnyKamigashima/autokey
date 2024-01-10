import random

def calcula_digito(digs):
   s = 0
   qtd = len(digs)
   for i in range(qtd):
      s += n[i] * (1+qtd-i)
   res = 11 - s % 11
   if res >= 10: return 0
   return res      

n = [random.randrange(10) for i in range(9)]
n.append(calcula_digito(n))
n.append(calcula_digito(n))

cpf = ("%d%d%d%d%d%d%d%d%d%d%d" % tuple(n))

keyboard.send_keys(cpf)

#clipboard.fill_clipboard(cpf)
