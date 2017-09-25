from parser import Parser
from config import Config
from data import Data
from embedding import Embedding

args = Parser().get_parser().parse_args()
config = Config(args)
data = Data(config)
embedding = Embedding(config, data)

frames = data.get_frames("0001.avi")
#print(os.path.join(config.cascade_path , config.cascade))
for i in frames:
  faces = embedding.detect_face(i)
  print(faces)
