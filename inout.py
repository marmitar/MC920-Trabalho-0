"""
Funções de IO com imagens e matrizes auxiliares.
"""
import numpy as np
import cv2
from pathlib import Path
from typing import IO, TextIO, AnyStr, Tuple, Union, Optional
from tipos import Image


def leitura(filebuf: IO[AnyStr]) -> Tuple[Image, str]:
    """
    Lê e decodifica uma imagem a partir de um buffer IO
    """
    buf = np.frombuffer(filebuf.read(), dtype=np.uint8)
    nome = filebuf.name

    img = cv2.imdecode(buf, cv2.IMREAD_COLOR)
    if img is None:
        msg = f'não foi possível parsear "{nome}" como imagem'
        raise Exception(msg)

    return img, nome


def escrita(img: Image, arquivo: str) -> None:
    """
    Escreve uma matriz como imagem PNG em um arquivo
    """
    cv2.imwrite(arquivo, img)


def mostrar(img: Image, nome: str="") -> None:
    """
    Apresenta a imagem em uma janela com um nome
    """
    cv2.imshow(nome, img)
    cv2.waitKey()


def ordem_mosaico(arquivo: Union[str, TextIO, Path], *, delimitador: Optional[str]=None) -> np.ndarray:
    """
    Lê uma matriz de reordenação dos blocos de mosaico de um arquivo de texto.

    Nota
    ----
    A matriz de reordenação, com ``N`` linhas e ``M`` colunas, deve ser
    composta por inteiros de ``1`` a ``N * M``, sem repetições.

    Exemplo
    -------
    >>> from io import StringIO
    >>>
    >>> arq = StringIO("1 3\n2 4")
    >>> ordem_mosaico(arq)
    array([[0, 2],
           [1, 3]])
    >>>
    >>> csv = StringIO("1, 4\n3, 2")
    >>> ordem_mosaico(csv, delimitador=',')
    array([[0, 3],
           [2, 1]])
    """
    ordem = np.loadtxt(arquivo, dtype=int, ndmin=2, delimiter=delimitador)
    m, n = ordem.shape

    ordem -= 1
    idx = set(range(m * n))

    try:
        for linha in ordem:
            for ind in linha:
                idx.remove(ind)

        assert not idx

    except KeyError:
        msg = f'{arquivo=} não representa uma permutação de blocos'
        raise ValueError(msg)

    return ordem
