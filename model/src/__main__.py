import os
import numpy as np
from data import Data
from parser import Parser
from config import Config
from network import Network
from embeddng import Embedding

class Model(object):
    def __init__(self, config):
        self.config = config