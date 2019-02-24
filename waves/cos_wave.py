from .base_wave import BaseWave
import math

class CosWave(BaseWave):

  def __init__(self, freq, amp):
    super().__init__(freq, amp)

  def sample(self, t):
    return self.amplitude * math.cos(2 * math.pi * t * self.frequency)
