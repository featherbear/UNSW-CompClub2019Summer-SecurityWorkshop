# To hide
# img = (covr >> n << n) | hide >> (8 - n)

# To extract
# img << (8-n)

from PIL import Image

def extract(source, lsb):
    image = Image.open(source).convert(mode = "RGB")
    pixels = image.load()
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            r = 0xFF & (r << (8 - lsb))
            g = 0xFF & (g << (8 - lsb))
            b = 0xFF & (b << (8 - lsb))
            pixels[x, y] = (r, g, b)

    image.save('output.png')
    print("Image saved into output.png!")

    image.show()
    image.close()


def hide(medium, secret_image, lsb):
    medium_image = Image.open(medium).convert(mode = "RGB")
    
    orig_secretImage = Image.open(secret_image).convert(mode = "RGB")
    resized_secretImage = orig_secretImage.resize(medium_image.size)
    orig_secretImage.close()

    m_pixels = medium_image.load()
    s_pixels = resized_secretImage.load()
    
    result = Image.new("RGB", medium_image.size)
    r_pixels = result.load()
    
    for x in range(result.width):
        for y in range(result.height):
            o_r, o_g, o_b = m_pixels[x, y]
            s_r, s_g, s_b = s_pixels[x, y]

            r = (o_r >> lsb << lsb) | (s_r >> (8 - lsb))
            g = (o_g >> lsb << lsb) | (s_g >> (8 - lsb))
            b = (o_b >> lsb << lsb) | (s_b >> (8 - lsb))

            r_pixels[x, y] = r, g, b

    result.save('output.png')
    print("Image saved into output.png!")

    result.show()
    result.close()
    medium_image.close()
    resized_secretImage.close()

##########################################################
# The stuff below here already written for you!           
# It's boring stuff that isn't really part of the activity
# ---
# Of course, feel free to poke around, and mess with it
# Your mentors will be able to help explain the code :)
##########################################################

if __name__ == "__main__":
    print("LSB Image in Image")
    print("==================")
    print("1. Hide           ")
    print("2. Extract        ")

    from tempfile import SpooledTemporaryFile
    from typing import Union
    
    def getFile(prompt: str) -> Union[str, SpooledTemporaryFile]:
      file = input(prompt)
      
      import os.path
      if os.path.isfile(file): return file
      
      import re
      if re.match("^https?://", file, re.IGNORECASE):
        print("Detected web link - downloading...")
        try:
          from urllib import request as urllib2
          import tempfile
        
          tmpFile = SpooledTemporaryFile()
          tmpFile.write(urllib2.urlopen(file).read())
          
          tmpFile.flush()
          return tmpFile
        except:
          print("Could not retrieve file at", file)

      return None

    def getIntInput(prompt: str, *args: [int]) -> int:
      number = input(prompt)
      if not number.isdigit(): return None
      
      number = int(number)
      if args and not number in args: return None
      
      return number

    while True:
        action = getIntInput("Enter an action > ", *(1,2))
        if action is None: continue

        if action == 1:
            medium = getFile("Enter the filename of the medium (image to hide into): ")
            if medium is None: 
              print("Cannot find file")
              continue

            secret_image = getFile("Enter the filename of the secret image: ")
            if secret_image is None:
              print("Cannot find file")
              continue

            lsb = getIntInput("Enter the number of significant bits to modify (0-8): ", *range(9))
            if lsb is None: 
              print("Invalid choice")
              continue

            hide(medium, secret_image, lsb)
            if type(medium) is SpooledTemporaryFile: medium.close()
            if type(secret_image) is SpooledTemporaryFile: secret_image.close()
        else:
            source = getFile("Enter the filename of the image to extract from: ")
            if source is None:
              print("Cannot find file")
              continue

            lsb = getIntInput("Enter the number of significant bits to analyse: ", *range(9))
            if lsb is None: 
              print("Invalid choice")
              continue

            extract(source, lsb)
            if type(source) is SpooledTemporaryFile: source.close()
        break
