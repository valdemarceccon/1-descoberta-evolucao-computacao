from aula2_criptografia.dicionario import dic
import random
import unicodedata
import re


def decrypt(valor):
    pattern = re.compile(r'([\\/><]?[0-9a-zA-Z]{3}|.)')
    resultado = ''
    for trecho in pattern.finditer(valor):
        resultado = resultado + find_value(trecho.group(0))

    return resultado


def encrypt(valor):
    valor_sem_acentos = str(unicodedata.normalize('NFKD', valor).encode('ASCII', 'ignore'), 'ASCII')
    r = []
    for c in valor_sem_acentos:
        code = find_code(c)
        if code is not None:
            r.append(shuffle(code))
        else:
            r.append(c)

    return ''.join(r)


def shuffle(valor):
    string_to_shuffle = valor[1:] if len(valor) == 4 else valor
    r = random.sample(string_to_shuffle, len(string_to_shuffle))
    join = "".join(r)
    return valor[0] + join if len(valor) == 4 else join


def find_code(valor):
    for key, value in dic.items():
        if str.upper(valor) == str.upper(value):
            return key

    return None


def find_value(valor):
    for key, value in dic.items():
        s = set(key)
        if set(valor) == s:
            return value

    return valor


if __name__ == '__main__':
    import sys
    import argparse

    argparser = argparse.ArgumentParser(description='Criptografa e descriptografa o texto do arquivo informado')
    argparser.add_argument('arquivo', type=str, help='Nome ou caminho do arquivo a ser criptografado ou '
                                                     'descriptografado')
    argparser.add_argument('--acao', dest='acao', default='c')

    parsed_args = argparser.parse_args()

    with open(sys.argv[1], encoding='UTF-8') as arquivo:
        for linha in arquivo:
            if parsed_args.acao == 'c':
                criptografado = encrypt(linha)
                print(criptografado)
            else:
                descriptografado = decrypt(linha)
                print(descriptografado)
