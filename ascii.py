import PIL.Image

# caracteres ASCII usados para formar la imagen
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# redimensionar la imagen
def resize(image, new_width=100):
    width, height = image.size
    ratio = height/width/1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convertir los pixeles a escala gris
def byw(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convertir los pixeles en una cadena de ASCII
def pixels_convert(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main(new_width=100):
    # Abrir la imagen mediante un input
    path = input("Introduce la ruta de tu imagen:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "no es una ruta válida.")
        return
  
    # convertir la imagen a ascii    
    new_image_data = pixels_convert(byw(resize(image)))
    
    # formato
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width)])
    
     # imprimir resultado
    print(ascii_image)
    
    # guardar el resultado como .txt
    with open("imagen_ascii.txt", "w") as f:
        f.write(ascii_image)
 

main()
