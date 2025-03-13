class Image:
    def show(self):
        pass


class RealImage(Image):
    def __init__(self, file_name):
        self.file_name = file_name
        self._load_image()

    def _load_image(self):
        print(f"Load image from {self.file_name}")

    def show(self):
        print(f"Displaying {self.file_name}")


class ImageProxy(Image):
    def __init__(self, file_name):
        self.file_name = file_name
        self._real_image = None

    def show(self):
        if self._real_image is None:
           self._real_image = RealImage(self.file_name)
        self._real_image.show()

proxy_image = ImageProxy("/home/user/photo.jpeg")
proxy_image.show()
proxy_image.show()
