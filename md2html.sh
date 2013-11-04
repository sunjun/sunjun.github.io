#!/bin/sh
if [ -f "${1}.md" ]; then 
	cat "${1}.md" | python -m markdown2 > "${1}.html"
else
	echo "${1}.md do not exist"
fi
