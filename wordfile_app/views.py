from django.http import FileResponse, HttpResponse
from rest_framework.views import APIView
from docx import Document
import pandas as pd
import json
import os

class WordFileView(APIView):
    def post(self, request, format=None):
        # Get JSON data from request
        data = json.loads(request.body)

        # Create a Document
        doc = Document()

        # Add data to Document
        for key, value in data.items():
            doc.add_paragraph(f"{key}: {value}")

        # Ensure 'temp' directory exists
        os.makedirs('temp', exist_ok=True)

        # Save Document
        file_path = os.path.join('temp', 'output.docx')
        doc.save(file_path)

        # Append data to Excel file
        try:
            df_new = pd.DataFrame([data])
            file_name = 'data.xlsx'
            if os.path.isfile(file_name):
                df_old = pd.read_excel(file_name)
                df_new = pd.concat([df_old, df_new])
            df_new.to_excel(file_name, index=False)
        except Exception as e:
            return HttpResponse(f"Failed to append data to Excel file: {str(e)}")

        # Return file as response
        try:
            response = FileResponse(open(file_path, 'rb'), content_type='application/msword')
            response['Content-Disposition'] = f'attachment; filename="output.docx"'
            return response
        except Exception as e:
            return HttpResponse(f"Failed to return file: {str(e)}")
