import matplotlib.pyplot as plt
import numpy as np

# 1. Setup Timeline (Centered around the 3600s mark)
t = np.linspace(3590, 3610, 5000)

# 2. Create the "Normal" N3 Delta Wave
delta_wave = 3 * np.sin(2 * np.pi * 1.2 * t)

# 3. Create Spikes with different "Chances" (Amplitudes)
# Spike 1: Before 3600 (Low chance -> Small amplitude)
spike_loc_low = 3595 
spike_low = 2 * np.exp(-((t - spike_loc_low)**2) / (2 * 0.05**2))

# Spike 2: After 3600 (High chance -> Large amplitude)
spike_loc_high = 3605
spike_high = 12 * np.exp(-((t - spike_loc_high)**2) / (2 * 0.05**2))

# 4. Combine Signals
eeg_combined = delta_wave + spike_low + spike_high + np.random.normal(0, 0.4, 5000)

# 5. Plotting
plt.figure(figsize=(12, 5))
plt.plot(t, eeg_combined, color='darkred', label='EEG Signal')

# Visual marker for the threshold
plt.axvline(3600, color='blue', linestyle='--', label='3600s (1 Hour) Threshold')
plt.axvspan(3600, 3610, color='red', alpha=0.1, label='High Sleepwalking Risk')

plt.title('Sleepwalking Arousal Probability Shift at 3600s', fontsize=14)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude (µV)')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.2)
plt.show()

plt.savefig('my_eeg_result.pdf', dpi=300, bbox_inches='tight')
plt.show()