from setuptools import find_packages,setup

setup(
    name='chat_with_video',
    version='0.0.1',
    author='aniket sarap',
    author_email='aniketsarap27@gmail.com',
    install_requires=["langchain","streamlit","python-dotenv","PyPDF2","google-generativeai"],
    packages=find_packages()
)
