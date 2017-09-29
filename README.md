# Video Embedding Generator

## Installation
Install the required Python Modules :
```shell
pip3 install -r requirements.txt
```
Install the required plugin to run the script :
```shell
python3  
import imageio
imageio.plugins.ffmpeg.download()
```
If the script doesn't work yet and you are on Ubuntu, open the video normally. It should install all the required plugins for working with videos.

Set up/Create all the directories
```shell
mv <video_path> ./data/
mkdir ./data/frames
mkdir ./data/aligned/
mkdir ./data/features/
```
Install Docker and do the following :
```shell
docker pull bamos/openface
docker run bamos/openface -v <host-path>:<path-docker> -it bash
```

## Running
Modify the path variables in the scripts before running.
```shell
cd model/src
python3 frames.py
python3 embedding.py
```
