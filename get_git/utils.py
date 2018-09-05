import requests


def make_request(url, method='get', token=None, data=None):
    if method.lower() == 'get':
        response = requests.get(url)
    elif method.lower() == 'post':
        response = requests.post(
            url,
            json={'query': data},
            headers={'Authorization': f'token {token}'}
        )
    else:
        return {'error': f'method {method} not allowed.'}

    if response.status_code == 200:
        return response.json()
    else:
        raise RequestException(f'Request to {url} failed with status code {response.status_code}.')


class RequestException(Exception):
    pass
