import pulumi_aws as aws

class Network:
    def __init__(self, vpc_name: str, vpc_cidr_block: str):
        self.vpc = aws.ec2.Vpc(vpc_name,
            cidr_block=vpc_cidr_block,
            enable_dns_hostnames=True,
            enable_dns_support=True)

        self.public_subnet = aws.ec2.Subnet("public-subnet",
            vpc_id=self.vpc.id,
            cidr_block="10.0.1.0/24",
            map_public_ip_on_launch=True,
            availability_zone="ap-southeast-1a")

        self.igw = aws.ec2.InternetGateway("igw",
            vpc_id=self.vpc.id)

        self.route_table = aws.ec2.RouteTable("route-table",
            vpc_id=self.vpc.id,
            routes=[{
                "cidr_block": "0.0.0.0/0",
                "gateway_id": self.igw.id,
            }])

        self.rt_assoc_public = aws.ec2.RouteTableAssociation("rt-assoc-public",
            subnet_id=self.public_subnet.id,
            route_table_id=self.route_table.id)

    def get_vpc_id(self):
        return self.vpc.id

    def get_subnet_id(self):
        return self.public_subnet.id
