import argparse

from argparse_formatter import BlankLinesHelpFormatter


def parsing():
    """
    Parser function
    :return: argparse.Namespace - arguments for further work
    """
    description = '''
    Application which restore desired version of xcms
    
    usage:
    xcms_finder.py -p path -v version
    or
    python xcms_finder.py -p path -v version
    
    where
    xcms_finder.py - name of our program
    path - path on your computer where the xcms repository will be stored
    version - valid xcms version like 2.99.6 or 3.0.0
    python - just your python =)
    
    Also you can specify xcms repo url, but it points to xcms repo - change is unlikely
    
    After that you'll see list of passing versions until program will hit specified version, or you'll face an error
    If you have an error and there is no answer about it in my repository, please write to me about it - tetpapx@bk.ru
    
    After normal work you'll find tar.gz archive with desired xcms version in the specified by path directory
    '''
    
    # Parser initialization
    parser = argparse.ArgumentParser(description=description,
                                     epilog='Goodbye',
                                     formatter_class=BlankLinesHelpFormatter)
    
    # Arguments
    parser.add_argument('-p', '--path',
                        help='absolute or relative path where to store xcms repo locally, default - in current directory',
                        metavar='<path where to store repo>',
                        type=str,
                        default='.')
    parser.add_argument('-v', '--version',
                        help='desired version of xcms',
                        metavar='<desired version of xcms>',
                        type=str,
                        required=True)
    parser.add_argument('-r', '--repo-clone-url',
                        help='url with xcms repository, default - https://github.com/sneumann/xcms.git',
                        metavar='<xcms repository url>',
                        type=str,
                        default='https://github.com/sneumann/xcms.git')

    # Parse arguments
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    parsing()
