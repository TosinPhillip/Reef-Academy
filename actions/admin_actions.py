# This file contains the actions that an admin can take on the admin page

import PyPDF2
import re

def parse_pdf(file_path):
    """
    This function allows the admin to upload a PDF file that contains the questions. It will be automatically parsed and the questions will be extracted into a dictionary to be posted on the database.

    The question will be posted in the format:
    -Question type: (Multiple choice, Fill in the gap, Theory) [QT]
    -Question itself [Q]
    -Options (If Multiple choice) [O]
    -Answer [A]
    -Explanation [E]
    -Video file (optional) [V]
    -Image/Code/Equation (Optional) [I]
    -Availability tag (Free or requires login) [AT]


    The dictionary will be returned in the format:
    {Q:[QT, O, A, E, V, I, AT]
    }
    
    """
    
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    questions = {}

    current_question = None
    current_info = {}

    for page in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page]
        text = page_obj.extract_text()
        lines = text.split('\n')

        for line in lines:
            line = line.strip()

            # Check for question type
            match = re.match(r'QT: (.*)', line)
            if match:
                current_info['type'] = match.group(1)
                continue

            # Check for question
            match = re.match(r'Q: (.*)', line)
            if match:
                current_question = match.group(1)
                current_info = {}
                continue

            # Check for options
            match = re.match(r'O: (.*)', line)
            if match:
                if 'options' not in current_info:
                    current_info['options'] = []
                current_info['options'].append(match.group(1))
                continue

            # Check for answer
            match = re.match(r'A: (.*)', line)
            if match:
                current_info['answer'] = match.group(1)
                continue

            # Check for explanation
            match = re.match(r'E: (.*)', line)
            if match:
                current_info['explanation'] = match.group(1)
                continue

            # Check for video file
            match = re.match(r'V: (.*)', line)
            if match:
                current_info['video'] = match.group(1)
                continue

            # Check for image/code/equation
            match = re.match(r'I: (.*)', line)
            if match:
                current_info['image'] = match.group(1)
                continue

            # Check for availability tag
            match = re.match(r'AT: (.*)', line)
            if match:
                current_info['availability'] = match.group(1)
                if current_question:
                    questions[current_question] = current_info
                    current_question = None
                continue

    pdf_file_obj.close()
    return questions