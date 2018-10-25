"""
This module sets the configurations for the application
"""
import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False


class DevelopmentConfig(Config):
    """Development phase configurations"""
    DEBUG = True


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
