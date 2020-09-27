
import jogovelha
import sys

erroInicializar = False
jogo = jogovelha.inicializar()

if len(jogo) != 3:
    erroIniciar = True
else:
    for linha in jogo:
        if len(linha) != 3:
            erroInicializar = True
        else:
            for elemento in lnha:
                if elemento != ".":
                    erroinicializar = True
if erroInicializar:
    sys.exit(1)
else:
    sys.exit(0)
