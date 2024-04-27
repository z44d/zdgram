from setuptools import setup, find_packages
import re


with open("README.md", encoding="utf-8") as f:
    long_description = "\n" + f.read()

with open("zdgram/__init__.py", encoding="utf-8") as f:
    VERSION = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

DESCRIPTION = 'Python module based on https://core.telegram.org/bots/api'

# Setting up
setup(
    name="zdgram",
    version=VERSION,
    author="ZAID",
    author_email="y8838@hotmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(exclude=["examples"]),
    install_requires=['asyncio', 'aiohttp'],
    keywords=['bots', 'bot-api', 'telegram'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires="~=3.8",
)