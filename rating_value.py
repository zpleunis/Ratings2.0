import re

class RatingValue(object):
    ratval_re = re.compile(r"Rating name \(version\): (?P<name>.*?) " \
                            r"\(v(?P<version>\d+?)\)\n" \
                            r"Description: (?P<descr>.*?)\n" \
                            r"Value: (?P<value>.*?)$", \
                            flags=re.MULTILINE | re.DOTALL)

    def __init__(self, name, version, description, value):
        self.name = name
        self.version = version
        self.description = description
        self.value = value

    def __str__(self):
        text  = "Rating name (version): %s (v%d)\n" % (self.name, self.version)
        text += "Description: %s\n" % self.description
        text += "Value: %.12g" % self.value
        return text


def parse_string(string):
    """Parse a string for rating values and return a list
        of RatingValue objects.

        Input:
            string: The string to parse.

        Output:
            ratvals: A list of RatingValue objects gleaned from the string.
    """
    matches = RatingValue.ratval_re.finditer(string)
    ratvals = []
    for match in matches:
        grps = match.groupdict()
        ratvals.append(RatingValue(grps['name'], int(grps['version']), \
                                    grps['descr'], float(grps['value'])))
    return ratvals
