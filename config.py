import os

class Config:

    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_ARTICLE = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY = 'e090655fdf3c4a649f08c2eca7a1f2cc'
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

configOptions = {
    'development':DevConfig,
    'production':ProdConfig
}   

