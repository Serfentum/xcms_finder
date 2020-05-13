import tarfile

from pathlib import Path


def tar_repo(path):
    """
    Archive and compress dir into tar.gz
    :param path: str - path to the directory to archive
    :return:
    """
    # Construct tar path
    tar_name = str(path) + '.tar.gz'
    path = Path(path).expanduser()
    
    with tarfile.open(tar_name, mode='x:gz') as tar:
        tar.add(path, arcname=path.name)

    # arcname = os.path.basename(include_dir)
    
    print(f'Archive tar.gz at {tar_name}')


if __name__ == '__main__':
    
    path = '/home/arleg/skoltech/aspire/server/different_xcms/3.0.0'
    
    tar_repo(path=path)
