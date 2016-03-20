import scratchapi

from src.mooshoe.Config import Config


class Main:
    #This class bridges two Scratch projects together.

    #grab config
    config = Config()
    yml = config.get_yml()

    #init vars
    username = yml["username"]
    password = yml["password"]
    cloudvar = yml["cloud-variable"]#name of cloud varible
    projectId = yml["projects"]

    update = yml["update-interval"]

    scratch = scratchapi.ScratchUserSession(username, password)
    scratch.tools.verify_session()
    cloud = [scratchapi.CloudSession(projectId[0], scratch), scratchapi.CloudSession(projectId[1], scratch)]

    #Begin server
    while True:
        p1 = cloud[0].get_updates(update)  #get updates
        p2 = cloud[1].get_updates(update)  #get more updates
        if len(p1) != 0:  #if the first project updated:
            cloud[0].set_var(cloudvar, cloud[0].get_var(cloudvar))
            cloud[1].set_var(cloudvar, cloud[0].get_var(cloudvar))
            print("Bridge modified. 1")
            pass
        elif len(p2) != 0:  #if the second project updated
            cloud[0].set_var(cloudvar, cloud[1].get_var(cloudvar))
            cloud[1].set_var(cloudvar, cloud[1].get_var(cloudvar))
            print("Bridge modified. 2")
            pass
        else:  #if there are no updates, pass.
            pass