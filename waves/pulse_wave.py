from .base_wave import BaseWave
import math

class PulseWave(BaseWave):

  def __init__(self, freq, amp, duty_cycle=0.5):
    super().__init__(freq, amp)
    self.cutoff = math.cos(math.pi * duty_cycle)

  def sample(self, t):
    return self.amplitude if ((math.sin(2 * math.pi * t * self.frequency) > self.cutoff)) else -self.amplitude
