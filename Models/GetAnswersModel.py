import requests
from PyPDF2 import PdfFileReader as Reader


class GetAnswersModel:
    def get_answers(self, data):
        pdf_url = data.link
        r = requests.get(pdf_url)

        with open("static/currentfile.pdf", 'wb') as f:
            f.write(r.content)

        pdf = Reader("static/currentfile.pdf")
        pdfPage1Extract = pdf.getPage(1).extractText()
        print(pdfPage1Extract)
        try:
            pdfPage2Extract = pdf.getPage(2).extractText()
        except:
            pdfPage2Extract = ""
        answers = [
            pdfPage1Extract[pdfPage1Extract.find("\n1 ") + 3:pdfPage1Extract.find("\n1 ") + 4],
            pdfPage1Extract[pdfPage1Extract.find(" 12 ") + 4:pdfPage1Extract.find(" 12 ") + 5],
            pdfPage1Extract[pdfPage1Extract.find(" 13 ") + 4:pdfPage1Extract.find(" 13 ") + 5],
            pdfPage1Extract[pdfPage1Extract.find(" 14 ") + 4:pdfPage1Extract.find(" 14 ") + 5],
            pdfPage1Extract[pdfPage1Extract.find(" 15 ") + 4:pdfPage1Extract.find(" 15 ") + 5],
            pdfPage1Extract[pdfPage1Extract.find(" 16 ") + 4:pdfPage1Extract.find(" 16 ") + 5],
            pdfPage1Extract[pdfPage1Extract.find(" 17 ") + 4:pdfPage1Extract.find(" 17 ") + 5],
            pdfPage1Extract[pdfPage1Extract.find(" 18 ") + 4:pdfPage1Extract.find(" 18 ") + 5],
            pdfPage1Extract[pdfPage1Extract.find(" 19 ") + 4:pdfPage1Extract.find(" 19 ") + 5],
            pdfPage1Extract[pdfPage1Extract.find(" 110 ") + 5:pdfPage1Extract.find(" 110 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 111 ") + 5:pdfPage1Extract.find(" 111 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 112 ") + 5:pdfPage1Extract.find(" 112 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 113 ") + 5:pdfPage1Extract.find(" 113 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 114 ") + 5:pdfPage1Extract.find(" 114 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 115 ") + 5:pdfPage1Extract.find(" 115 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 116 ") + 5:pdfPage1Extract.find(" 116 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 117 ") + 5:pdfPage1Extract.find(" 117 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 118 ") + 5:pdfPage1Extract.find(" 118 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 119 ") + 5:pdfPage1Extract.find(" 119 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 120 ") + 5:pdfPage1Extract.find(" 120 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 121 ") + 5:pdfPage1Extract.find(" 121 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 122 ") + 5:pdfPage1Extract.find(" 122 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 123 ") + 5:pdfPage1Extract.find(" 123 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 124 ") + 5:pdfPage1Extract.find(" 124 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 125 ") + 5:pdfPage1Extract.find(" 125 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 126 ") + 5:pdfPage1Extract.find(" 126 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 127 ") + 5:pdfPage1Extract.find(" 127 ") + 6],
            pdfPage1Extract[pdfPage1Extract.find(" 128 ") + 5:pdfPage1Extract.find(" 128 ") + 6],
            pdfPage2Extract[pdfPage2Extract.find("\n29 ") + 4:pdfPage2Extract.find("\n29 ") + 5],
            pdfPage2Extract[pdfPage2Extract.find(" 130 ") + 5:pdfPage2Extract.find(" 130 ") + 6],
            pdfPage2Extract[pdfPage2Extract.find(" 131 ") + 5:pdfPage2Extract.find(" 131 ") + 6],
            pdfPage2Extract[pdfPage2Extract.find(" 132 ") + 5:pdfPage2Extract.find(" 132 ") + 6],
            pdfPage2Extract[pdfPage2Extract.find(" 133 ") + 5:pdfPage2Extract.find(" 133 ") + 6],
            pdfPage2Extract[pdfPage2Extract.find(" 134 ") + 5:pdfPage2Extract.find(" 134 ") + 6],
            pdfPage2Extract[pdfPage2Extract.find(" 135 ") + 5:pdfPage2Extract.find(" 135 ") + 6],
            pdfPage2Extract[pdfPage2Extract.find(" 136 ") + 5:pdfPage2Extract.find(" 136 ") + 6],
            pdfPage2Extract[pdfPage2Extract.find(" 137 ") + 5:pdfPage2Extract.find(" 137 ") + 6],
            pdfPage2Extract[pdfPage2Extract.find(" 138 ") + 5:pdfPage2Extract.find(" 138 ") + 6],
            pdfPage2Extract[pdfPage2Extract.find(" 139 ") + 5:pdfPage2Extract.find(" 139 ") + 6],
            pdfPage2Extract[pdfPage2Extract.find(" 140 ") + 5:pdfPage2Extract.find(" 140 ") + 6],
        ]
        for answer in answers:
            print(answer)
        return answers
