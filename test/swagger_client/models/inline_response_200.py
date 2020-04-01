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

from pprint import pformat
from six import iteritems
import re


class InlineResponse200(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, status=None, copyright=None, num_results=None, results=None):
        """
        InlineResponse200 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'str',
            'copyright': 'str',
            'num_results': 'int',
            'results': 'list[EmailedArticle]'
        }

        self.attribute_map = {
            'status': 'status',
            'copyright': 'copyright',
            'num_results': 'num_results',
            'results': 'results'
        }

        self._status = status
        self._copyright = copyright
        self._num_results = num_results
        self._results = results

    @property
    def status(self):
        """
        Gets the status of this InlineResponse200.


        :return: The status of this InlineResponse200.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InlineResponse200.


        :param status: The status of this InlineResponse200.
        :type: str
        """

        self._status = status

    @property
    def copyright(self):
        """
        Gets the copyright of this InlineResponse200.


        :return: The copyright of this InlineResponse200.
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """
        Sets the copyright of this InlineResponse200.


        :param copyright: The copyright of this InlineResponse200.
        :type: str
        """

        self._copyright = copyright

    @property
    def num_results(self):
        """
        Gets the num_results of this InlineResponse200.


        :return: The num_results of this InlineResponse200.
        :rtype: int
        """
        return self._num_results

    @num_results.setter
    def num_results(self, num_results):
        """
        Sets the num_results of this InlineResponse200.


        :param num_results: The num_results of this InlineResponse200.
        :type: int
        """

        self._num_results = num_results

    @property
    def results(self):
        """
        Gets the results of this InlineResponse200.


        :return: The results of this InlineResponse200.
        :rtype: list[EmailedArticle]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this InlineResponse200.


        :param results: The results of this InlineResponse200.
        :type: list[EmailedArticle]
        """

        self._results = results

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
