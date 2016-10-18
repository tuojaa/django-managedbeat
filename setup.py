from setuptools import setup

setup(name='django-managedbeat',
      version='0.0.1',
      description='Django admin command to run celerybeat more reliably on Amazon Elastic Beanstalk',
      author='Tuomas Jaanu',
      author_email='tuomas@jaa.nu',
      url='https://github.com/tuomasjaanu/django-managedbeat',
      packages=['managedbeat', ],
      install_requires=[
          "django-celery",
          "django",
      ],
     )