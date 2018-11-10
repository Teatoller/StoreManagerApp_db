"""
This module sets the configurations for the application
"""
import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    DATABASE_URL = os.getenv("DATABASE_URL")
  

class DevelopmentConfig(Config):
    """Development phase configurations"""
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_TEST_URL")
    PRESERVE_CONTEXT_ON_EXCEPTION = True


class TestingConfig(Config):
    """Testing Configurations."""
    TESTING = True
    DEBUG = True


class ReleaseConfig(Config):
    """Release Configurations."""
    DEBUG = False
    TESTING = False

#  config Dictionary in key value pairs
app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'release': ReleaseConfig,
}