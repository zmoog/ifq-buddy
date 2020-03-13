import logging

from datetime import date
from ifq import Scraper


class SyncTask:
    """
    Handle the download and upload of the latest
    IFQ issue in PDF format.
    """

    def __init__(self, scraper: Scraper):
        self.logger = logging.getLogger(__name__)
        self.scraper = scraper

    def run(self, day: date):
        """Syncs the PDF file published on the `day`."""
        local_path = self.scraper.download_pdf(day)
        self.logger.info(f'File {local_path} downloaded successfully')

        # TODO: and now you do something with the downloaded file.
