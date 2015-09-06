#!/bin/bash

source /usr/local/bin/virtualenvwrapper.sh
workon gala2015

python build_index.py > /tmp/update_gala.log 2>&1 ||
  (cat /tmp/update_gala.log  && exit 1)

if git commit index.html -m "autoupdate" > /dev/null; then
  git push origin gh-pages
fi

