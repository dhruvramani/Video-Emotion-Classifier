import os
import utils

class Config(object):
    def __init__(self, args):
        self.codebase_root_path = args.path
        self.project_name = args.project
        self.batch_size = args.batch_size
        self.dropout = args.dropout
        self.optimizer = args.optimizer
        self.max_epochs = args.max_epochs
        self.cascade = args.cascade
        self.frames = args.frames
        self.load = args.load
        self.debug = args.debug

        self.project_path, self.data_path, self.cascade_path, self.ckptdir_path = self.set_paths()

    def set_paths(self):
        project_path = utils.path_exists(self.codebase_root_path)
        data_path = utils.path_exists(os.path.join(self.codebase_root_path, "../data", "videos"))
        cascade_path = utils.path_exists(os.path.join(self.codebase_root_path, "../data", "cascades"))
        ckptdir_path = utils.path_exists(os.path.join(self.codebase_root_path, "checkpoint"))
        return project_path, data_path, cascade_path, ckptdir_path
