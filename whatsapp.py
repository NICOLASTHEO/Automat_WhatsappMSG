import pywhatkit as kit
import keyboard
import time
from datetime import datetime

# DUAS FORMAS DE AUTOMATIZAR MENSAGENS NO WHATSAPP
# SUPER INTERRESANTE PARA EMPRESAS, ACELERA PROCESSOS E MINIMIZA PESSOAL E RECURSOS.

# 1ª FORMA:

kit.sendwhatmsg('+5511999887766',
                'Uma mensagem qualquer, a qualquer dia e horário para quantas pessoas eu quiser, sem estar com o celular na mão.', 10, 11)   # colocar o número com código do país e estado.


# 2ª FORMA:

# colocar o número com código do país e estado.
contatos = ['+5511999887766', '+5511977886655']

while len(contatos) >= 1:
    kit.sendwhatmsg(contatos[0], 'Uma mensagem qualquer, a qualquer dia e horário para quantas pessoas eu quiser, sem necessitar do celular.', datetime.now(
    ).hour, datetime.now().minute + 1)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl+w')
