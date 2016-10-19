# django-managedbeat

This package provides a managed, more reliable approach for running celerybeat in multiple instance system, such as
Amazon Elastic Beanstalk.

The main functionality is to keep one and only one instance of celerybeat running in such cluster at all times.

## Installation

Add managedbeat to INSTALLED_APPS

## Configuration

Managedbeat reads configuration from Django settings variable MANAGEDBEAT. It expects a dictionary and following
keys are used right now:

- cache_key: Cache key to use for storing celerybeat status
- leader_expire: Expiration time (in seconds) for leader information (will start a new leader if current one has not
reported since leader_expire seconds)
- status_poll_interval: Interval to set and poll current leader status (in seconds). This should be lower than
leader_expire

Default settings are as follows:

MANAGEDBEAT = {
  "cache_key": "managedbeat_status",
  "leader_expire": 60,
  "status_poll_interval": 15
}