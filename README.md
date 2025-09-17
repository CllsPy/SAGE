## Project Overview

<img width="831" height="463" alt="image" src="https://github.com/user-attachments/assets/3c540f09-121f-41fb-ad56-c9c824ecdb99" />


This project provides a streamlined method for summarizing scientific articles using advanced natural language processing capabilities. By leveraging Google Generative AI and fine-tuned prompt engineering, the application generates structured summaries of uploaded scientific articles.


## Features

- **Automatic Summarization:** Converts uploaded articles into structured summaries.
- **Detailed Outputs:** Includes key findings, objectives, methods, results, conclusions, and key concepts.
- **User-Friendly Input:** Users can upload files for seamless summarization.
- **Powered by Generative AI:** Utilizes Google's Gemini AI model for content generation.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- `pip` (Python package manager)

### Dependencies
Install the required libraries using:
```bash
pip install streamlit python-dotenv google-generativeai PyPDF2
```



## Usage

### Setting Up API Key
1. Create a `.env` file in the project directory.
2. Add your Google Generative AI API key to the file:
   ```plaintext
   API_KEY=your_api_key_here
   ```

### Running the Application
1. Save the code in a Python script file (e.g., `app.py`).
2. Run the script:
   ```bash
   python app.py
   ```

### Workflow
1. Upload a scientific article file (PDF or text format).
2. The program will process the file and generate a structured summary.


## Example Prompt

The summarization prompt used in the application ensures a consistent structure:
```
# Structured Summary

# Key Findings

# Objectives

# Methods

# Results

# Conclusions

# Key Concepts
```


## Code Explanation

### Environment Variables
The `.env` file is used to securely load the API key.

### Functions
- `summarize(file)`: Generates the summary using the Google Generative AI model.
- `main()`: Entry point of the application.



## Contributing
Contributions are welcome. Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.


## To-do

- [ ] translate text - ptbr
- [ ] add copy button
- [ ] add tutorial
- [ ] add loading bar
