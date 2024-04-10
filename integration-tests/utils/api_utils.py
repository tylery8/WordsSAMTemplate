import boto3


def get_base_url(api_name, region_name):
    api_gateway = boto3.client('apigateway', region_name=region_name)
    rest_apis = api_gateway.get_rest_apis()['items']
    rest_api_index = next((index for index, item in enumerate(rest_apis) if item['name'] == api_name), None)
    rest_api_id = rest_apis[rest_api_index]['id']
    stage_name = api_gateway.get_stages(restApiId=rest_api_id)['item'][0]['stageName']

    return f"https://{rest_api_id}.execute-api.{region_name}.amazonaws.com/{stage_name}"
