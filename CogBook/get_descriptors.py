from facenet_models import FacenetModel
import numpy as np
from CogBook.label_config import settings

def get_descriptors(image_data, *, detect_thresh=settings.DETECTION_THRESHOLD):
    """
    Returns a descriptors numpy array.

    Parameters
    ----------
    image_data : numpy.ndarray, shape-(R, C, 3) (RGB is the last dimension)
        Pixel information for the image.
    
    Returns
    -------
    np.ndarray, shape-(N, 512)
        The descriptor vectors, where N is the number of faces.
    """
    
    model = FacenetModel()
    boxes, probabilities, _ = model.detect(image_data)
    descriptors = model.compute_descriptors(image_data, boxes)
    
    output = []
    for i in range(len(descriptors)):
        if (probabilities[i] >= detect_thresh):
            output.append(descriptors[i])
    return np.array(output)
