# Cover Letter Generator

This is a Python program that generates cover letters based on your CV (Curriculum Vitae) and a LinkedIn job posting URL. The program utilizes the LLM (OpenAI API) to generate personalized and professional cover letters.

## Demo
hosted demo - https://coverlettergenerator.streamlit.app/
(you will require an open ai api key)

## Prerequisites
Before running the program, make sure you have the following prerequisites installed:

Python (version 3.7 or higher)
langchian Python SDK (to access the LLM API)
You can install the required Python packages by running the following command:

```pip install -r requirements.txt```

## Getting Started & Usage
To get started, follow these steps:

1. Clone the repository or download the source code files.
2. Install the required dependencies mentioned in the Prerequisites section.
3. Run ```streamlit run app.py``` to open the GUI.
4. Get an API Key from Open AI (free or paid)
5. Add API key to the lefthand sidebar.
6. Upload Your CV.
7. Add a Linked in Job URL(make sure that you are adding the full URL, accesibble publically. Not the url from job search window)
8. Sumbit
![Alt text](/images/image2.png)
![Alt text](/images/image.png)

The program will use your CV and the job posting URL to generate a cover letter tailored to the job requirements. 


## Customization
You can customize the generated cover letter by modifying the templates and formatting in the files. Look for the comments and placeholders to guide you in making changes according to your preferences.

## Important Note
Please note that this program utilizes the LLM (OpenAI API) to generate the cover letter content. Make sure you have appropriate access and credentials for the API. Refer to the OpenAI documentation for more information on how to set up and use the API.

## Disclaimer
This program is provided as-is without any warranty. Use it at your own risk. The authors and contributors of this program are not responsible for any misuse or consequences arising from the use of this program.

## License
This project is licensed under the MIT License. Feel free to modify and distribute it according to the terms of the license.