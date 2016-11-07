from wand.image import Image
import PIL.Image as PI
import pyocr
import pyocr.builders
import io

if(__name__=="__main__"):
    tool = pyocr.get_available_tools()[0]
    lang = tool.get_available_languages()
    print(lang)