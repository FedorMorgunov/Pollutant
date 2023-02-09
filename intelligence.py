# This is a template.
# You should modify the functions below to match
# the signatures determined by the project specification
import numpy as np
import skimage as sk


def find_red_pixels(map_filename, upper_threshold=100, lower_threshold=50):
    """
    The find_red_pixels function takes a file name and several parameters as arguments and loads the specified image
    file. It then creates a new image with the same dimensions as the original image and sets all pixel values to 255
    (white). It then iterates over the pixels in the original image and checks if the pixel is red, based on the
    provided parameters. If the pixel is red, the corresponding pixel in the new image is set to black (0, 0, 0),
    otherwise it is left as white. Finally, the new image is saved to file and returned.
    """

    image = sk.io.imread('data/' + map_filename)

    new_image = np.full_like(image, 255)

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if not (image[x][y][0] > upper_threshold and image[x][y][1] < lower_threshold and image[x][y][2] < lower_threshold):
                new_image[x][y][0] = 0
                new_image[x][y][1] = 0
                new_image[x][y][2] = 0

    new_image = new_image[:, :, :3]
    sk.io.imsave('map-red-pixels.jpg', new_image)

    return new_image

    # Your code goes here


def find_cyan_pixels(map_filename, upper_threshold=100, lower_threshold=50):
    """The find_cyan_pixels function is similar to the find_red_pixels function, but it marks cyan pixels instead of
    red pixels in the output image. """

    image = sk.io.imread('data/' + map_filename)

    new_image = np.full_like(image, 255)

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if not (image[x][y][0] < upper_threshold and image[x][y][1] > lower_threshold and image[x][y][2] > lower_threshold):
                new_image[x][y][0] = 0
                new_image[x][y][1] = 0
                new_image[x][y][2] = 0

    new_image = new_image[:, :, :3]
    sk.io.imsave('map-cyan-pixels.jpg', new_image)

    return new_image

    # Your code goes here


def detect_connected_components(IMG):
    """The detect_connected_components function calls the find_red_pixels function to generate a black and white
    image with only red pixels marked. It then uses a queue-based algorithm to detect and mark connected components
    in the image. It returns the original image with the connected components marked. """

    all_components = []

    q = np.array([], dtype=int)
    # Creating an empty queue
    # Empty ndarray with specified datatype of the elements that can be stored in it

    component = 0
    pixels = 0

    mark = np.zeros_like(IMG[:, :, :1])

    for x in range(IMG.shape[0]):
        for y in range(IMG.shape[1]):
            if IMG[x][y][0] == 255 and mark[x][y][0] == 0:
                mark[x][y][0] = component + 1
                pixels += 1
                q = np.append(q, [x, y])
                # Enqueue: adding elements to the back of the ndarray
                while len(q) != 0:
                    q.shape = (-1, 2)
                    # Reshaping it into the n by 2 elements ndarray
                    m = q[0][0]
                    n = q[0][1]
                    q = np.delete(q, 0, axis=0)
                    # Dequeue: coping values of and deleting the first row of the  ndarray
                    for s in range(m-1, m+2):
                        for t in range(n-1, n+2):
                            try:
                                if IMG[s][t][0] == 255 and mark[s][t][0] == 0:
                                    mark[s][t][0] = component + 1
                                    pixels += 1
                                    q = np.append(q, [s, t])
                                    # Enqueue: adding elements to the back of the ndarray
                            except IndexError:
                                continue

                            """
                            Some pixels wouldn't have 8 neighbours. For example pixels in a first row.
                            Therefore I used Try and Except to catch the pixels that are out of range 
                            and jump to next iteration, e.g. don't include them in list
                            """

                component += 1
                all_components.append('Connected Component ' + str(component) + ', number of pixels = ' + str(pixels)+'\n')
                pixels = 0

    with open('cc-output-2a.txt', 'w') as f:
        for element in all_components:
            f.write(element)
        f.write('Total number of connected components: ' + str(component))

    return mark
    # Your code goes here


def detect_connected_components_sorted(MARK):
    """Your documentation goes here"""

    img = np.zeros_like(MARK)

    components = dict.fromkeys(list(range(1, np.amax(MARK)+1)), 0)
    # Making dictionary with keys corresponding to connected components
    # and values to the number of pixels in the component

    for x in range(MARK.shape[0]):
        for y in range(MARK.shape[1]):
            if MARK[x][y][0] != 0:
                components[MARK[x][y][0]] += 1

    sorted_components = {}

    def bubblesort(elements):
        swapped = False
        # Looping from size of array from last index[-1] to index [0]
        for n in range(len(elements) - 1, 0, -1):
            for i in range(n):
                if elements[i][1] > elements[i + 1][1]:
                    swapped = True
                    # swapping data if the element is less than next element in the array
                    elements[i], elements[i + 1] = elements[i + 1], elements[i]
            if not swapped:
                # exiting the function if we didn't make a single swap
                # meaning that the array is already sorted.
                return

    sorted_keys = []

    a = list(components.items())
    bubblesort(a)

    for i in list(reversed(a)):
        sorted_keys.append(i[0])

    for w in sorted_keys:
        sorted_components[w] = components[w]

    first_value = list(sorted_components.keys())[0]
    second_value = list(sorted_components.keys())[1]

    for x in range(MARK.shape[0]):
        for y in range(MARK.shape[1]):
            if MARK[x][y][0] == first_value or MARK[x][y][0] == second_value:
                img[x][y][0] = 255
            else:
                img[x][y][0] = 0

    sk.io.imsave('cc-top-2.jpg', img)

    with open('cc-output-2b.txt', 'w') as f:
        for component in sorted_components:
            f.write('Connected Component ' + str(component) + ', number of pixels = ' + str(sorted_components[component])+'\n')
        f.write('Total number of connected components: ' + str(np.amax(MARK)))

    # Your code goes here

