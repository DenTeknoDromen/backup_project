from pyminio import Pyminio

client = Pyminio.from_credentials(endpoint="http://localhost:9001/",
                                access_key="minioadmin",
                                secret_key="minioadmin")

