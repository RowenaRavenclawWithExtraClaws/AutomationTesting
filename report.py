import fpdf
from fpdf import FPDF


class Report:  # A class for constructing bug reports with basic information and a screenshot which shows where the error occurs.

    @staticmethod
    # Basic bug information constructor.
    def constructInfo(id, name, submitDate, summary, expectedResult, actualResult):
        info = {}

        info['ID'] = id
        info['Name'] = name
        info['Submit Date'] = str(submitDate)
        info['Summary'] = summary
        info['Expected Result'] = expectedResult
        info['Actual Result'] = actualResult

        return info

    @staticmethod
    def generateReportAsTextFile(info):
        try:
            with open('bugReports/textReports/bugReport' + str(info['ID']) + '.txt', 'w') as outFile:
                for item in info:
                    outFile.write(item + ': ' + str(info[item]))
                    outFile.write('\n')
        except Exception as e:
            print(str(e))

    @staticmethod
    # This method generates the complete bug report (meta-data and a screenshot).
    def generateReport(info):
        imgPath = 'bugReports/screenshots/test' + str(info['ID']) + '.png'
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        colWidth = pdf.w / 2.5
        rowHeight = pdf.font_size * 2

        # populating a basic pdf table with the bug meta-data.
        for item in info:
            pdf.cell(colWidth, rowHeight,
                     txt=item, border=1)
            pdf.cell(colWidth, rowHeight,
                     txt=str(info[item]), border=1)
            pdf.ln(rowHeight)

        # Add the screenshot to the pdf.
        pdf.image(imgPath, w=pdf.w / 1.5, h=pdf.h / 4.0)

        pdf.output('bugReports/completeReports/bugReport' +
                   str(info['ID']) + '.pdf')

    @staticmethod
    def genrateBugReport(id, name, submitDate, summary, expectedResult, actualResult):
        info = Report.constructInfo(
            id, name, submitDate, summary, expectedResult, actualResult)

        Report.generateReportAsTextFile(info)
        Report.generateReport(info)
