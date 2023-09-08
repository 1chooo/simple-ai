#!/bin/zsh
#   Version v0.1.2
#   Author: Hugo ChunHo Lin
#   GitHub: github.com/1chooo
#   Copyright (C) 2023 Hugo ChunHo Lin All rights reserved.

if [[ "$VIRTUAL_ENV" != "" ]]; then
  echo "venv has been activated"
else
  source venv/bin/activate
  echo "venv is activated"
fi

python main.py
