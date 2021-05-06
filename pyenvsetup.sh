sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl libncurses5-dev libncursesw5-dev xz-utils libffi-dev liblzma-dev git tk8.6-dev
curl https://pyenv.run | bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
exec "$SHELL"
pyenv install 3.7.0
pyenv global 3.7.0
python -m pip install wheel
python -m pip install chatterbot chatterbot_corpus tk
python -m spacy download en
curl https://raw.githubusercontent.com/ReCore-sys/chatbotsetup/main/chatbot.py -O
curl https://raw.githubusercontent.com/ReCore-sys/chatbotsetup/main/bot.png -O
curl https://raw.githubusercontent.com/ReCore-sys/chatbotsetup/main/db.sqlite3 -O
python chatbot.py

