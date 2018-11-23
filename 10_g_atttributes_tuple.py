from collections import namedtuple
from dataclasses import dataclass

X = namedtuple('Point', 'attrx attry')
a = X(attrx=1, attry=2)  # attrx=  <- Dynamic **kwargs
a.attrx  # attrx


class C(namedtuple('Point', 'attrx attry')):
    pass


y = C(1, attry=2)  # attry=
y.attrx  # attrx



@dataclass
class Point:
    attrx: float
    attry: float


p = Point(attrx=1, attry=2)  # attrx=
p.attrx  # attrx
