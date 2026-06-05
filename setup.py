from setuptools import setup, find_packages

setup(
    name=\'commit-craft-ai\',
    version=\'0.1.0\',
    packages=find_packages(),
    py_modules=[\'commit_craft_ai\'],
    install_requires=[
        # No external dependencies for this mock version, but in a real project:
        # \'openai\',
        # \'GitPython\',
    ],
    entry_points={
        \'console_scripts\': [
            \'commit-craft-ai=commit_craft_ai:main\',
        ],
    },
    author=\'Manus AI\',
    author_email=\'support@manus.im\',
    description=\'AI-powered Git Commit Message Generator\',
    long_description=open(\'README.md\').read(),
    long_description_content_type=\'text/markdown\',
    url=\'https://github.com/your-username/Commit-Craft-AI\', # Replace with your GitHub repo URL
    classifiers=[
        \'Programming Language :: Python :: 3\',
        \'License :: OSI Approved :: MIT License\',
        \'Operating System :: OS Independent\',
        \'Development Status :: 3 - Alpha\',
        \'Intended Audience :: Developers\',
        \'Topic :: Software Development :: Version Control\',
        \'Topic :: Scientific/Engineering :: Artificial Intelligence\',
    ],
    python_requires=\'>=3.6\',
)
