from tfstate.base import Tfstate, Module, ResourceMap
tf_file = open('terraform.tfstate.backup')
tfstate_data = Tfstate(tf_file)


