from setuptools import setup, find_packages

setup(
    name="lyra",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Dependencias de tiempo de ejecución
        "PySide6",
        "google-api-python-client",
        "tinydb",
        "APScheduler",
        "openai",
        "langchain",
        "whisper",
        "pyttsx3",
        "cryptography",
    ],
    entry_points={
        "console_scripts": [
            "lyra=main:main",
        ]
    },
)