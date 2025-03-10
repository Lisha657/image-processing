from images import Image
import color2grayscale


image = Image("Bird.gif")
image.draw()
newImage = image.clone() # Create a copy of image
newImage.draw()
newImage.save("newbird")
color2grayscale.grayscale(newImage) # Change in second window only
newImage.draw()
