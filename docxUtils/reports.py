import abc
import os
from StringIO import StringIO

from docx import Document
from docx.shared import Inches
from docx.enum.section import WD_ORIENT


class DOCXReport(object):

    def __init__(self, root_path, context):
        self.root_path = root_path
        self.context = context

    def build_report(self):
        """
        Build DOCX report, create content, return file in StringIO format
        """
        fn = os.path.join(self.root_path, self.get_template_fn())
        self.doc = Document(fn)
        self.create_content()

        docx = StringIO()
        self.doc.save(docx)
        docx.seek(0)

        return docx

    @abc.abstractmethod
    def get_template_fn(self):
        """
        Get Word-template filename; template should contain all Word-styles
        used in the report.
        """
        pass

    @abc.abstractmethod
    def create_content(self):
        """
        Main-method called to generate the content in a Word report
        """
        pass

    def setLandscape(self):
        """
        Set the document to landscape
        """
        section = self.doc.sections[-1]
        section.orientation = WD_ORIENT.LANDSCAPE
        section.page_width = Inches(11)
        section.page_height = Inches(8.5)

    def setMargins(self, left=None, right=None, top=None, bottom=None):
        """
        Set the margins on the page, in inches.
        """
        section = self.doc.sections[-1]
        if left:
            section.left_margin = Inches(left)
        if right:
            section.right_margin = Inches(right)
        if top:
            section.top_margin = Inches(top)
        if bottom:
            section.bottom_margin = Inches(bottom)
