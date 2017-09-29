import os
from PIL import Image
from parser import Parser
from config import Config
from data import Data

args = Parser().get_parser().parse_args()
config = Config(args)
data = Data(config)

VIDEO_DIR = "/home/dhruv/Desktop/VideoEmbedding/data/videos/"
FRAME_DIR = "/home/dhruv/Desktop/VideoEmbedding/data/frames/"

for video in os.listdir(VIDEO_DIR):
    if not os.path.exists(FRAME_DIR + video):
        os.makedirs(FRAME_DIR + video)
    frames, count = data.get_frames(video), 0
    for frame in frames:
       im = Image.fromarray(frame)
       im.save("{}{}/{}.png".format(FRAME_DIR, frame, count))
       count += 1

