import pulumi_aws as aws
import os

class KeyPair:
    def __init__(self):
        self.public_key = os.getenv("PUBLIC_KEY")
        self.key_pair = aws.ec2.KeyPair("my-key-pair",
            key_name="my-key-pair",
            public_key=self.public_key)

    def get_key_name(self):
        return self.key_pair.key_name
