import yaml # install pyyaml first with 'pip install pyyaml' command in terminal

with open('data.yml', 'r') as file:
    data = yaml.safe_load(file)

project = data.get('project')
name = project.get('name')
print(name)
work_packages = project.get('work_packages')
for work_package in work_packages:
    print(work_package)