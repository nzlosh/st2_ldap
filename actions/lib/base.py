#encoding=utf-8
#  from st2actions.runners.pythonrunner import Action
__all__ = [
    'BaseLDAPAction'
]


class Action(object):
    def __init__(self, config):
        self.config = config


class BaseLDAPAction(Action):
    def __init__(self, config):
        super(BaseLDAPAction, self).__init__(config=config)
        self._client = self._get_client()

    def _get_client(self):
        config = self.config

        options = {'server': config['url']}

        rsa_cert_file = config['rsa_cert_file']
        rsa_key_content = self._get_file_content(file_path=rsa_cert_file)

        oauth_creds = {
            'access_token': config['oauth_token'],
            'access_token_secret': config['oauth_secret'],
            'consumer_key': config['consumer_key'],
            'key_cert': rsa_key_content
        }

        client = JIRA(options=options, oauth=oauth_creds)
        return client

