import datetime

# Get the current time formatted as YYYY-MM-DD HH:MM:SS
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Prepare the new content for README.md
new_content = f"Current time: {current_time}\n"

# Open README.md in write mode (this will overwrite the existing content)
with open("README.md", "w", encoding="utf-8") as readme_file:
    readme_file.write(new_content)

print("README.md updated successfully.")
