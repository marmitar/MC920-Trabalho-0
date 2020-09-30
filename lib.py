"""
Operações de processamento de imagens.

Nota
----
Todas as operações aqui fazem cópia da imagem para evitar
alterar inesperadamente o buffer interno dos vetores.
"""
import numpy as np
from typing import Optional, Tuple
from tipos import Image


# # # # # # # # # # # # #
# Operações auxiliares  #

Limit = Tuple[float, float]

def transformacao_linear(x: np.ndarray, ylim: Limit, xlim: Optional[Limit]=None) -> np.ndarray:
    """
    Transforma os elementos de array linearmente para a região ``ylim``.
    Quando definido, ``xlim`` serve como os limites iniciais do array,
    antes da transformação. Caso contrário, os limites usados são ``min(x)``
    e ``max(x)``.

    Nota
    ----
    Quando ``xlim`` é definido, é possível que o resultado ultrapasse
    os limites em ``ylim``.
    """
    xlim = x if xlim is None else xlim
    ymin, ymax = np.min(ylim), np.max(ylim)
    xmin, xmax = np.min(xlim), np.max(xlim)
    y = ((ymax - ymin) * x) / (xmax - xmin) + ymin
    return y


def trunca(array: np.ndarray) -> Image:
    """
    Trunca um array qualquer para inteiros de 8 bits, representando uma imagem.
    """
    img: Image = array.astype(np.uint8)
    img[array <= 0] = 0
    img[array >= 255] = 255

    assert img.ndim == 3
    return img


# # # # # # # # # # # # #
# Operações com imagens #

def grayscale(img: Image) -> Image:
    """
    Muda a imagem para tons de cinza.
    """
    gray = np.mean(img, axis=2)
    canais = np.stack([gray, gray, gray], axis=2)
    return trunca(canais)


def negativo(img: Image) -> Image:
    """
    Faz o negativo da imagem.
    """
    return ~img


def espelhamento_vertical(img: Image) -> Image:
    """
    Espelha a imagem pelas linhas.
    """
    mirror: Image = img[::-1]
    return mirror.copy()


def converter_intervalo(img: Image, zmin: int=100, zmax: int=200) -> Image:
    """
    Muda o intervalo de intensidades de ``[0, 255]`` para ``[zmin, zmax]``.
    """
    trf = transformacao_linear(img, (zmin, zmax))
    return trunca(trf)


def inverte_linhas_pares(img: Image) -> Image:
    """
    Espelha as linhas pares horizontalmente.
    """
    copy = img.copy()
    copy[::2] = copy[::2,::-1]
    return copy


def reflexao_linhas(img: Image) -> Image:
    """
    Reflete verticalmente as linhas superiores.
    """
    mid = img.shape[0] // 2
    copy = img.copy()
    copy[-mid:] = copy[:mid:-1]
    return copy


def ajuste_brilho(img: Image, gama: float) -> Image:
    """
    Ajusta o brilho da imagem com fator gama.
    """
    A = transformacao_linear(img, (0, 1), (0, 255))
    B = A ** (1 / gama)
    ajustado = transformacao_linear(B, (0, 255), (0, 1))
    return trunca(ajustado)


def plano_de_bit(img: Image, bit: int) -> Image:
    """
    Extrai o plano para um dado ``bit``.
    """
    bitpat = (img >> bit) & 1
    return bitpat * 255
