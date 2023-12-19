class Box:
    """ Create a Box class with length, width and height """

    def __init__(self, box_length, box_width, box_height):
        """" Create three private variables. Initialize length, width and height """
        self.__length = box_length
        self.__width = box_width
        self.__height = box_height

    def volume(self):
        """ Create a method to calculate the volume of the box"""
        return self.__length * self.__width * self.__height

    def get_length(self):
        """using get_length method to get box's length"""
        return self.__length

    def get_width(self):
        """using get_width method to get box's width"""
        return self.__width

    def get_height(self):
        """using get_height method to get box's height"""
        return self.__height


def box_sort(box_list):
    """uses insertion sort to sort a list of Boxes from greatest volume to least volume"""
    for index in range(1, len(box_list)):
        key_box = box_list[index]
        pos = index - 1
        while pos >= 0 and box_list[pos].volume() < key_box.volume():
            box_list[pos + 1] = box_list[pos]
            pos -= 1
        box_list[pos + 1] = key_box


def main():
    b1 = Box(3.4, 19.8, 2.1)
    b2 = Box(1.0, 1.0, 1.0)
    b3 = Box(8.2, 8.2, 4.5)

    box_list = [b1, b2, b3]
    box_sort(box_list)

    for box in box_list:
        print(f"Box: length={box.get_length()}, width={box.get_width()}, height={box.get_height()}, volume={box.volume()}")

if __name__ == '__main__':
    main()