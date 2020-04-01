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


class Media(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, subtype=None, caption=None, copyright=None, approved_for_syndication=None, media_metadata=None):
        """
        Media - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'subtype': 'str',
            'caption': 'str',
            'copyright': 'str',
            'approved_for_syndication': 'bool',
            'media_metadata': 'list[MediaMetadata]'
        }

        self.attribute_map = {
            'type': 'type',
            'subtype': 'subtype',
            'caption': 'caption',
            'copyright': 'copyright',
            'approved_for_syndication': 'approved_for_syndication',
            'media_metadata': 'media-metadata'
        }

        self._type = type
        self._subtype = subtype
        self._caption = caption
        self._copyright = copyright
        self._approved_for_syndication = approved_for_syndication
        self._media_metadata = media_metadata

    @property
    def type(self):
        """
        Gets the type of this Media.


        :return: The type of this Media.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Media.


        :param type: The type of this Media.
        :type: str
        """

        self._type = type

    @property
    def subtype(self):
        """
        Gets the subtype of this Media.


        :return: The subtype of this Media.
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """
        Sets the subtype of this Media.


        :param subtype: The subtype of this Media.
        :type: str
        """

        self._subtype = subtype

    @property
    def caption(self):
        """
        Gets the caption of this Media.


        :return: The caption of this Media.
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """
        Sets the caption of this Media.


        :param caption: The caption of this Media.
        :type: str
        """

        self._caption = caption

    @property
    def copyright(self):
        """
        Gets the copyright of this Media.


        :return: The copyright of this Media.
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """
        Sets the copyright of this Media.


        :param copyright: The copyright of this Media.
        :type: str
        """

        self._copyright = copyright

    @property
    def approved_for_syndication(self):
        """
        Gets the approved_for_syndication of this Media.


        :return: The approved_for_syndication of this Media.
        :rtype: bool
        """
        return self._approved_for_syndication

    @approved_for_syndication.setter
    def approved_for_syndication(self, approved_for_syndication):
        """
        Sets the approved_for_syndication of this Media.


        :param approved_for_syndication: The approved_for_syndication of this Media.
        :type: bool
        """

        self._approved_for_syndication = approved_for_syndication

    @property
    def media_metadata(self):
        """
        Gets the media_metadata of this Media.


        :return: The media_metadata of this Media.
        :rtype: list[MediaMetadata]
        """
        return self._media_metadata

    @media_metadata.setter
    def media_metadata(self, media_metadata):
        """
        Sets the media_metadata of this Media.


        :param media_metadata: The media_metadata of this Media.
        :type: list[MediaMetadata]
        """

        self._media_metadata = media_metadata

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
