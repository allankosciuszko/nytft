# swagger_client.MostPopularApi

All URIs are relative to *https://api.nytimes.com/svc/mostpopular/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emailed_period_json_get**](MostPopularApi.md#emailed_period_json_get) | **GET** /emailed/{period}.json | Most emailed articles on NYTimes.com.
[**shared_period_json_get**](MostPopularApi.md#shared_period_json_get) | **GET** /shared/{period}.json | Most shared articles on NYTimes.com.
[**shared_period_share_type_json_get**](MostPopularApi.md#shared_period_share_type_json_get) | **GET** /shared/{period}/{share_type}.json | Most shared articles on NYTimes.com of specified share type.
[**viewed_period_json_get**](MostPopularApi.md#viewed_period_json_get) | **GET** /viewed/{period}.json | Most viewed articles on NYTimes.com.


# **emailed_period_json_get**
> InlineResponse200 emailed_period_json_get(period)

Most emailed articles on NYTimes.com.

Returns an array of the most emailed articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days). 

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
swagger_client.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MostPopularApi()
period = 56 # int | Time period: 1, 7, or 30 days.

try: 
    # Most emailed articles on NYTimes.com.
    api_response = api_instance.emailed_period_json_get(period)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MostPopularApi->emailed_period_json_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **int**| Time period: 1, 7, or 30 days. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shared_period_json_get**
> InlineResponse2001 shared_period_json_get(period)

Most shared articles on NYTimes.com.

Returns an array of the most shared articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days). 

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
swagger_client.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MostPopularApi()
period = 56 # int | Time period: 1, 7, or 30 days.

try: 
    # Most shared articles on NYTimes.com.
    api_response = api_instance.shared_period_json_get(period)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MostPopularApi->shared_period_json_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **int**| Time period: 1, 7, or 30 days. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shared_period_share_type_json_get**
> InlineResponse2001 shared_period_share_type_json_get(period, share_type)

Most shared articles on NYTimes.com of specified share type.

Returns an array of the most shared articles by share type on NYTimes.com for specified period of time (1 day, 7 days, or 30 days). 

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
swagger_client.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MostPopularApi()
period = 56 # int | Time period: 1, 7, or 30 days.
share_type = 'share_type_example' # str | Share type: facebook.

try: 
    # Most shared articles on NYTimes.com of specified share type.
    api_response = api_instance.shared_period_share_type_json_get(period, share_type)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MostPopularApi->shared_period_share_type_json_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **int**| Time period: 1, 7, or 30 days. | 
 **share_type** | **str**| Share type: facebook. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **viewed_period_json_get**
> InlineResponse2002 viewed_period_json_get(period)

Most viewed articles on NYTimes.com.

Returns an array of the most viewed articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days). 

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
swagger_client.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MostPopularApi()
period = 56 # int | Time period: 1, 7, or 30 days.

try: 
    # Most viewed articles on NYTimes.com.
    api_response = api_instance.viewed_period_json_get(period)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MostPopularApi->viewed_period_json_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **int**| Time period: 1, 7, or 30 days. | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

