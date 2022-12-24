import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="intramove",
    version="0.0.1",
    author="Abdellatif Dalab",
    author_email="abdulatifsal@gmail.com",
    description="A client for interacting with Intramove.ai API",
    long_description="A client for interacting with Intramove.ai API that allows you to purchase credits and query available services like news headline analysis.",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires = ["ratelimiter","bson","requests","webbrowser"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)