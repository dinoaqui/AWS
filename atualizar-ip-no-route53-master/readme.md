#  Este Script originalmente desenvolvido por:
#  Wittemberg Mesquita - https://www.linkedin.com/in/wittemberg/
# Repositorio Original:
# https://gitlab.com/comunidade-cloud/aws/atualizar-ip-no-route53  
# Comunidade Cloud - AWS:
# https://gitlab.com/comunidade-cloud/aws

# ATUALIZAR IP EM UM REGISTRO A DO ROUTE 53 - Container Docker 

Este projeto tem o intuito de atualizar seu IPv4 Público em um registro A do Route 53, criando assim um serviço de DDNS que você poderá usar em seus clientes. Basta colocar na Cron para atualizar no tempo necessário.

## Modo de uso

  - Homologado em Linux Ubuntu;
  - Instale o Docker e o git;
  ```
  sudo apt update && sudo apt install git -y
  curl -fsSL https://get.docker.com/ | sh
  ```
  obs: Está instalação do Docker NÃO é para ser usada em produção. O modo correto de instlação está na pagina oficial https://docs.docker.com/engine/install/ubuntu/   

  - Configurar o usuario para ter acesso aos comandos do Docker, sem ser root

  ```
  sudo usermod -aG docker $USER
  ```
  obs: Após este passo, deve-se encerrar a sessão e acessar novamente para se concretizar.   



  - Clone o Repositório;
```
git clone https://gitlab.com/soaresnetoh/atualizar-ip-no-route53.git
cd atualizar-ip-no-route53
```  
  - Rode o Comando;
    - Para fazer o build da imagem
```
  docker build . -t route53_update
```
  - Rode o Comando;
    - Para alterar o registro no Route53 da AWS, deve-se rodar o container colocando algumas variaveis, como as credenciais AWS que tenham acesso ao Route53 e ao final do comando as informações de <DOMINIO> <SUBDOMINIO> <NOVO_IP>:  
  $ docker run -it --rm -e AWS_ACCESS_KEY_ID=AKYTGGTRG -e AWS_SECRET_ACCESS_KEY=4Hb3d333qhngr1TYw1C8jMqyDkUYhhj -v $PWD:/app/script route53_update exemplo.com.br app 200.200.175.175
  -> onde "exemplo.com.br" é o DOMINIO e "app" é o SUBDOMINIO  e "200.200.175.175" é o NOVO_IP. Caso queira que seja usado o ip real , use da seguinte forma:  
  $ docker run -it --rm -v $PWD:/app/script route53_update exemplo.com.br app meu_ip  
  ex: 
  
```
  docker run -it --rm -e AWS_ACCESS_KEY_ID=AKYTGGTRG -e AWS_SECRET_ACCESS_KEY=4Hb3d333qhngr1TYw1C8jMqyDkUYhhj -v $PWD:/app/script route53_update exemplo.com.br app 200.200.175.175
```
