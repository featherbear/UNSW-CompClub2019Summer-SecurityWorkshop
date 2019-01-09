from PIL import Image

def extract(source, lsb):
    pass
    ## Open the image
    
    ## For each pixel, extract the least significant bits
    
    ## Store and show the hidden image!
    
    
def hide(medium, secret_image, lsb):
    pass
    ## Open the medium
    
    ## Open the secret image
    
    ## Resize the secret image to fit the medium
    
    ## For each pixel, hide the pixel information of the secret image into the medium

    ## Store and show the special image!



##########################################################
# The stuff below here already written for you!           
# It's boring stuff that isn't really part of the activity
# ---
# Of course, feel free to peek around and mess with it
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
