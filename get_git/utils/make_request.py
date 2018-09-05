import requests


class RequestException(Exception):
    pass

def make_request(url, method, token=None, data=None):
    headers = {}

    if method.lower() == 'get':
        response = requests.get(url)
    elif method.lower() == 'post':
        headers['Authorization'] = f'{token}'
        response = requests.post(
            url,
            json={'query': data},
            headers=headers
        )
    else:
        return {'error': f'method {method} not allowed.'}

    if response.status_code == 200:
        return response.json()
    else:
        raise RequestException(f'Request to {url} failed with status code {response.status_code}.')
