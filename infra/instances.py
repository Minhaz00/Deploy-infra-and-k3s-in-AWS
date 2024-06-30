import pulumi_aws as aws
import pulumi

class Instances:
    def __init__(self, subnet_id, security_group_id, key_name):
        self.ami_id = "ami-003c463c8207b4dfa"  
        self.instance_type = "t3.small"
        self.create_instances(subnet_id, security_group_id, key_name)

    def create_instances(self, subnet_id, security_group_id, key_name):
        self.master_node = aws.ec2.Instance("master-node",
            instance_type=self.instance_type,
            ami=self.ami_id,
            subnet_id=subnet_id,
            key_name=key_name,
            vpc_security_group_ids=[security_group_id],
            tags={"Name": "master-node"})

        self.worker_node_1 = aws.ec2.Instance("worker-node-1",
            instance_type=self.instance_type,
            ami=self.ami_id,
            subnet_id=subnet_id,
            key_name=key_name,
            vpc_security_group_ids=[security_group_id],
            tags={"Name": "worker-node-1"})

        self.worker_node_2 = aws.ec2.Instance("worker-node-2",
            instance_type=self.instance_type,
            ami=self.ami_id,
            subnet_id=subnet_id,
            key_name=key_name,
            vpc_security_group_ids=[security_group_id],
            tags={"Name": "worker-node-2"})

        pulumi.export("master_public_ip", self.master_node.public_ip)
        pulumi.export("worker1_public_ip", self.worker_node_1.public_ip)
        pulumi.export("worker2_public_ip", self.worker_node_2.public_ip)
