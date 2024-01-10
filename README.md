# Intro

Este repo possui alguns scripts criados para AutoKey do Linux. A maioria dos scripts foram escritos em Python e podem ser reaproveitados em parte para o AutoHotKey.

Exemplo de script para AutoKey (Linux) que digita um numero de 10 digitos aleatorios ao apertar <ctrl> F5

```python
import subprocess
import random

# Função para executar o código Python e retornar o resultado
def run_python_code(code):
    process = subprocess.Popen(['python3', '-c', code], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode().strip()

# Código Python para gerar número de 10 dígitos aleatórios
python_code = """
import random

numero = str(random.randint(1000000000, 9999999999))
print(numero)
"""

# Executar código Python e obter o número gerado
random_number = run_python_code(python_code)

# Digitar número no campo ativo
keyboard.send_keys(random_number)

```


Exemplo de script para AutoHotKey (Windows) que digita um numero de 10 digitos aleatorios ao apertar <ctrl> F5

```python
#SingleInstance force

^F5::
    ; Código Python para gerar número de 10 dígitos aleatórios
    pythonCode := "
import random

numero = str(random.randint(1000000000, 9999999999))
print(numero)
"

    ; Salvar código Python em um arquivo temporário
    pythonFile := A_Temp . "\random_number_generator.py"
    FileDelete, %pythonFile%
    FileAppend, %pythonCode%, %pythonFile%

    ; Executar código Python
    Run, python %pythonFile%, , Hide

    ; Aguardar um pouco para que o resultado seja exibido
    Sleep, 500

    ; Ler o resultado do arquivo de log
    logFile := A_Temp . "\random_number_log.txt"
    FileRead, randomNumber, %logFile%

    ; Apagar o arquivo de log
    FileDelete, %logFile%

    ; Digitar número no campo
    SendInput % randomNumber
    return

```
