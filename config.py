import yaml
import getpass

cfg = yaml.load(open("config.yml", 'r'))

cfg["username"] = cfg["username"] if("username" in cfg) else input("Username: ")
cfg["password"] = cfg["password"] if("password" in cfg) else getpass.getpass("Password: ")

if "projects" in cfg:
	if not len(cfg["projects"]) == 2:
		cfg["projects"][0] = input("First project: ")
		cfg["projects"][1] = input("Second project: ")
else:
	cfg["projects"][0] = input("First project: ")
	cfg["projects"][1] = input("Second project: ")

print(cfg)