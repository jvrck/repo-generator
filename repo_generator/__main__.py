from repo_utils import *
import argparse
import os

argp = argparse.ArgumentParser()
argp.add_argument('-o', '--output', help='Output directory', default="~/.repo-generator")
args = argp.parse_args()

output_dir = None

if args.output[0] == '~':
    output_dir = os.path.expanduser(args.output)
else: 
    output_dir = args.output

if check_git():
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    create_repo(output_dir)
else:
    print('git is not installed...Exiting')
