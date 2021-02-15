
import boto3

translate = boto3.client(service_name='translate', region_name='ap-northeast-2', use_ssl=True)

result = translate.translate_text(Text="나는 임영민입니다.", 
            SourceLanguageCode="ko", TargetLanguageCode="ko")
            
print(result)
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))