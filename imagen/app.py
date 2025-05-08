import IPython

app = IPython.Application.instance()
app.kernel.do_shutdown(True)

import typing
import IPython.display
from PIL import Image as PIL_Image
from PIL import ImageOps as PIL_ImageOps

def display_image(
    image,
    max_width: int = 600,
    max_height: int = 350,
) -> None:
    pil_image = typing.cast(PIL_Image.Image, image._pil_image)
    if pil_image.mode != "RGB":
        # RGB is supported by all Jupyter environments (e.g. RGBA is not yet)
        pil_image = pil_image.convert("RGB")
    image_width, image_height = pil_image.size
    if max_width < image_width or max_height < image_height:
        # Resize to display a smaller notebook image
        pil_image = PIL_ImageOps.contain(pil_image, (max_width, max_height))
    IPython.display.display(pil_image)


from vertexai.preview.vision_models import ImageGenerationModel
import vertexai

vertexai.init(project="aihktn25-shared", location="us-central1")

generation_model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")

images = generation_model.generate_images(
    prompt="ENTER PROMPT HERE",
    number_of_images=4,
    aspect_ratio="1:1",
    negative_prompt="",
    person_generation="allow_adult",
    safety_filter_level="block_few",
    add_watermark=True,
)

display_image(images[0])