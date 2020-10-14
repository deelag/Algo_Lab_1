class ProjectorScreen:
    def __init__(self, height, width, manufacturer, fastening_type):
        self.height = int(height)
        self.width = int(width)
        self.manufacturer = manufacturer
        self.fastening_type = fastening_type

    def __str__(self):
        return "height:" + str(self.height) + "; width:" + str(
            self.width) + "; manufacturer: " + self.manufacturer + "; fastening type: " + self.fastening_type
