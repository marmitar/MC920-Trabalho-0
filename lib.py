"""
Operações de processamento de imagens.
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
