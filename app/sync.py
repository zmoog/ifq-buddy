import logging

from datetime import date
from ifq import Scraper

from app.settings import OC_URL, OC_USERNAME, OC_PASSWORD, OC_FILE_PATTERN
import owncloud


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

        # TODO: move to a separate function
        oc = owncloud.Client(OC_URL)
        oc.login(OC_USERNAME, OC_PASSWORD)
        oc.put_file(OC_FILE_PATTERN.format(day=day), local_path)
