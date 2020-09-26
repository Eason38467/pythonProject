
import yaml

with open('1-push-config.yaml') as file:
    content = yaml.load(file,Loader=yaml.FullLoader)

print(content)
print(content[0]["hosts"])