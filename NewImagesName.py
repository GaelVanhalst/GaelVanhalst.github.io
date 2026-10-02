import os

# Set the path to your portfolio folder
project_folder = "."  # "." means current directory where script is run

old_text = "_img"
new_text = "Images"

# Step 1: Rename the folder if it exists
old_folder_path = os.path.join(project_folder, old_text)
new_folder_path = os.path.join(project_folder, new_text)

if os.path.exists(old_folder_path):
    os.rename(old_folder_path, new_folder_path)
    print(f"Renamed folder '{old_text}' to '{new_text}'")

# Step 2: Update references inside HTML, CSS, JS, and Markdown files
text_extensions = (".html", ".htm", ".css", ".js", ".md")

for root, _, files in os.walk(project_folder):
    for file in files:
        if file.endswith(text_extensions):
            file_path = os.path.join(root, file)

            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            if old_text in content:
                updated_content = content.replace(old_text, new_text)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)
                print(f"Updated references in: {file_path}")

print("Done! All occurrences replaced.")