from embeddify.lib import get_data, post_data


def generate_embeddings(index_name, data):
    endpoint = f'pipelines/{index_name}/data'
    return post_data(endpoint, data)


def search(index_name, params):
    endpoint = f'search/{index_name}'
    return post_data(endpoint, params)


def ask(agent_name, query):
    raise Exception(f"Method not implemented")
