import pulumi_aws as aws

class SecurityGroup:
    def __init__(self, vpc_id):
        self.security_group = aws.ec2.SecurityGroup("web-secgrp",
            description='Enable SSH and K3s access',
            vpc_id=vpc_id,
            ingress=[
                {
                    "protocol": "tcp",
                    "from_port": 22,
                    "to_port": 22,
                    "cidr_blocks": ["0.0.0.0/0"],
                },
                {
                    "protocol": "tcp",
                    "from_port": 6443,
                    "to_port": 6443,
                    "cidr_blocks": ["0.0.0.0/0"],
                },
            ],
            egress=[{
                "protocol": "-1",
                "from_port": 0,
                "to_port": 0,
                "cidr_blocks": ["0.0.0.0/0"],
            }])

    def get_security_group_id(self):
        return self.security_group.id
