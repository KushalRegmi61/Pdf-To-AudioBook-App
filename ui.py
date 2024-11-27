from tkinter import *
from tkinter import filedialog, messagebox
from gtts import gTTS
from PyPDF2 import PdfReader


class PdfToAudiobook:
    def __init__(self):
        self.root = Tk()
        self.root.title("PDF to Audiobook") # setting the title of the window
        self.root.config(padx=50, pady=50) # padding
        self.root.geometry('600x400') # setting the size of the window

    #TODO: INITIALIZING THE VARIABLES
        self.text = "" # variable to store the extracted text
        self.file_path = "" # path to the pdf file
        self.audio_path = "" # path to save the audio file
        self.is_saved = 1 # flag to check if the audio file is saved
        self.is_converted = 0 # flag to check if the pdf is converted to audio

    #TODO:   creating the labels and buttons for the app
        # Upload file button 
        self.upload_button = Button(self.root, text="Upload PDF", command=self.upload_pdf, font=("Times New Roman", 13, "bold"))
        self.upload_button.grid(row=0, column=0, pady=10)

        # creating a canvas for the text
        self.canvas = Canvas(self.root, width=500, height=200, bg="#375362")
        self.canvas.grid(row=1, column=0, columnspan=2)

        # adding the text to the canvas
        self.canvas_text = self.canvas.create_text(
                                                    250, 
                                                    100, 
                                                    text=(
                                                        "📂 Upload a PDF file to start your journey! 📚\n\n"
                                                        "🎧 Turn your documents into audiobooks effortlessly.\n\n"
                                                        "🚀 Ready? Click 'Upload PDF' to begin!"
                                                    ), 
                                                    font=("Times New Roman", 14, "bold"), 
                                                    fill="white", 
                                                    anchor=CENTER
                                                )

        # Quit button
        self.quit_button = Button(self.root, text="Quit", command=self.quit, font=("Times New Roman", 13, "bold"))
        self.quit_button.grid(row=0, column=1 ,pady=10)

        #  converting the pdf to audio
        self.convert_button = Button(self.root, text="Convert to Audio", command=self.convert_pdf_to_audio, font=("Times New Roman", 13, "bold"))
        self.convert_button.grid(row=2, column=0, pady=10)

        # save audio button
        self.save_button = Button(self.root, text="Save Audio", command=self.save_audio, font=("Times New Roman", 13, "bold"))
        self.save_button.grid(row=2, column=1, pady=10)

        #disabling the buttons
        self.convert_button.config(state=DISABLED)
        self.save_button.config(state=DISABLED)
    
        # runnig the app
        self.root.mainloop()

    #TODO: function to convert the pdf to audio
    def upload_pdf(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])  # getting the file path
        if not self.file_path:
            messagebox.showerror("Error", "No file selected")  # error message if no file is selected
        else:
            messagebox.showinfo("Success", "File uploaded successfully")  # success message if file is uploaded
            self.convert_button.config(state=NORMAL)  # enabling the convert button

            # Professional multi-line display
            new_text = (
                "✅ File uploaded successfully!\n\n"
                "👉 Now click the 'Convert to Audio' button\n"
                "   to create your audiobook."
            )

            # Update the canvas text
            self.canvas.itemconfig(
                self.canvas_text,
                text=new_text,
                font=("Times New Roman", 14, "bold"),
                fill="white",
                justify="center",  # Center-align text
            )

            self.is_saved = 0  # Set the flag to indicate unsaved changes

            # changing the upload button text
            self.upload_button.config(text="Add New PDF")

    def convert_pdf_to_audio(self):
        if self.is_converted: # checking if the pdf is already converted
            messagebox.showwarning("Warning", "PDF is already converted to audio.")
            return
        else:
            self.is_converted = 1  # Set the flag to indicate that the PDF is converted to audio
            try:
                # Open the PDF file and extract text
                pdf = PdfReader(self.file_path)
                self.text = ""  # variable to store the extracted text

                for page in pdf.pages:  # loop through all pages in the PDF
                    self.text += page.extract_text()

                # Creating the audio file using gTTS
                self.tts = gTTS(self.text)

                # Check if the audio file object is successfully created
                if self.tts:
                    # Update canvas with a success message
                    new_text = (
                        "🎉 Audio file created successfully!\n\n"
                        "👉 Click the 'Save Audio' button to save your audiobook.\n"
                        "   Enjoy listening to your content!"
                    )
                    self.canvas.itemconfig(
                        self.canvas_text,
                        text=new_text,
                        font=("Times New Roman", 14, "bold"),
                        fill="white",
                        justify="center",
                    )

                    # Enable the Save button
                    self.save_button.config(state=NORMAL)

                    # Show a success message box
                    messagebox.showinfo("Success", "Audio file created successfully! Click 'Save Audio' to save it.")

                else:
                    # Update canvas with an error message
                    new_text = "❌ Failed to create audio file. Please try again."
                    self.canvas.itemconfig(
                        self.canvas_text,
                        text=new_text,
                        font=("Times New Roman", 14, "bold"),
                        fill="red",
                        justify="center",
                    )
                    messagebox.showerror("Error", "Audio file not created.")

            except Exception as e:
                # Handle exceptions and display an error message
                error_message = f"An error occurred: {e}"
                self.canvas.itemconfig(
                    self.canvas_text,
                    text="❌ Error: Unable to process the PDF.\nPlease check the file and try again.",
                    font=("Times New Roman", 14, "bold"),
                    fill="red",
                    justify="center",
                )
                messagebox.showerror("Error", error_message)


        # Function to save the audio file
    def     save_audio(self):
        if self.is_saved:
            messagebox.showwarning("Warning", "No changes to save.")
            return
        else:

            try:
                # Prompt user to choose save location
                self.audio_path = filedialog.asksaveasfilename(
                    defaultextension=".mp3",
                    filetypes=[("MP3 files", "*.mp3")],
                    initialdir="~/PROJECTS/PDF-TO-AUDIOBOOK",
                    title="Save Audio File"
                )

                if self.audio_path:
                    # Save the audio file
                    self.tts.save(self.audio_path)

                    # Update canvas with success message
                    new_text = (
                        "✅ Audio file saved successfully!\n\n"
                        "🎧 Click on Add New to new .pdf file"
                        
                    )
                    self.canvas.itemconfig(
                        self.canvas_text,
                        text=new_text,
                        font=("Times New Roman", 14, "bold"),
                        fill="white",
                        justify="center",
                    )

                    # Display a success message box
                    messagebox.showinfo("Success", "Audio file saved successfully!")

                    # Set the flag to indicate saved changes
                    self.is_saved = 1

                else:
                    # Handle case when user cancels the save dialog
                    self.canvas.itemconfig(
                        self.canvas_text,
                        text="❌ Save operation canceled. Audio file not saved.",
                        font=("Times New Roman", 14, "bold"),
                        fill="red",
                        justify="center",
                    )
                    messagebox.showwarning("Warning", "Audio file not saved.")

            except Exception as e:
                # Handle exceptions and display an error message
                error_message = f"An error occurred: {e}"
                self.canvas.itemconfig(
                    self.canvas_text,
                    text="❌ Error: Unable to save the audio file.\nPlease try again.",
                    font=("Times New Roman", 14, "bold"),
                    fill="red",
                    justify="center",
                )
                messagebox.showerror("Error", error_message)


    #TODO: Method to quit the application
    def quit(self):
        if self.is_saved:   
            self.root.quit() # quitting the application
        else:
            if messagebox.askyesno("Warning", "You have unsaved changes. Do you want to quit?"):
                self.root.quit()



# PdfToAudiobook() # creating the object of the PdfToAudiobook class