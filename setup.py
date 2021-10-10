import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discordtownlistpy",
    version="0.0.3",
    author="Infinity#2837",
    author_email="bobcustomerservice@talktalk.net",
    description="An unofficial API wrapper for interfacing with discord town list API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TrainsRAwesome/discordtownlistpy",
    project_urls={
        "Bug Tracker": "https://github.com/TrainsRAwesome/discordtownlistpy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=["requests","asyncio"],
    python_requires=">=3.6",
)