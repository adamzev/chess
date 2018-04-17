import boto3
import json
client = boto3.client('lambda')

response = client.invoke(
    FunctionName='chess-move-dev-hello',
    InvocationType='RequestResponse', #|'RequestResponse'|'DryRun',
    LogType='None', #|'Tail',
    ClientContext='string',
    Payload=b'{"board":"testboard"}', #|file,
)
res_json = json.loads(response['Payload'].read().decode("utf-8"))
print(res_json)
