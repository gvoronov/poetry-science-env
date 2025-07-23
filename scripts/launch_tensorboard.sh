project=$1
port=$2

(cd ~/poetry-science-env/scripts; poetry run tensorboard --load_fast=false --logdir /code/users/gennadyvoronov/tensorboard-logs/$project --port $port)