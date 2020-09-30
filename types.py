from numpy import ndarray, uint8, dtype
from typing import Protocol, Type, Union, Literal, Optional, overload, Tuple


class Image(Protocol, ndarray): # type: ignore
    dtype: Type[dtype] = uint8
    ndim: Union[Literal[2], Literal[3]]
    shape: Union[Tuple[int, int], Tuple[int, int, int]]
