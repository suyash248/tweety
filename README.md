# Tweety 
**Uses twitter Streaming API to get the target tweets for a recent high traffic event(s), and persisting them to elasticsearch. Later, tweets can be filtered using REST API**

## Requirements
Python 2.7+, pip, Elastilcsearch, Twitter developer app

> Note: For creating `Twitter developer app', visit [Twitter Application Management](https://apps.twitter.com/) page

## How to run?
1. Move to ```<project-dir>```, create virual environment and then activate it as


```sh
$ cd <project-dir>
$ virtualenv .environment
$ source .environment/bin/activate
```

2. Copy ```settings_sample.py``` and create ```settings.py```. Edit configuration/settings related to ```Twitter developer app```.

```sh
$ cp settings_sample.py settings.py
```


3. Add project to ```PYTHONPATH``` as 

```sh 
$ export PYTHONPATH="$PYTHONPATH:." # . corresponds to current directory(project-dir)
```

> If you are using PyCharm then it can be done under `run configuration`.

4. Under ```<project-dir>``` install requirements/dependencies as 

```sh 
$ pip install -r requirements.txt
```

5. Then run ```app.py``` as  

```sh
$ python app.py
```

> Now you can access the application by visiting ```{protocol}://{host}:{port}```. For localhost it is ```http://localhost:5000```.

> Congratulations! Start ```[Streaming](https://github.com/suyash248/tweety#streaming)``` & later on data can be filtered by using ```Funneling``` API.



## API's/Endpoints

### Streaming

```sh
GET /stream?keywords=cricket,hockey,virat
```

It will start streaming real-time tweets containing ```kewords```. And tweets will get persisted in elasticsearch under
the index ```tweets_index``` and ```tweet``` document type.

*Response*

```javascript
{
  "status": "success",
  "message": "Started streaming tweets with keywords [u'cricket', u'hockey', u'virat']"
}
```

### Funneling/Searching

```sh
POST /funnel?from=0&size=20
```

**Operators**: "equals", "contains", "wildcard", "gte", "gt", "lte", "lt"

**Fields**: "screen_name", "user_name", "location", "source_device", "is_retweeted", "retweet_count", "country", "country_code", "reply_count", "favorite_count", "tweet_text", "created_at", "timestamp_ms", "lang", "hashtags"

> Note: ```from``` & ```size```  can be used for limit/pagination, but are optional, default ```size``` is 100.

*Request body*

```javascript
{
	"sort":["created_at"],          		// User '-' sign for 'desc' order.
	"criteria": {
		"AND": [{
			"fields": ["created_at"],	
			"operator": "gte",		// equals, contains, wildcard, gte, gt, lte, lt
			"query": "2017-12-17T14:18:13"
		    }, {
			"fields": ["location"],
			"operator": "wildcard",
			"query": "*ind*"
		    }, {
			"fields": ["hashtags"],		// 'hashtags' is an array field.
			"operator": "contains",
			"query": "Cricket"
		    }
		],
		"OR": [{
			"fields": ["hashtags"],
			"operator": "contains",
			"query": "cricket"
		    }, {
			"fields": ["hashtags"],
			"operator": "contains",
			"query": "hockey"
		    }
		],
		"NOT": [{
			"fields": ["source_device"],
			"operator": "equals",
			"query": "Twitter for Android"
		    }
		]
    	}
}
```

*Response*

```javascript
{
    "count": {
        "total": 21,
        "fetched": 10
    },
    "results": [
        {
            "sort": [
                1513520366000
            ],
            "_type": "tweet",
            "_source": {
                "lang": "in",
                "is_retweeted": false,
                "retweet_count": 0,
                "screen_name": "T10CricketLive",
                "country": "",
                "created_at": "2017-12-17T14:19:26",
                "hashtags": [
                    "IndvSL",
                    "Cricket"
                ],
                "tweet_text": "Ind 193/2 (30 ov), need 23. Karthik 15(24), Dhawan 87(79). Bowling figures of Akila Dananjaya so far: 7-0-48-1. #IndvSL #Cricket",
                "source_device": "IFTTT",
                "reply_count": 0,
                "location": "New Delhi, India",
                "country_code": "",
                "timestamp_ms": "1513520366428",
                "user_name": "cricGuru5167",
                "favorite_count": 0
            },
            "_score": null,
            "_index": "tweets_index",
            "_id": "AWBk2AUVU3yhj98vAeu_"
        },
        {......},
        {......},
        {......},
        {......},
    ]
}
```

