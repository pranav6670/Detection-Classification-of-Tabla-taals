## Automatic Detection and classification of tabla talas from given music

### Methods used

1. Models
  * Convolutional Neural Network 
  * Long Short-Term Memory Network
  
2. Signal Processing
  * Downsampling (from 44100 to 16000)
  * Noise Threshold Detection (Using envelope detection)
  

### Getting Started

1. Clone this repository `git clone https://github.com/pranav6670/Detection-Classification-of-Tabla-taals.git`.

2. Data is stored in `wavfiles` diectory. Check-out the data. There are 10 classes of [talas](https://en.wikipedia.org/wiki/Tala_(music)). A `test.csv` is included in the directory 

3. First run the `dataops.py` script which will pre-process the data which includes, first, downsampling the data and then cleaning it(noise threshold detection).

4. Then create two folders named `models` and `pickles` into the directory.

5. Run `model.py` to form pickles out of the data and start training. The `cfg.py` can be used to adjust the parameters of MFCC function. `In model.py`, `config.mode == 'conv'` will select the CNN model while `config.mode == 'rec'` will select the LSTM model. The difference between these is only the shape of input data to the model. Once pickles are formed for both the models, the data dosen't load again the next time, saving alot of time. The models are easy to modify.

6. Under `models` directory, you will find the `conv.model` and `rec.model` formed, after training. Use these models to predict using `predict.py`

### Data Distribution

![Data](https://github.com/pranav6670/Detection-Classification-of-Tabla-taals/blob/master/distribution.png)



  
  
