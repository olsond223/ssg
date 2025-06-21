import os

from extract_title import extract_title
from blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as from_file:
        from_contents = from_file.read()

    with open(template_path, "r") as template_file:
        template_contents = template_file.read()

    node = markdown_to_html_node(from_contents)
    content = node.to_html()
    title = extract_title(from_contents)
    
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    dest_contents = template_contents.replace("{{ Title }}", title).replace("{{ Content }}", content)
    with open(dest_path, "w") as dest_file:
        dest_file.write(dest_contents)
    dest_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        filepath = os.path.join(dir_path_content, entry)
        if os.path.isdir(filepath):
            generate_pages_recursive(filepath, template_path, dest_dir_path)
        elif os.path.isfile(filepath) and entry.endswith(".md"):
            rel_path = os.path.relpath(filepath, start="content")
            dest_path = os.path.join(dest_dir_path, rel_path).replace(".md", ".html")
            os.makedirs(os.path.dirname(dest_path), exist_ok = True)
            generate_page(filepath, template_path, dest_path)
        
