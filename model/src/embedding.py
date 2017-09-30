import os

FRAMES_DIR = "/root/shared/VideoEmbedding/data/frames/"
ALIGNED_DIR = "/root/shared/VideoEmbedding/data/aligned/"
FEATURES_DIR = "/root/shared/VideoEmbedding/data/features/"
OPENFACE_DIR = "/root/openface/"

for video in os.listdir(FRAMES_DIR):
    frames = os.listdir(FRAMES_DIR + video)
    n_frames = int(len(frames)/50)
    count, dont_delete = 0, list()
    while(count < 50 and count < len(frames)):
        dont_delete.append(frames[count])
        count += n_frames
    for frame in frames:
        if frame not in dont_delete:
            os.remove(FRAMES_DIR +  video +  frame)
    while count < len(frames):
        if frames[count] not in dont_delete:
            os.remove(FRAMES_DIR + video + frame)
        count += 1
    
    os.system("for N in {1..8}; do " + OPENFACE_DIR + "util/align-dlib.py " + FRAMES_DIR + video + " align outerEyesAndNose " + ALIGNED_DIR  + " --size 96 & done")
    os.system(OPENFACE_DIR + "batch-represent/main.lua -outDir " + FEATURES_DIR + " -data " + ALIGNED_DIR)


