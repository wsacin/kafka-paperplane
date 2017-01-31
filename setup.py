#!/usr/bin/env python

from distutils.core import setup

setup(name='kafka-paperplane',
      version='0.1',
      description='API for Apache Kafka as a notification system.',
      author='Walter Sobral',
      author_email='wsacin@gmail.com',
      packages=[
          'kafka_paperplane',
          'kafka_paperplane.persistence',
      ]
      )
