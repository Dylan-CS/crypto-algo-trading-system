import nacos

class NacosClient:
    def __init__(self, server_addresses, namespace, username, password):
        self.client = nacos.NacosClient(
            server_addresses,
            namespace=namespace,
            username=username,
            password=password
        )

    def register_service(self, service_name, ip, port):
        self.client.add_naming_instance(service_name, ip, port)

    def get_config(self, data_id, group):
        return self.client.get_config(data_id, group) 