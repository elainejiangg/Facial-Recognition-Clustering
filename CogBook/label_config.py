from argparse import Namespace
from pathlib import Path

path = Path(__file__).resolve().parent

settings = Namespace()

settings.DETECTION_THRESHOLD = 0.97
settings.FACE_IDENTIFY_THRESHOLD = 0.5
