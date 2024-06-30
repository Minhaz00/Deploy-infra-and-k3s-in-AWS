from key_pair import KeyPair
from network import Network
from security_group import SecurityGroup
from instances import Instances

def main():
    key_pair = KeyPair()
    network = Network()
    security_group = SecurityGroup(network.get_vpc_id())
    instances = Instances(network.get_subnet_id(), security_group.get_security_group_id(), key_pair.get_key_name())

if __name__ == "__main__":
    main()
