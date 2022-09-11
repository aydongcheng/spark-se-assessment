import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgres://qhlayvrmlbvoyi:fcf0b1968c6bea21655e54aac3a73937efa3ea5fa12f6b6add99d8a8b63e730a@ec2-44-194-4-127.compute-1.amazonaws.com:5432/'
database_name = 'dcqkrf59eg3p7d'


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'diagnostic_secret')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'diagnostic_secret'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///diagnostic'
