import cv2
import numpy as np

def read_img(path):
   return cv2.imread(path, 0)

def s_p_noisy_without_superposition(image, salt_prop, pepper_prop):
    noisy_image = np.copy(image)
    shape = image.shape
    total_pixels = image.size
    pixel_to_change = []
    salt_coords = []
    pepper_coords = []
    num_salt = int(total_pixels * salt_prop)
    num_pepper = int(total_pixels * pepper_prop)
    while len(pixel_to_change) <= num_salt:
        random_pair = (np.random.randint(0, shape[0]),np.random.randint(0, shape[1]))
        if random_pair not in pixel_to_change:
            pixel_to_change.append(random_pair)
        else:
            pass
    while len(pixel_to_change) <= num_salt + num_pepper:
        random_pair = (np.random.randint(0, shape[0]),np.random.randint(0, shape[1]))
        if random_pair not in pixel_to_change:
            pixel_to_change.append(random_pair)
        else:
            pass
    print(pixel_to_change)
    # Adicione "sal" (pixels brancos) à imagem
    # salt_coords = [np.random.randint(0, d, num_salt) for d in image.shape]
    #noisy_image[salt_coords] = 255

    # Adicione "pimenta" (pixels pretos) à imagem
    # pepper_coords = [np.random.randint(0, d, num_pepper) for d in image.shape]
    # noisy_image[pepper_coords] = 0
    for i in range(num_salt):
        salt_coords.append(pixel_to_change[i])
    for i in range(num_salt, num_pepper):
        salt_coords.append(pixel_to_change[i])
    noisy_image[salt_coords] = 255
    noisy_image[pepper_coords] = 0
    return noisy_image

def s_p_noisy(image, salt_prop, pepper_prop):
    salt_coords = [];    pepper_coords = []
    noisy_image = np.copy(image)
    shape = image.shape
    total_pixels = image.size
    num_salt = int(total_pixels * salt_prop)
    num_pepper = int(total_pixels * pepper_prop)
    print(num_salt, num_pepper)
    while len(salt_coords) <= num_salt:
        random_pair = (np.random.randint(0, shape[0]),np.random.randint(0, shape[1]))
        salt_coords.append(random_pair)
    while len(pepper_coords) <= num_salt + num_pepper:
        random_pair = (np.random.randint(0, shape[0]),np.random.randint(0, shape[1]))
        pepper_coords.append(random_pair)
    print(salt_coords, pepper_coords)
    for coord in salt_coords: 
        noisy_image[coord] = 255
    for coord in pepper_coords: 
        noisy_image[coord] = 0
    return noisy_image
# image = read_img('notebooks/img/img46_gray_noise.png')
image = read_img('notebooks/img/img46.png')
print(image.shape)
print(image.size)
salt_propability = 0.1  # Exemplo: 1% dos pixels serão "sal"
pepper_probability = 0.2  # Exemplo: 1% dos pixels serão "pimenta"

noisy_image = s_p_noisy(image, salt_propability, pepper_probability)

cv2.imshow('Imagem', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

   #if image is not None:
        #cv2.imshow('Imagem', image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
    #else:
    #    return 
# Carrega a imagem
