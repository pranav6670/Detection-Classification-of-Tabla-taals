from keras.models import load_model
from keras.utils.vis_utils import plot_model

conv_model = load_model('/home/pranav/Desktop/models_training#1/conv.model')
rec_model = load_model('/home/pranav/Desktop/models_training#1/rec.model')

graph = plot_model(conv_model, to_file='convmodel.png', show_shapes=True,
                   show_layer_names=True)

graph1 = plot_model(rec_model, to_file='recmodel.png', show_shapes=True,
                   show_layer_names=True)

