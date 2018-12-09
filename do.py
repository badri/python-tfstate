from tfstate.base import Tfstate, Module, ResourceMap
tf_file = open('terraform.tfstate')
tfstate_data = Tfstate(tf_file)
for module in tfstate_data.modules:
    if len(module.path) == 2 and module.path[1] == 'openshift_digitalocean':
        print(module.outputs)


