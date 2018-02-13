from toxic_comment.main.models.data_points import DataPoints, Label


class DataPointsBuilder(object):

    def __init__(self, delimiter):
        self.train_data_points = DataPoints()
        self.test_data_points = DataPoints()
        self.delimiter = delimiter

    def build_and_get_train_data_points(self, file_path) -> DataPoints:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as train_file:
            train_file.readline()
            lines = train_file.readlines()
            current = 0
            while current < len(lines):
                line, current = self._get_line(lines, current)
                split_line = line.split(self.delimiter)
                toxic_id = split_line.pop(0)
                label = self._get_label(split_line)
                text = self._get_text(split_line)
                self.train_data_points.add(toxic_id, text, label)
        return self.train_data_points

    def build_and_get_test_data_points(self, file_path) -> DataPoints:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as test_file:
            test_file.readline()
            for line in test_file.readlines():
                split_line = line.split(self.delimiter)
                toxic_id = split_line.pop(0)
                text = self._get_text(split_line)
                self.test_data_points.add(toxic_id, text)
        return self.test_data_points

    @staticmethod
    def _get_text(split_line):
        text = ""
        for sub_text in split_line:
            text += sub_text
        return text

    @staticmethod
    def _get_label(split_line):
        identity_hate = int(split_line.pop())
        insult = int(split_line.pop())
        threat = int(split_line.pop())
        obscene = int(split_line.pop())
        severe_toxic = int(split_line.pop())
        toxic = int(split_line.pop())
        return Label(toxic, severe_toxic, obscene, threat, insult, identity_hate)

    def _get_line(self, lines, current):
        line = lines[current]
        while True:
            split_line = line.split(self.delimiter)
            try:
                self._get_label(split_line)
                return line, current + 1
            except:
                current += 1
                line += lines[current]
