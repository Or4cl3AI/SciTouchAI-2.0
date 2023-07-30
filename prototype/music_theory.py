```python
import numpy as np
from scipy.signal import spectrogram

def createExperience(user_input):
    """
    Function to create an engaging user experience using principles of music theory.
    This function uses the user input to generate a unique sound pattern.
    """
    # Convert user input into a numpy array
    user_input_array = np.array(list(map(int, user_input.split())))

    # Generate a spectrogram from the user input array
    frequencies, times, Sxx = spectrogram(user_input_array)

    # Normalize the spectrogram
    Sxx_normalized = Sxx / np.max(Sxx)

    # Use the normalized spectrogram to generate a sound pattern
    sound_pattern = np.sin(2 * np.pi * frequencies * times)

    # Return the sound pattern
    return sound_pattern
```