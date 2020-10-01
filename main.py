from argparse import ArgumentParser, FileType
from typing import List, Dict, Tuple, Callable, Any
import cv2
from inout import leitura, escrita, mostrar, ordem_mosaico
from tipos import Image
from lib import (
    grayscale, negativo, espelhamento_vertical, converter_intervalo,
    inverte_linhas_pares, reflexao_linhas, ajuste_brilho,
    plano_de_bit, combinacao, mosaico
)


Transform = Callable[..., Image]
Arguments = List[Callable[[str], Any]]

operation: Dict[str, Tuple[Transform, Arguments]] = {
    'monocromatico':    (grayscale,             []),
    'negativo':         (negativo,              []),
    'esp.vertical':     (espelhamento_vertical, []),
    'conv.intervalo':   (converter_intervalo,   []),
    'inverte.pares':    (inverte_linhas_pares,  []),
    'reflexao':         (reflexao_linhas,       []),
    'aj.brilho':        (ajuste_brilho,         [float]),
    'plano.bit':        (plano_de_bit,          [int]),
    'combina':          (combinacao,            [cv2.imread, float]),
    'mosaico':          (mosaico,               [ordem_mosaico])
}


def aplica_ops(img: Image, ops: List[str]) -> Image:
    """Aplica a sequência de operações na imagem."""

    op = iter(ops)

    for code in op:
        # decide a operação
        func, argp = operation[code]
        # le e parseia os argumentos necessarios
        args = [argty(next(op)) for argty in argp]
        # aplica a operação com os argumentos
        img = func(img, *args)

    return img


# parser de argumentos
description = 'Ferramenta de processamentos simples de imagem.'

parser = ArgumentParser(description=description, allow_abbrev=False)
parser.add_argument('input', type=FileType('rb'), metavar='INPUT',
                    help='imagem de entrada')
parser.add_argument('-f', '--force-show', action='store_true',
                    help='sempre mostra o resultado final em uma janela')
parser.add_argument('-o', '--output', type=FileType('wb'), action='append', metavar='FILE',
                    help='arquivo para gravar o resultado')
parser.add_argument('ops', type=str, metavar='OPERATION [ARGS...]', nargs='*',
                    help='operações que devem ser feitas na imagem')

if __name__ == "__main__":
    args = parser.parse_intermixed_args()

    # entrada
    img, name = leitura(args.input)

    # operações
    img = aplica_ops(img, args.ops)

    # saída
    if len(args.output) == 0 or args.force_show:
        mostrar(img, name)

    for output in args.output:
        escrita(img, output)
