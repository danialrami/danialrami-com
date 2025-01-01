# adapted from networkchuck! https://blog.networkchuck.com/posts/my-insane-blog-pipeline/

import os
import re
import shutil

# Paths remain the same
posts_dir = "/Users/danielramirez/danialrami/content"
attachments_dir = "/Users/danielramirez/Obsidian/ore/attachments"
static_images_dir = "/Users/danielramirez/danialrami/static/images"

# Verify and create directories if needed
if not os.path.exists(static_images_dir):
    os.makedirs(static_images_dir)

# Verify required directories exist
if not os.path.exists(posts_dir):
    raise FileNotFoundError(f"Posts directory not found: {posts_dir}")
if not os.path.exists(attachments_dir):
    raise FileNotFoundError(f"Attachments directory not found: {attachments_dir}")

# Modified to use os.walk() with error handling
for root, dirs, files in os.walk(posts_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            
            try:
                with open(filepath, "r") as file:
                    content = file.read()
            except UnicodeDecodeError:
                with open(filepath, "r", encoding="utf-8") as file:
                    content = file.read()
            
            # Add support for more image formats
            images = re.findall(r'\[\[([^]]*\.(png|jpg|jpeg|gif|webp))\]\]', content)

            
            for image in images:
                markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
                content = content.replace(f"[[{image}]]", markdown_image)
                
                image_source = os.path.join(attachments_dir, image)
                if os.path.exists(image_source):
                    try:
                        shutil.copy(image_source, static_images_dir)
                    except shutil.Error as e:
                        print(f"Error copying {image}: {e}")
                else:
                    print(f"Warning: Image not found: {image}")

            try:
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(content)
            except Exception as e:
                print(f"Error writing to {filepath}: {e}")

print("Markdown files processed and images copied successfully.")