import yaml
import getpass


class Config:
    #This class manages the config.yml.

    cfg = yaml.load(open("config.yml", 'r'))

    def __init__(self):
        cfg = self.cfg

        cfg["username"] = cfg["username"] if("username" in cfg) else input("Username: ")
        cfg["password"] = cfg["password"] if("password" in cfg) else getpass.getpass("Password: ")
        cfg["update-interval"] = cfg["update-interval"] if ("update-interval" in cfg) else input("update-interval: ")
        cfg["cloud-variable"] = cfg["cloud-variable"] if("cloud-variable" in cfg) else input("cloud-variable: ")

        if "projects" in cfg:
            if not len(cfg["projects"]) == 2:
                cfg["projects"][0] = input("First project: ")
                cfg["projects"][1] = input("Second project: ")
        else:
            cfg["projects"][0] = input("First project: ")
            cfg["projects"][1] = input("Second project: ")

        self.cfg = cfg

    def get_yml(self):
        return self.cfg
