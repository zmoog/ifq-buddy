import logging
import owncloud
from datetime import date

from app.settings import OC_URL, OC_USERNAME, OC_PASSWORD, OC_FILE_PATTERN

class OwncloudUploader: 

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.client = owncloud.Client(OC_URL)

    def upload(self, source_file, day: date):
        """Upload a file to Owncloud/Nextcloud"""

        self.client.login(OC_USERNAME, OC_PASSWORD)
        dest_file = OC_FILE_PATTERN.format(day=day)
        self.client.put_file(dest_file, source_file)
        
        self.logger.info(f'File {dest_file} successfully uploaded')