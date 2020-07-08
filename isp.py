# Interface Segregation Principle

"""
Criar interface que contenha métodos gerais e deixar que suas subclasses extendam essas funções (Polimorfismo)
"""

""" Implementação errada """
class IShape:

    def draw_square(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError


class Circle(IShape):
    def draw_circle(self)
        pass


class Rectangle(IShape):
    def draw_rectangle
        pass


class Square(IShape):
    def draw_square:
        pass

"""--------------------------------------------------"""

"""Implementação correta"""
class IShape:
    def draw(self):
        raise NotImplementedError


class Circle(IShape):
    def draw(self):
        pass


class Square(IShape):
    def draw(self):
        pass


class Rectangle(IShape):
    def draw(self):
        pass



