import numpy as np
from facenet_models import FacenetModel
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.pyplot import text
from CogBook.label_config import settings 

from PIL import Image

from CogBook import query_database

def label_faces(image_data, *, box_threshold=settings.DETECTION_THRESHOLD, iden_threshold=settings.FACE_IDENTIFY_THRESHOLD):
    """
    Displays an image with boxes around people's faces and labels them with names.

    Parameters
    ----------
    image_data : numpy.ndarray, shape-(R, C, 3) (RGB is the last dimension)
        Pixel information for the image.
    """
    
    # this will download the pretrained weights (if they haven't already been fetched)
    # which should take just a few seconds
    model = FacenetModel()

    # detect all faces in an image
    # returns a tuple of (boxes, probabilities, landmarks)
    boxes, probabilities, _ = model.detect(image_data)

    # producing a face descriptor for each face
    # returns a (N, 512) array, where N is the number of boxes
    # and each descriptor vector is 512-dimensional
    fig, ax = plt.subplots()
    ax.imshow(image_data)
    if (boxes is None):
        x = image_data.shape[1] // 2
        y = image_data.shape[0] // 2
        ax.text(x, y,
                "GIMME A FACE",
                size=50,
                va="center",
                ha="center",
                bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8),))
        plt.show()
        return
    descriptors = model.compute_descriptors(image_data, boxes)

    names = []
    for d in descriptors:
        names.append(query_database(d, iden_threshold).capitalize())


    for box, prob, i in zip(boxes, probabilities, range(len(names))):
        if prob<box_threshold:
            continue
        # draw the box on the screen
        ax.add_patch(Rectangle(box[:2], *(box[2:] - box[:2]), fill=None, lw=2, color="red"))
        # add names to the box
        ax.text(*box[:2],
                names[i], #+" "+str(prob)
                size=12,
                va="center",
                bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8),))
    plt.show()
