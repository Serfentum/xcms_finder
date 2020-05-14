import argparse


# https://stackoverflow.com/questions/3853722/python-argparse-how-to-insert-newline-in-the-help-text
class BlankLinesHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def _split_lines(self, text, width):
        return text.splitlines()
