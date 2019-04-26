import boto3
import sys

try:
    client = boto3.client ('ecs')

except Exception as e:
    print ("ERROR: failed to connect to ECS")
    sys.exit(1)

#input variables
task = input("What is the name of your Task: ")
clustername = input("What is the name of your Cluster: ")

taskresponse = client.describe_tasks(
    cluster=clustername,
    tasks=[
        task,
    ]
)

containerinstancearn = taskresponse ['tasks'][0]['containerInstanceArn']

container_response = client.describe_container_instances(
    cluster=clustername,
    containerInstances=[
        containerinstancearn,
    ]
)

print ( "Task {} is currently running on EC2 Instance {} ".format (task, ((container_response) ['containerInstances'] [0] ['ec2InstanceId'])))

