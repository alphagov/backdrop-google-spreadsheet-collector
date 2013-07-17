
class ListConverter(object):

    def to_dict(self, data):
        header, rows = data[0], data[1:]

        def maybe_convert_to_number(s):
            try:
                return int(s)
            except (ValueError, TypeError):
                return s

        def row_to_dict(row):
            converted_row = map(maybe_convert_to_number, row)
            return dict(zip(header, converted_row))

        return map(row_to_dict, rows)      

