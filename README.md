# PDF to Audiobook 🎧

A Python application that converts PDF documents into audiobooks effortlessly. This tool extracts text from PDF files and transforms it into audio using Google Text-to-Speech (`gTTS`). Perfect for users who want to listen to their documents on the go.

---

## Features ✨

- 📂 **Upload PDF Files**: Easily select and upload PDF files for conversion.
- 🎧 **Convert to Audio**: Generate an audiobook from your document with a single click.
- 💾 **Save Audio File**: Save the generated audiobook as an MP3 file.
- 🖥️ **User-Friendly Interface**: Intuitive design powered by `Tkinter`.
- 🚨 **Error Handling**: Informative messages for invalid inputs or errors.

---


## Prerequisites 📋

Ensure you have the following installed on your system:

- Python 3.8 or higher
- `pip` (Python package installer)

---

## Installation 🛠️

1. Clone this repository:
   ```bash
   git clone git@github.com:KushalRegmi61/Pdf-To-AudioBook-App.git
   cd pdf-to-audiobook
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## Dependencies 📦

This project uses the following Python libraries:

- [`PyPDF2`](https://pypi.org/project/PyPDF2/): For extracting text from PDF files.
- [`gTTS`](https://pypi.org/project/gTTS/): For converting text to speech.
- [`Tkinter`](https://docs.python.org/3/library/tkinter.html): For creating the graphical user interface.

---

## Usage 🚀

1. Launch the application:
   ```bash
   python main.py
   ```

2. **Upload a PDF**:
   - Click the `Upload PDF` button and select a PDF file.

3. **Convert to Audio**:
   - After uploading, click `Convert to Audio` to generate the audiobook.

4. **Save the Audio**:
   - Click `Save Audio` to save the audiobook as an MP3 file.

5. **Quit**:
   - Click the `Quit` button to exit the application.

---

## File Structure 📂

```
📦 pdf-to-audiobook
├── MP3/                  # MP3 files folder
├── pdf_files/            # Pdf files folder
├── main.py               # Main application file
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

---

## Known Issues 🐞

- The application may not handle scanned PDFs effectively since `PyPDF2` extracts only text-based content.
- Audio playback and pause functionality are not included in this version.

---

## Future Enhancements 🚀

- 🔊 Integrate audio playback with controls (play, pause, stop).
- 🌐 Add support for multiple languages.
- 📜 Support scanned PDFs using Optical Character Recognition (OCR).

---

## Contributing 🤝

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

---



## Author ✍️

- **Your Name**  
  GitHub: [@KushalRegmi](https://github.com/KushalRegmi61)  


