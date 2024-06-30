from key_pair import KeyPair
from network import Network
from security_group import SecurityGroup
from instances import Instances

key_pair = KeyPair("my-vpc", "10.0.0.0/16")
network = Network()
security_group = SecurityGroup(network.get_vpc_id())
instances = Instances(network.get_subnet_id(), security_group.get_security_group_id(), key_pair.get_key_name())
