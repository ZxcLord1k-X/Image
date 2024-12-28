from PIL import Image
from PIL import ImageFilter
with Image.open("te3t tet tet tete  tet tet tet tet t tet t et tet tet tet tet tet .jpeg") as image_original:
    #image_original.show()

    image_gray = image_original.convert("L")
    image_gray.save("gray_kartinka.jpeg")
    image_gray.show()

    image_blur = image_original.filter(ImageFilter.BLUR)
    image_blur.save("blur_kartinka.jpeg")

    image_rotate = image_original.transpose(Image.ROTATE_180)
    image_rotate.save("rotate_kartinka.jpeg")