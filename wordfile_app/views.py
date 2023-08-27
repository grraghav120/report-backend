from django.http import FileResponse, HttpResponse
from rest_framework.views import APIView
from docx import Document
import pandas as pd
import json
import os
# for pdf
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def data_collect_in_excel_file(data):
    df_new = pd.DataFrame([data])
    file_name = 'data.xlsx'
    if os.path.isfile(file_name):
        df_old = pd.read_excel(file_name)
        df_new = pd.concat([df_old, df_new])
    df_new.to_excel(file_name, index=False)


class WordFileView(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)
        # print(data)

        # generate docx from data

        # doc = Document()
        # doc.add_heading(data['uhid'], level=1)
        # doc.add_paragraph(data['FullName'])
        # response = HttpResponse(content_type='application/msword')
        # response['Content-Disposition'] = 'attachment; filename="document.docx"'
        # doc.save(response)
        # return response
        
        # generate pdf from report.html

        pdf = render_to_pdf('wordfile_app/report.html', data)
        if pdf:
            # Set response headers for download
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="Report.pdf"'
            data_collect_in_excel_file(data)
            return response
        else:
            return HttpResponse("Error generating PDF", status=500)


        # waste code start


        # try:
        #     df_new = pd.DataFrame([data])
        #     file_name = 'data.xlsx'
        #     if os.path.isfile(file_name):
        #         df_old = pd.read_excel(file_name)
        #         df_new = pd.concat([df_old, df_new])
        #     df_new.to_excel(file_name, index=False)
        # except Exception as e:
        #     return HttpResponse(f"Failed to append data to Excel file: {str(e)}")

       
        # try:
        #     response = FileResponse(open(file_path, 'rb'), content_type='application/msword')
        #     response['Content-Disposition'] = f'attachment; filename="output.docx"'
        #     return response
        # except Exception as e:
        #     return HttpResponse(f"Failed to return file: {str(e)}")
