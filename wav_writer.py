import wave, array, math

class WavWriter():

  def __init__(self, file_name, wave_func, duration, smooth=False, volume=0.5, channels=1, dataSize=2, sampleRate=44100):

    self.file_name = file_name
    self.wave_func = wave_func
    self.duration = duration

    self.smooth = smooth
    self.volume = volume
    self.numChan = channels
    self.dataSize = dataSize
    self.sampleRate = sampleRate

  def write(self):
    numSamples = self.sampleRate * self.duration
    data = array.array('h')

    with wave.open(self.file_name, 'wb') as f:
      f.setparams((self.numChan, self.dataSize, self.sampleRate, 0, "NONE", "Uncompressed"))

      for t in range(numSamples):
        sample = 32767 * self.volume
        sample *= (math.pow(math.sin((math.pi/self.duration) * t/self.sampleRate), 1/2) if self.smooth else 1)
        sample *= self.wave_func.sample(t/self.sampleRate)
        sample /= self.wave_func.amplitude
        data.append(int(sample))
      f.writeframes(data.tostring())

    print('done writing', self.file_name)
