class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
# create __init__(self, start)
# create method for .reset and .generate

    def __init__(self, start):
        """create counter starting from start number"""
        self.start = start
        self.serial = start
        self.increment = 0

    def generate(self):
        """increments the serial number by 1"""
        self.start += self.increment
        self.increment = 1

        return self.start


    def reset(self):
        """"resets serial number back to start number"""
        self.start = self.serial
        self.increment = 0