#!/opt/local/bin/python

import sys
import os
import markdown2
import shutil

def main():
    if len(sys.argv) < 2:
        print "input the name of the file!"
        sys.exit()

    html_file = open(sys.argv[1] + ".html", "w+")
    template = open("template.html", "r")

    md_file_name = sys.argv[1] + ".md" 
    if os.path.isfile(md_file_name) == False:
        print md_file_name + "doesn't found!"
        sys.exit()

    md_file = open(md_file_name, "r")
    md_html_string = markdown2.markdown(md_file.read())
    md_file.close()

    for template_string in template:
        if template_string.startswith("<body>"):
            html_file.write(template_string)
            html_file.write(md_html_string.encode('utf-8'))
        elif template_string.endswith("</title>\n"):
            title_name = sys.argv[1].encode('utf-8')
            title_string = "<title>" + title_name + "</title>\n"
            html_file.write(title_string)     
        else:
            html_file.write(template_string)

    template.close()
    html_file.close()

    if sys.argv[1] != "index":
        insert_link_in_index(sys.argv[1])

def insert_link_in_index(link_name):
    index_file_src = open("index.html","r")
    index_file_des = open("index_new.html", "w+")
    for line in index_file_src:
        index_file_des.write(line)
        if line.startswith("<body>"):
            link_url = '<h1><a href="' + link_name + '.html">' +\
                       link_name + '</a></h1>\n' 
            index_file_des.write(link_url)

    index_file_des.close()
    index_file_src.close()

    os.remove("index.html")
    os.rename("index_new.html", "index.html")

if (__name__ == "__main__"):
    main()
