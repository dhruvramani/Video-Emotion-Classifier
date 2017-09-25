import argparse

class Parser(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--path", default="../", help="Base Path for the Model")
        parser.add_argument("--project", default="VideoEmbedding", help="Project Folder")
        parser.add_argument("--cascade", default="haarcascade.xml", help="Cascade for OpenCV CLM")
        parser.add_argument("--frames", default=100, type=int, help="Number of Frames Per Video")
        parser.add_argument("--dropout", default=0.5, type=float, help="Dropout Keep")
        parser.add_argument("--optimizer", default="rmsprop", )
        parser.add_argument("--batch_size", default=30, type=int, help="Number of Videos in a Batch")
        parser.add_argument("--max_epochs", default=100, type=int, help="Maximum Number of Epochs")
        parser.add_argument("--debug", default=False, type=self.str_to_bool, help="Debug Mode")
        parser.add_argument("--load", default=False, type=self.str_to_bool, help="Load Model to calculate accuracy")
        self.parser = parser

#   TODO - config.py : cascade_path, videos_path, 
    def str_to_bool(self, string):
        if string.lower() == "true":
            return True
        elif string.lower() == "false":
            return False

    def get_parser(self):
        return self.parser