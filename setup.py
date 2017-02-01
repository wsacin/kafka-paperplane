#!/usr/bin/env python

from setuptools import setup

setup(name='kafka-paperplane',
      version='0.1',
      description='API for Apache Kafka as a notification system.',
      author='Walter Sobral',
      author_email='wsacin@gmail.com',
      license='apache-2.0',
      packages=[
          'kafka_paperplane',
          'kafka_paperplane.persistence',
      ],
      install_requires=[
          'yajl',
          'kafka-python',
          'pymongo',
          'redis',
      ]
      )
