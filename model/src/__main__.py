import os
import numpy as np
from data import Data
from parser import Parser
from config import Config
from network import Network
from embeddng import Embedding

def main_model():
    args = Parser().get_parser().parse_args()
    config = Config(args)
    data = Data(config)
    net = Network(config)
    # net.run_model()
