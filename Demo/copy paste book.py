import pathlib

download.save_as("output.txt")

with open("output.txt", "r") as f:
    content = f.read()

assert "Expected Text" in content
