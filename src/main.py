from realtime import process_realtime
from visualization import plot_signals

original, filtered, fs = process_realtime()

plot_signals(original, filtered)

print("Real-time processing complete")
