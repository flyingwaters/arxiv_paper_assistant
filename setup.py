from setuptools import setup, find_packages
 
setup(
    name='arxiv_search_assistant',
    version='0.1',
    description='An Python Package to help you search the arxiv api and use gpt-3.5-turbo to generate one Chinese sentence from the summary.',
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        # list of any packages that need to be installed along with your package
        feedparser,
        arxiv,
        tqdm,
        openai
    ],
    author="fenglongyu",
    Email="fly_fenglongyu@outlook.com"
    url="https://github.com/flyingwaters/paper_search_assistant.git"
)