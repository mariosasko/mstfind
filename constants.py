from typing import Container, Tuple, TypeVar, Union

T = TypeVar('T')
Number = Union[int, float]
Edge = Tuple[T, T]
Edges = Container[Tuple[Edge, Number]]
