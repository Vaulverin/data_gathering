import json
from parsers.parser import Parser


class DataParser(Parser):

    def parse(self, data):
        """
        Parses html text and extracts field values
        :param data: gathered data
        :return: a dictionary where key is one
        of defined fields and value is this field's value
        """
        json_text = data[data.find('\t') + 1:]

        return json.loads(json_text)
