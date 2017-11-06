import logging
import requests
import time

logger = logging.getLogger(__name__)


class Scrapper(object):
    def __init__(self, skip_objects=None):
        self.skip_objects = skip_objects

    def scrap_process(self, storage):

        # Each request gets 100 matches, we need 10000
        url = 'https://api.opendota.com/api/proMatches'
        matches_limit = 10000
        matches_per_request = 100
        less_than_match_id = 0
        scraped_matches = 0
        while  scraped_matches < matches_limit:
            current_url = url
            if scraped_matches != 0:
                current_url += '?less_than_match_id=' + str(less_than_match_id)

            response = requests.get(current_url)
            if not response.ok:
                logger.error(response.text)
                # then continue process, or retry, or fix your code
            else:
                data = response.text

                line = [current_url + '\t' + data.replace('\n', '')]

                if scraped_matches == 0:
                    storage.write_data(line)
                else:
                    storage.append_data(line)

                scraped_matches += 100
                less_than_match_id = response.json()[-1]['match_id']
                time.sleep(4)