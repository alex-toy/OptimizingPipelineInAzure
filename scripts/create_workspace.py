from azureml.core import Workspace

ws = Workspace.create(
    name='alexei-ws',
    subscription_id='',
    resource_group='myresourcegroup',
    create_resource_group=True,
    location='francecentral'
)