# setuptools ko import karna, jo package banane mein madad karta hai
import setuptools

# README.md file ko padhna aur uska content long_description mein store karna
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Version number set karna
__version__ = "0.1.0"

# Repository ka naam set karna
REPO_NAME = 'LinkLNS'

# Source repository ka naam set karna
SRC_REPO = 'LinkLNS'

# Author ka username set karna
AUTHOR_USER_NAME = "DashingData"

# Author ka email set karna
AUTHOR_EMAIL = "abhishekac407@gmail.com"

# setuptools.setup function ko call karna package ke details ke saath
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python tool to link media into NoteBook",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"": "src"},  # Yahan par 'packages_dir' ki jagah 'package_dir' hona chahiye
    packages=setuptools.find_packages(where="src")  # 'where' parameter add kiya gaya hai
)
