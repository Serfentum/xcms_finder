from commit_analysis import find_commit
from init_repo import init_repo
from tar_repo import tar_repo


def get_xcms_version(path, version, repo_clone_url='https://github.com/sneumann/xcms.git'):
    """
    Clone xcms repo to specified path in version subdirectory,
    try to checkout to specified version
    and archive this version
    :param path: str - path, where dir with repo will be places
    :param version: str - future name of repo dir
    :param repo_clone_url: str - xcms url from gihub to clone, https://github.com/sneumann/xcms.git by default
    :return:
    """
    # Clone repo from url to specified path, dir with it will be named as version
    repo, local_repo = init_repo(repo_clone_url, path, version)
    
    # Checkout to the desired version of xcms
    try:
        sha = find_commit(repo, local_repo, version, branch='master')
    except:
        return
    
    # Archive xcms version
    tar_repo(local_repo)
    

if __name__ == '__main__':
    version = '2.99.6'
    path = '~/skoltech/aspire/server/different_xcms'
    
    get_xcms_version(path=path,
                     version=version)

