class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        output = ""
        for _ in range(self.height):
            output += "*"*self.width + "\n"
        return output

    def get_amount_inside(self, another):
        return int(self.width / another.width) * int(self.height / another.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __descr__(self):
        return str(self)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.side})"

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)
