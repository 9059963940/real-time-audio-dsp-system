import matplotlib.pyplot as plt
import numpy as np

def plot_signals(original, filtered):
    plt.figure(figsize=(10,5))

    plt.subplot(2,1,1)
    plt.title("Original Signal")
    plt.plot(original)

    plt.subplot(2,1,2)
    plt.title("Filtered Signal")
    plt.plot(filtered)

    plt.tight_layout()
    plt.show()
