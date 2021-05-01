# Menu Driven EC2 script
import boto3
import sys
from colored import fg

aws_mgmt_console = boto3.session.Session(profile_name="boto_profile")
ec2_console = aws_mgmt_console.client("ec2")

while True:
    print(" ************Welcome to EC2 Menu Driven Scrip************ ")

    print(
        """
         1. Start
         2. Stop
         3. Reboot
         4. Terminate
         5. Exit"""
    )
    opt = int(input("Enter option: "))
    if opt == 1:
        instance_id = input("Enter your EC2 Instance Id: ")
        print("Starting the Instance...")
        ec2_console.start_instances(InstanceIds=[instance_id])
        waiter = ec2_console.get_waiter("instance_running")
        waiter.wait(InstanceIds=[instance_id])
        print("The instance is now up and running!! Now performing the health check!!")

    elif opt == 2:
        instance_id = input("Enter your EC2 Instance Id: ")
        print("Stopping the instance")
        ec2_console.stop_instances(InstanceIds=[instance_id])
        waiter = ec2_console.get_waiter("instance_stopped")
        waiter.wait(InstanceIds=[instance_id])
        print("The instance is now stopped!!")

    elif opt == 3:
        instance_id = input("Enter your EC2 Instance Id: ")
        print("Rebooting the instance")
        ec2_console.reboot_instances(InstanceIds=[instance_id])
    elif opt == 4:
        instance_id = input("Enter your EC2 Instance Id: ")
        print("Terminating the instance")
        ec2_console.terminate_instances(InstanceIds=[instance_id])
        waiter = ec2_console.get_waiter("instance_terminated")
        waiter.wait(InstanceIds=[instance_id])
        print("The instance is now Terminated!!!!")

    elif opt == 5:
        print(fg("yellow") + "Thanks for using the script")
        sys.exit()
    else:
        print("sorry, invalid options. enter a correct option!!")
