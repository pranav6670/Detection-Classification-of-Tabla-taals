import mainui
from PyQt5 import QtGui, QtCore, QtWidgets
import librosa
import librosa.display
import sys
import wave
import numpy as np
import matplotlib.pyplot as plt
import pyaudio


class MainApp(QtWidgets.QMainWindow, mainui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self._scripts = ("guiGO.py", "liveSpectogram.py")
        self._processes = []
        for script in self._scripts:
            process = QtCore.QProcess(self)
            process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
            process.setProcessChannelMode(QtCore.QProcess.ForwardedChannels)
            process.setProgram('bash')
            process.setArguments(['-c', 'python3 {}'.format(script)])
            self._processes.append(process)

        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.WAVE_OUTPUT_FILENAME = "file.wav"

        self.font = QtGui.QFont()
        self.font.setFamily("Trebuchet MS")
        self.font.setPointSize(15)
        self.status.setFont(self.font)
        self.startApp()
        self.stopApp()
        self.exitapp()
        self.margincalc()
        self.seccals()
        self.onseparateclick()
        self.onshowclicked()
        self.onrecordclicked()
        # self.RECORD_SECONDS = self.ip_rec.value()
        # print(self.RECORD_SECONDS)

    def record(self):
        self.RECORD_SECONDS = self.ip_rec.value()
        self.audio = pyaudio.PyAudio()
        # start Recording
        self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                      rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        print("recording...")
        self.texts = "Recording started"
        self.status.setText(self.texts)
        self.status.show()
        self.frames = []
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            self.data = self.stream.read(self.CHUNK)
            self.frames.append(self.data)
        self.status.clear()
        self.texxtt = "Done recording for {} secs".format(self.ip_rec.value)
        self.status.setText(self.texxtt)
        print("finished recording")
        # stop Recording
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        self.waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        self.waveFile.setnchannels(self.CHANNELS)
        self.waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        self.waveFile.setframerate(self.RATE)
        self.waveFile.writeframes(b''.join(self.frames))
        self.waveFile.close()

    def onrecordclicked(self):
        self.rec_start.clicked.connect(self.record)

    def on_readyReadStandardOutput(self):
        self.output = self.sender().readAllStandardOutput()
        print(self.output)

    def seccals(self):
        self.ip_rec.valueChanged.connect(self.value_dialchange)
        self.ip_rec.setMinimum(15)
        self.ip_rec.setMaximum(30)
        self.RECORD_SECONDS = self.ip_rec.value()

    def margincalc(self):
        self.margin_per.setMinimum(1)
        self.margin_per.setMaximum(10)
        self.margin_har.setMinimum(1)
        self.margin_har.setMaximum(10)
        self.margin_per.valueChanged.connect(self.valuechange)
        self.margin_har.valueChanged.connect(self.valuechange)
        self.RECORD_SECONDS = self.ip_rec.value()

    def value_dialchange(self):
        self.recop.setTextColor(QtGui.QColor(154, 0, 255))
        self.recop.setText(str(self.ip_rec.value()) + " secs")

    def valuechange(self):
        self.marginvalue_har.setTextColor(QtGui.QColor(255, 150, 0))
        self.marginvalue_per.setTextColor(QtGui.QColor(255, 150, 0))
        self.font = QtGui.QFont()
        self.font.setFamily("Trebuchet MS")
        self.font.setPointSize(15)
        self.marginvalue_har.setFont(self.font)
        self.marginvalue_per.setFont(self.font)
        self.marginvalue_har.setText(str(self.margin_har.value()))
        self.marginvalue_per.setText(str(self.margin_per.value()))

    def hpssop(self):
        self.file = "file.wav"
        self.y, self.sr = librosa.load(self.file)
        self.margin_harms = self.margin_har.value()
        self.margin_pers = self.margin_per.value()
        self.harmonic, self.percussive = librosa.effects.hpss(self.y,
                                                              margin=(self.margin_harms, self.margin_pers))
        librosa.output.write_wav("harmonic.wav", self.harmonic, self.sr)
        librosa.output.write_wav("percussive.wav", self.percussive, self.sr)
        self.status.setTextColor(QtGui.QColor(0, 0, 255))
        self.text = "Done Separating"
        self.status.setText(self.text)

    def onseparateclick(self):
        self.hpss.clicked.connect(self.hpssop)

    def onshowclicked(self):
        self.plot_hpss.clicked.connect(self.plots)

    def plots(self):
        self.file = "file.wav"
        self.y, self.sr = librosa.load(self.file)
        self.stft = librosa.stft(self.y)
        self.stft_harmonic, self.stft_percussive = librosa.decompose.hpss(self.stft)
        self.ref = np.max(np.abs(self.y))
        plt.figure(figsize=(12, 8))

        plt.subplot(3, 1, 1)
        librosa.display.specshow(librosa.amplitude_to_db(self.stft, ref=self.ref), y_axis='log')
        plt.colorbar()
        plt.title('Full spectrogram')

        plt.subplot(3, 1, 2)
        librosa.display.specshow(librosa.amplitude_to_db(self.stft_harmonic, ref=self.ref), y_axis='log')
        plt.colorbar()
        plt.title('Harmonic spectrogram')

        plt.subplot(3, 1, 3)
        librosa.display.specshow(librosa.amplitude_to_db(self.stft_percussive, ref=self.ref), y_axis='log', x_axis='time')
        plt.colorbar()
        plt.title('Percussive spectrogram')
        plt.tight_layout()
        self.status.setTextColor(QtGui.QColor(255, 100, 255))
        self.text = "Plotting Done"
        self.status.setText(self.text)
        plt.show()

    def startApp(self):
        for process in self._processes:
            self.start.clicked.connect(process.start)
            self.start.clicked.connect(self.onstartclicked)

    def onstartclicked(self):
        self.status.setTextColor(QtGui.QColor(0, 255, 0))
        self.text = "Started Visuals"
        self.status.setText(self.text)

    def stopApp(self):
        for process in self._processes:
            self.stop.clicked.connect(process.kill)
            self.stop.clicked.connect(self.onstopclicked)

    def onstopclicked(self):
        self.status.setTextColor(QtGui.QColor(250, 0, 0))
        self.text = "Stopped Visuals"
        self.status.setText(self.text)

    def exitapp(self):
        self.exit.clicked.connect(self.close)

    def closeEvent(self, event):
        for script in self._scripts:
            QtCore.QProcess.startDetached("bash", ["-c", "pkill -f {}".format(script)])
        super(MainApp, self).closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainApp()
    w.show()
    sys.exit(app.exec_())


