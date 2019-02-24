from .base_wave import BaseWave


class CompoundWave(BaseWave):

  def __init__(self):
    self.waves = []

  @property
  def amplitude(self):
    return sum(wave.amplitude for wave in self.waves)

  @classmethod
  def fromDict(cls, wave_type, wave_data):
    self = CompoundWave()
    for key, value in wave_data.items():
      self.waves.append(wave_type(key, value))
    return self

  def addWave(self, wave):
    self.waves.append(wave)

  def sample(self, t):
    return sum(wave.sample(t) for wave in self.waves)
