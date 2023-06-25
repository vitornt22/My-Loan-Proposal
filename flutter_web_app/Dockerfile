# Define a imagem base
FROM nginx:alpine

# Remove o arquivo de configuração padrão do Nginx


# Copia os arquivos estáticos do Flutter Web para o diretório de publicação do Nginx
COPY . /usr/share/nginx/html

# Copia um novo arquivo de configuração para o Nginx
COPY nginx.conf /etc/nginx/conf.d

# Expõe a porta 80 para acessar o Nginx
EXPOSE 80

