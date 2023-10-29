import cv2
import numpy as np

def read_img(path):
   return cv2.imread(path)

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

salt_propability = 0.1  # % dos pixels serão "sal"
pepper_probability = 0.2  # % dos pixels serão "pimenta"
#---------------------------------------------------
image = read_img('notebooks/img/img46.png')
cv2.imshow('Imagem', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

noisy_image = s_p_noisy(image, salt_propability, pepper_probability)

noisy_image = read_img('notebooks/img/img46_gray_noise.png')
cv2.imshow('Noisy-Imagem', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#---------------------------------------------------
filtered_image = cv2.medianBlur(noisy_image, 17)
cv2.imshow('Fixed-Imagem', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()