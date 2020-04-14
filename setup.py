import setuptools

setuptools.setup(
    name="pd-replicator",
    version="0.0.1",
    author="Sam Wilkinson",
    author_email="hello@samwilkinson.io",
    description="Copy a pandas DataFrame to the clipboard with one click",
    long_description="Copy a pandas DataFrame to the clipboard with one click",
    url="https://github.com/scwilkinson/pd-replicator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
          'pandas',
          'ipywidgets',
          'ipython',
    ]
)
