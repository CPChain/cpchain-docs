import os

# Remove all RST files in all directory
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".rst"):
            os.remove(os.path.join(root, file))
