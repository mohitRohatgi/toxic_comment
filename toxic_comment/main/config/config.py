class Config(object):
    """Holds model hyperparams and data information.
    The config class is used to store various hyperparameters and dataset
    information parameters. Model objects are passed a Config() object at
    instantiation.
    """
    batch_size = 64
    num_steps = 10
    max_epochs = 16
    early_stopping = 2
    dropout = 0.9
    max_seq_length = None
    vocab_size = None
    embedding_size = None
    lr = 0.001
