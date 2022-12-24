import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="intramove",
    version="0.0.1",
    author="Abdellatif Dalab",
    author_email="abdulatifsal@gmail.com",
    description="A client for interacting with Intramove.ai API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abdelatifsd/intramove",
    packages=setuptools.find_packages(),
    install_requires = ["ratelimiter","bson","requests","webbrowser"],
    keywords = ["python", "deep learning", "finance", "text classification", "text analysis", "sentiment"],
    classifiers=[
        "Development Status :: 1 - Developing"
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)