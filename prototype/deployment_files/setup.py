from setuptools import setup, find_packages

setup(
    name='ScientificDataAnalysisApp',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'tensorflow',
        'keras',
        'flask',
        'gunicorn',
        'cryptography',
        'bcrypt',
        'pyjwt',
        'nltk',
        'matplotlib',
        'seaborn',
        'music21',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'run_app = prototype.deployment_files.run:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A cutting-edge mobile application that leverages AI, data science, and machine learning to analyze complex scientific data sets.",
    keywords="AI, Data Science, Machine Learning, Mobile Application",
    url="http://github.com/yourusername/ScientificDataAnalysisApp"
)