import os
from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(name="pytux",
          version="0.1.0",
          # TODO: check required version
          python_requires=">=3.6",
          install_requires=["wheel"],
          packages=find_packages(include=["pytux", "pytux.*"]),
          package_dir={"pytux": "pytux"},
          entry_points={
              "console_scripts": [
                  "pytux = pytux.__main__:main"
              ]
          })
    try:
        home_path = os.path.join(os.path.expanduser("~"), ".pytux")
        os.makedirs(home_path, exist_ok=True)
    except Exception as err:
        print(err)
        exit(-1)
