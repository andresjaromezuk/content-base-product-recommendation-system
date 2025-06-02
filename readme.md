docker run -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" -e "OPENSEARCH_INITIAL_ADMIN_PASSWORD=J@r#o19b3" -d -v /Users/andresjaromezuk/Desktop/DEEPLEARNING/TPS/sistema-recomendacion/data/vector_db/db_data:/usr/share/opensearch/data opensearchproject/opensearch:latest


docker run -d \
  --name opensearch-dashboards \
  -p 5601:5601 \
  -e OPENSEARCH_HOSTS='["https://host.docker.internal:9200"]' \
  -e OPENSEARCH_USERNAME=admin \
  -e OPENSEARCH_PASSWORD='J@r#o19b3' \
  -e OPENSEARCH_SSL_VERIFICATIONMODE=none \
  opensearchproject/opensearch-dashboards:latest