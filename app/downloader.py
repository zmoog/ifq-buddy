import logging
from datetime import date
from ifq import Scraper

from app.settings import IFQ_USERNAME, IFQ_PASSWORD

class IFQDownloader:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.scraper = Scraper(IFQ_USERNAME, IFQ_PASSWORD)

    def download(self, day: date):
        """Downloads the PDF file published on the `day`"""

        local_path = self.scraper.download_pdf(day)
        self.logger.info(f'File {local_path} downloaded successfully')
        return local_path
