import cv2
import easyocr
import numpy as np

IMG_MIN_SIZE = 600


def recognize_text(img_path):

    image_toresize = cv2.imread(img_path)
    height, width = image_toresize.shape[:2]

    if height < IMG_MIN_SIZE or width < IMG_MIN_SIZE:
        new_height = IMG_MIN_SIZE if height < IMG_MIN_SIZE else height
        new_width = IMG_MIN_SIZE if width < IMG_MIN_SIZE else width

        blank_image = np.zeros((new_height, new_width, 3), np.uint8)
        blank_image[:, :] = (255, 255, 255)

        l_img = blank_image.copy()
        l_img[0:height, 0:width] = image_toresize.copy()

        cv2.imwrite(img_path, l_img)

    reader = easyocr.Reader(['ru'])
    return reader.readtext(img_path)


def get_text_bbox(img_path):

    try:
        result = recognize_text(img_path)

        for (bbox, _, prob) in result:
            if prob >= 0.5:
                (top_left, _, bottom_right, _) = bbox
                return int(top_left[0]), int(top_left[1]), int(bottom_right[0]), int(bottom_right[1])
    except:
        print('Не удалось распознать текст')

    return (0, 0, 0, 0)
