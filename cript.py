import random
from dicionario import dic
import unicodedata


def decrypt(valor):
    pass


def encrypt(valor):
    valor_sem_acentos = str(unicodedata.normalize('NFKD', valor).encode('ASCII', 'ignore'))
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


print(encrypt('''Hoje em dia, os computadores estão presentes em nossa vida de uma forma nunca vista anteriormente. Sejam em casa, na escola, na faculdade, na empresa ou em qualquer outro lugar, eles estão sempre entre nós. Ao contrário do que parece, a computação não surgiu nos últimos anos ou décadas, mas sim há mais de 7 mil anos.

Muitos povos da antiguidade utilizavam o ábaco para a realização de cálculos do dia a dia, principalmente nas áreas de comércio de mercadorias e desenvolvimento de construções civis. Ele pode ser considerado como a primeira máquina desenvolvida para cálculo, pois utilizava um sistema bastante simples, mas também muito eficiente na resolução de problemas matemáticos. É basicamente um conjunto de varetas de forma paralela que contém pequenas bolas que realizam a contagem.

Seu primeiro registro é datado do ano de 5.500 a.C., pelos povos que constituíam a Mesopotâmia. Contudo, o ábaco também foi usado posteriormente por muitas outras culturas: Babilônia, Egito, Grécia, Roma, Índia, China, Japão etc. Cada um desses povos possui uma versão de específica dessa máquina, entretanto, preservando a sua essência original. Seu nome na Roma Antiga era "Calculus", termo de onde a palavra cálculo foi derivada.'''))