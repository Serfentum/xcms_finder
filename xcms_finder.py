from cli import parsing
from get_xcms_version import get_xcms_version


# Parse args
args = parsing()

# Extract arguments
path = args.path
version = args.version
repo_clone_url = args.repo_clone_url

# Start working
get_xcms_version(path, version, repo_clone_url='https://github.com/sneumann/xcms.git')
