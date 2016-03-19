import yaml
import getpass

# Load the configuration file
cfg = yaml.load(open("config.yml", 'r'))

# Making sure "username" and "password" exist
cfg["username"] = cfg["username"] if("username" in cfg) else input("Username: ")
cfg["password"] = cfg["password"] if("password" in cfg) else getpass.getpass("Password: ")

# Making sure "projects" exists
if "projects" in cfg:
	if not len(cfg["projects"]) == 2: # Only 2 projects. Else asks for projects again
		cfg["projects"][0] = input("First project: ")
		cfg["projects"][1] = input("Second project: ")
else:
	cfg["projects"][0] = input("First project: ")
	cfg["projects"][1] = input("Second project: ")

# Making sure the variable name has been specified
cfg["variable-name"] = cfg["variable-name"] if("variable-name" in cfg) else input("Variable: ")

# "update-interval" can't be less than 0.1 and it has to be a valid number!
if "update-interval" in cfg:
	try:
		cfg["update-interval"] = int(cfg["update-interval"])
		cfg["update-interval"] = cfg["update-interval"] if(cfg["update-interval"] > 0.1) else 0.1
	except ValueError:
		cfg["update-interval"] = int(input("Update interval: "))
		cfg["update-interval"] = cfg["update-interval"] if(cfg["update-interval"] > 0.1) else 0.1
else:
	cfg["update-interval"] = input("Update interval: ")

print(cfg) # Printing is temporary