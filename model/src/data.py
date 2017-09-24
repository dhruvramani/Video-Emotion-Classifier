import os
import sys
import imageio
import numpy as np

class Data(object):
    def __init__(self, config):
        self.config = config
        self.batch_count = 1

    def read_video(self, file_name):
        vid = imageio.get_reader(os.path.join(self.config.data_path, file_name), 'ffmpeg')
        frame_count = 0
        for _ in vid:
            frame_count += 1
        return vid, frame_count

    def get_frames(self, file_name):
        vid, frame_count = self.read_video(file_name)
        if(frame_count > self.config.frames):
            single_frame = int(frame_count / self.config.frames)
        else : single_frame = 1
        frame, frames = 0, []
        while(frame < frame_count):
            frames.append(vid.get_data(frame))
            frame += int(single_frame)
        if(frame > frame_count):
            frames.append(vid.get_data(frame_count - 1))
        return np.asarray(frames, dtype=np.float32)

    def create_onehot(self, vector):
        one_hot = np.zeros((vector.size, vector.max() + 1))
        one_hot[np.arange(vector.size), vector] = 1
        return one_hot
