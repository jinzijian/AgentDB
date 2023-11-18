import pinecone
import configparser

# 创建配置解析器
config = configparser.ConfigParser()

# 读取配置文件
config.read('./config/config.ini')
api_key = config['pinecone']['api_key']
environment = config['pinecone']['environment']

def init_vecDB(api_key, environment):
    pinecone.init(api_key, environment)

if __name__ == "__main__":
    pinecone.init(api_key, environment="asia-southeast1-gcp")
    pinecone.delete_index("quickstart")
    pinecone.create_index("quickstart", dimension=8, metric="euclidean")
    pinecone.describe_index("quickstart")
    index = pinecone.Index("quickstart")

    index.upsert(
    vectors=[
        {"id": "A", "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},
        {"id": "B", "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]},
        {"id": "C", "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]},
        {"id": "D", "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]},
        {"id": "E", "values": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]}
    ]
    )
    print(index.query(
    vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    top_k=3,
    include_values=True
    ))
    pinecone.delete_index("quickstart")
