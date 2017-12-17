# set twitter keys & tokens
twitter_config = {
    "consumer_key": "abc",
    "consumer_secret": "xyz123",
    "access_token": "token-123",
    "access_token_secret": "tokensecret789"
}

es_mappings = {
    "tweet_index": {
        "mappings": {
            "tweet": {
                "properties": {
                    "timestamp_ms": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "hashtags": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "created_at": {
                      "type": "date",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "date"
                        }
                      }
                    },
                    "screen_name": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "user_name": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "location": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "source_device": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "country": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "country_code": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "tweet_text": {
                      "type": "string",
                      "fields": {
                        "raw": {
                          "index": "not_analyzed",
                          "type": "string"
                        }
                      }
                    },
                    "lang": {
                  "type": "string",
                  "fields": {
                    "raw": {
                      "index": "not_analyzed",
                      "type": "string"
                    }
                  }
                }
                }
            }
        }
    }
#PUT http://localhost:9200/tweets_index/_mapping/tweet/
}