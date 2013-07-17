
class JsonConverter(object):

    def convert(self, data):
        header, rows = data[0], data[1:]

        def row_to_dict(row):
            return dict(zip(header, row))

        return map(row_to_dict, rows)      

