# ignore_files.py

import os
import shutil


def ignore_files(files):
  """Returns a list of files that should be ignored when checking code into GitHub."""

  ignore_list = [
      ".vscode",
      "__psycache__",
      ".venv",
  ]

  def is_ignored(file):
    for p in ignore_list:
      if file.endswith(p):
        return True
    return False

  return [f for f in files if not is_ignored(f)]


def main():
  """Prints a list of files that should be ignored when checking code into GitHub."""

  files = os.listdir(".")
  ignored_files = ignore_files(files)

  for file in ignored_files:
    if file in os.listdir(".git"):
      shutil.rmtree(file)


if __name__ == "__main__":
  main()