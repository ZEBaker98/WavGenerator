from wav_writer import WavWriter

from waves.compound_wave import CompoundWave
from waves.sin_wave import SinWave
from waves.cos_wave import CosWave
from waves.pulse_wave import PulseWave

from hydrogen import hydrogen

def main():

  hydrogen_a4_func = CompoundWave.fromDict(SinWave, hydrogen(440))
  WavWriter('hydrogen_A4.wav', hydrogen_a4_func, 3, smooth=True).write()

  hydrogen_a4_func = CompoundWave.fromDict(SinWave, {**hydrogen(523.25), **hydrogen(659.25), **hydrogen(783.99)})
  WavWriter('hydrogen_C4_triad.wav', hydrogen_a4_func, 3, smooth=True).write()

  a4_func = SinWave(440, 1)
  WavWriter('A4.wav', a4_func, 3, smooth=True).write()

  a4_a5_func = CompoundWave.fromDict(SinWave, {440:1, 880:1})
  WavWriter('A4+A5.wav', a4_a5_func, 3, smooth=True).write()

  c4_triad_func = CompoundWave.fromDict(SinWave, {523.25:1, 659.25:1, 783.99:1})
  WavWriter('C4_triad.wav', c4_triad_func, 3, smooth=True).write()

  a4_pulse_50_func = PulseWave(440, 0.5, 0.5)
  WavWriter('a4_pulse_50.wav', a4_pulse_50_func, 3, smooth=True).write()

  a4_pulse_25_func = PulseWave(440, 0.5, 0.25)
  WavWriter('a4_pulse_25.wav', a4_pulse_25_func, 3, smooth=True).write()

  a4_pulse_12_func = PulseWave(440,0.5, 0.125)
  WavWriter('a4_pulse_12.wav', a4_pulse_12_func, 3, smooth=True).write()

if __name__ == "__main__":
  main()
