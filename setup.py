from setuptools import setup

setup(
    name='snapshotanalyzer-3000',
    version='0,1',
    author="Sashadev",
    author_email="...",
    description="SnapshotAnalyzer 3000 to manage AWS snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/sashadeve/snapshot-analyzer",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_point='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
