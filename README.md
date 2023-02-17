# repo-generator

Generate random git repositories using [Faker](https://faker.readthedocs.io/en/master/).


### How to use

This has been developed and tested on `Python 3.8.16` and MacOS

To install python dependencies:
```
pip install -r requirements.txt
```

Run the generator:
```
cd repo_generator
python3 .
```

This will generate a fake repository in the `~/.repo-generator` directory.

To generate a repository in a directory of your choice, execute the program with the `-o` argument:

```
python3 . -o /path/to/your/directory
```