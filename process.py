from argparse import ArgumentParser, FileType
from typing import List
from inout import leitura, escrita, mostrar, ordem_mosaico
from tipos import Image


def aplica_ops(img: Image, ops: List[str]) -> Image:
    """Aplica a sequência de operações na imagem."""
    return img


if __name__ == "__main__":
    # parser de argumentos
    description = 'Ferramenta de processamentos simples de imagem.'

    parser = ArgumentParser(description=description, allow_abbrev=False)
    parser.add_argument('input', type=FileType('rb'), metavar='INPUT',
                        help='imagem de entrada')
    parser.add_argument('-s', '--force-show', action='store_true',
                        help='sempre mostra o resultado final em uma janela')
    parser.add_argument('-o', '--output', type=FileType('wb'), metavar='FILE',
                        help='arquivo para gravar o resultado')
    parser.add_argument('ops', type=str, metavar='OPERATION [ARGS...]', nargs='*',
                        help='operações que devem ser feitas na imagem')
    args = parser.parse_args()

    # entrada
    img, name = leitura(args.input)

    # operações
    img = aplica_ops(img, args.ops)

    # saída
    if args.output is None or args.force_show:
        mostrar(img, name)

    if args.output is not None:
        escrita(img, args.output)
