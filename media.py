import os
import re
import shutil

# Paths for different media types
posts_dir = "/Users/danielramirez/danialrami/content"
attachments_dir = "/Users/danielramirez/Obsidian/ore/attachments"
static_images_dir = "/Users/danielramirez/danialrami/static/images"
static_videos_dir = "/Users/danielramirez/danialrami/static/videos"
static_audio_dir = "/Users/danielramirez/danialrami/static/audio"

# Media format patterns
IMAGE_FORMATS = r'\.(png|jpg|jpeg|gif|webp|svg)'
VIDEO_FORMATS = r'\.(mp4|webm|mov|avi)'
AUDIO_FORMATS = r'\.(mp3|wav|ogg|m4a)'

# Create all required directories
for directory in [static_images_dir, static_videos_dir, static_audio_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Verify required directories exist
if not os.path.exists(posts_dir):
    raise FileNotFoundError(f"Posts directory not found: {posts_dir}")
if not os.path.exists(attachments_dir):
    raise FileNotFoundError(f"Attachments directory not found: {attachments_dir}")

# Process markdown files
for root, dirs, files in os.walk(posts_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            
            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    content = file.read()
            except UnicodeDecodeError:
                print(f"Warning: Encoding issues with {filepath}")
                continue

            # Find all media references
            media_pattern = rf'!\[\[([^]]*({IMAGE_FORMATS}|{VIDEO_FORMATS}|{AUDIO_FORMATS}))\]\]'
            media_matches = re.findall(media_pattern, content, re.IGNORECASE)
            
            for media_match in media_matches:
                filename = media_match[0]  # Full filename
                extension = os.path.splitext(filename)[1].lower()
                
                # Determine media type and create appropriate markdown
                if re.match(IMAGE_FORMATS, extension, re.IGNORECASE):
                    markdown = f"![Image Description](/images/{filename.replace(' ', '%20')})"
                    target_dir = static_images_dir
                elif re.match(VIDEO_FORMATS, extension, re.IGNORECASE):
                    markdown = (f'<video controls controlsList="nodownload" oncontextmenu="return false;">'
                              f'<source src="/videos/{filename.replace(" ", "%20")}" type="video/{extension[1:]}"></video>')
                    target_dir = static_videos_dir
                elif re.match(AUDIO_FORMATS, extension, re.IGNORECASE):
                    markdown = (f'<audio controls controlsList="nodownload">'
                              f'<source src="/audio/{filename.replace(" ", "%20")}" type="audio/{extension[1:]}"></audio>')
                    target_dir = static_audio_dir
                
                # Replace the Obsidian link with markdown
                content = content.replace(f"![[{filename}]]", markdown)
                
                # Copy the media file
                media_source = os.path.join(attachments_dir, filename)
                if os.path.exists(media_source):
                    try:
                        shutil.copy(media_source, target_dir)
                    except shutil.Error as e:
                        print(f"Error copying {filename}: {e}")
                else:
                    print(f"Warning: Media file not found: {filename}")

            # Write updated content back to file
            try:
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(content)
            except Exception as e:
                print(f"Error writing to {filepath}: {e}")

print("Markdown files processed and media files copied successfully.")