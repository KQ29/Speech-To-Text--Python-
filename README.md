# Speech-To-Text (Python)

This Python project allows users to convert speech to text using their microphone and translate the recognized text into **English** or **French** using the Google Translate API. The program supports real-time speech recognition and can listen for up to 60 seconds of input. Users can stop the program by pressing '1' at any point.

## Features

- Real-time speech recognition via the microphone.
- Converts recognized speech to text using Google's Web Speech API.
- Automatically translates the recognized text into **English** or **French** using the Google Translate API.
- User-friendly option to stop the program by pressing '1'.
- Supports up to 60 seconds of speech input per phrase.

## Installation

### Requirements

- Python 3.x
- pip (Python package manager)
- A working microphone

### Libraries

The following Python libraries are required to run the project:

- `SpeechRecognition` - for speech-to-text.
- `googletrans` - for text translation.
- `pyaudio` - for handling microphone input.

### Installation Steps

1. Clone this repository or download the project files:
    ```bash
    git clone https://github.com/KQ29/speech-to-text-translation.git
    cd speech-to-text-translation
    ```

2. Create and activate a virtual environment (recommended):
    - **On macOS/Linux**:
        ```bash
        python3 -m venv env
        source env/bin/activate
        ```
    - **On Windows**:
        ```bash
        python -m venv env
        .\env\Scripts\activate
        ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, manually install the required libraries:
    ```bash
    pip install SpeechRecognition googletrans==4.0.0-rc1 pyaudio
    ```

### Dependencies

- `SpeechRecognition`: Provides functionality for recognizing speech via the microphone.
- `googletrans`: A Python library that interfaces with the Google Translate API for translation.
- `PyAudio`: Used for capturing microphone input.

## Usage

1. Run the script to start the speech recognition and translation process:
    ```bash
    python main.py
    ```

2. The program will prompt you to speak into your microphone. You will have up to 60 seconds to speak.
3. After recognizing the speech, it will automatically translate the text to English or French (depending on the code setup) and display the results.
4. If you'd like to stop the program, press `1` when prompted.

## Customization

- You can adjust the `phrase_time_limit` and `timeout` settings to change how long the program listens for speech and how long it waits before timing out.
- The translation is set to **English** (`'en'`) or **French** (`'fr'`). You can modify the `translate_text()` function to support other languages.

## Example

```bash
Please speak clearly into the microphone...
Recognizing speech...
Translated Text: Bonjour, comment ça va?
Final Translated Text: Hello, how are you?
Press '1' to stop the program, or any other key to continue: 1
Exiting program...
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact

If you have any questions or need help, feel free to contact me at [kamronbekibra2005@gmail.com].

