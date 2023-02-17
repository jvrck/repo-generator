import random
import os
from shutil import which
from faker import Faker

faker = Faker()

def create_repo(output_dir):
    repo_name = '-'.join(faker.words(3))
    generate_repository(repo_name, output_dir)

# generate a repo
def generate_repository(repo_name, output_dir):
    number_of_branches = random.randint(5,15)

    os.chdir(output_dir)
    os.mkdir(repo_name)

    repo_dir = get_repo_dir(output_dir, repo_name)

    os.chdir(repo_dir)
    os.system('git init')
    generate_readme(repo_name, repo_dir)
    os.system("git add .")
    os.system("git commit -m \'Added readme\'")

    # generate on master branch
    generate_branch_files(repo_dir, 'master')

    number_of_branches = random.randint(5,15)

    for i in range(1, number_of_branches):
        branch_name = faker.words(1)[0]
        generate_branch_files(repo_dir, branch_name)        

# generate files on a branch
def generate_branch_files(repo_dir, branch):
    os.chdir(repo_dir)
    os.system("git checkout -b {0}".format(branch))

    number_of_files = random.randint(5,15)

    for i in range(1, number_of_files):
        fake_word = faker.words(1)[0]
        file_name = "{0}.txt".format(fake_word)
        f = open(file_name, "w")
        f.write(faker.paragraph(nb_sentences=5))
        f.close()
        os.system("git add .")
        os.system("git commit -m \'Added {0}.txt\'".format(fake_word))
    
    os.system("git checkout master")

# generate a readme file
def generate_readme(repo_name, repo_dir):
    os.chdir(repo_dir)
    f = open("README.md", "w")
    f.write("# {0}\n".format(repo_name))
    f.write("Generated with [`repo-generator`](https://github.com/jvrck/repo-generator) \n")
    f.close()

# get the directory of the repo
# corrects the path if a slash does not exist    
def get_repo_dir(output_dir, repo_name):
    if not output_dir.endswith('/'):
        return "{0}/{1}".format(output_dir, repo_name)

    return "{0}{1}".format(output_dir, repo_name)

# Check git is installed
def check_git():
    return(which('git'))
