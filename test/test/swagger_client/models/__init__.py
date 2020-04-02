# coding: utf-8

"""
    Most Popular

    Provides services for getting the most popular articles on NYTimes.com based on emails, shares, or views.  Get most emailed articles for the last day: ``` /emailed/1.json ```  Get most shared articles on Facebook for the last day: ``` /shared/1/facebook.json ```  Get most viewed articles for the last seven days: ``` /viewed/7.json ```  ## Example Calls ``` https://api.nytimes.com/svc/mostpopular/v2/emailed/7.json?api-key=yourkey ```  ``` https://api.nytimes.com/svc/mostpopular/v2/shared/1/facebook.json?api-key=yourkey ```  ``` https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key=yourkey ``` 

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

# import models into model package
from .emailed_article import EmailedArticle
from .inline_response_200 import InlineResponse200
from .inline_response_200_1 import InlineResponse2001
from .inline_response_200_2 import InlineResponse2002
from .media import Media
from .media_metadata import MediaMetadata
from .shared_article import SharedArticle
from .viewed_article import ViewedArticle