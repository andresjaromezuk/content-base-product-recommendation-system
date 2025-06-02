# %%
from opensearchpy import OpenSearch

class VectorDbService:

  def __init__(self):
    host = 'localhost'
    port = 9200
    auth = ('admin', 'J@r#o19b3')
    self.client = OpenSearch(
      hosts = [{'host': host, 'port': port}],
      http_auth = auth,
      use_ssl = True,
      verify_certs = False,
      ssl_show_warn=False
    )

