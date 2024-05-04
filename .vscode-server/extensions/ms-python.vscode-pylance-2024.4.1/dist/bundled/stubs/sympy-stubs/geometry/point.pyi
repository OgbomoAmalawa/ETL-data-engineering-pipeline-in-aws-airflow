from typing import Any, Iterator, Self
from sympy.core.basic import Basic
from sympy.core.power import Pow
from sympy.geometry.entity import GeometryEntity
from sympy.series.order import Order

class Point(GeometryEntity):
    is_Point = ...
    def __new__(cls, *args, **kwargs) -> Point | Point2D | Point3D | Self:
        ...
    
    def __abs__(self) -> Pow | Any:
        ...
    
    def __add__(self, other) -> Point | Point2D | Point3D:
        ...
    
    def __contains__(self, item) -> bool:
        ...
    
    def __truediv__(self, divisor) -> Point | Point2D | Point3D:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __getitem__(self, key):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __iter__(self) -> Iterator[Basic]:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __mul__(self, factor) -> Point | Point2D | Point3D:
        ...
    
    def __rmul__(self, factor) -> Point | Point2D | Point3D:
        ...
    
    def __neg__(self) -> Point | Point2D | Point3D:
        ...
    
    def __sub__(self, other) -> Point | Point2D | Point3D:
        ...
    
    @staticmethod
    def affine_rank(*args) -> int:
        ...
    
    @property
    def ambient_dimension(self) -> Any | int:
        ...
    
    @classmethod
    def are_coplanar(cls, *points) -> bool:
        ...
    
    def distance(self, other) -> Pow | Any:
        ...
    
    def dot(self, p) -> Order:
        ...
    
    def equals(self, other) -> bool:
        ...
    
    def intersection(self, other) -> list[Self] | list[Any]:
        ...
    
    def is_collinear(self, *args) -> bool:
        ...
    
    def is_concyclic(self, *args) -> bool:
        ...
    
    @property
    def is_nonzero(self) -> bool | None:
        ...
    
    def is_scalar_multiple(self, p) -> bool:
        ...
    
    @property
    def is_zero(self) -> bool | None:
        ...
    
    @property
    def length(self):
        ...
    
    def midpoint(self, p) -> Point | Point2D | Point3D:
        ...
    
    @property
    def origin(self) -> Point | Point2D | Point3D:
        ...
    
    @property
    def orthogonal_direction(self) -> Point | Point2D | Point3D:
        ...
    
    @staticmethod
    def project(a, b):
        ...
    
    def taxicab_distance(self, p) -> Order:
        ...
    
    def canberra_distance(self, p) -> Order:
        ...
    
    @property
    def unit(self) -> Point | Point2D | Point3D | Any:
        ...
    


class Point2D(Point):
    _ambient_dimension = ...
    def __new__(cls, *args, _nocheck=..., **kwargs) -> Self:
        ...
    
    def __contains__(self, item):
        ...
    
    @property
    def bounds(self) -> tuple[Basic, Basic, Basic, Basic]:
        ...
    
    def rotate(self, angle, pt=...) -> Point | Point2D | Point3D:
        ...
    
    def scale(self, x=..., y=..., pt=...) -> Point:
        ...
    
    def transform(self, matrix) -> Point | Point2D | Point3D:
        ...
    
    def translate(self, x=..., y=...) -> Point:
        ...
    
    @property
    def coordinates(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def x(self) -> Basic:
        ...
    
    @property
    def y(self) -> Basic:
        ...
    


class Point3D(Point):
    _ambient_dimension = ...
    def __new__(cls, *args, _nocheck=..., **kwargs) -> Self:
        ...
    
    def __contains__(self, item):
        ...
    
    @staticmethod
    def are_collinear(*points) -> bool:
        ...
    
    def direction_cosine(self, point) -> list[Any]:
        ...
    
    def direction_ratio(self, point) -> list[Any]:
        ...
    
    def intersection(self, other) -> list[Self] | list[Any] | list[Point] | list[Point2D]:
        ...
    
    def scale(self, x=..., y=..., z=..., pt=...) -> Point3D:
        ...
    
    def transform(self, matrix) -> Point3D:
        ...
    
    def translate(self, x=..., y=..., z=...) -> Point3D:
        ...
    
    @property
    def coordinates(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def x(self) -> Basic:
        ...
    
    @property
    def y(self) -> Basic:
        ...
    
    @property
    def z(self) -> Basic:
        ...
    


