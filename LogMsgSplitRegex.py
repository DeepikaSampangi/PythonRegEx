import re

input_log_msg: str = '3e656b8e06c176 el-s3-log-file [24/Dec/2014:11:54:18 +0000] 202.141.245.38 arn:aws:iam::xxxxx:user/xyz E27FFBA2CA3D61F3 REST.GET.OBJECT logs/2014-12-23-09-25-19-E39257 "GET /el-s36 HTTP/1.1" 200 - 660 660 30 30 "https://s3-console-us-standard/Console.html?region&locale=en" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36" -'

pat = '\s+(?=(?:\"[^\"]|[^\"]])*$)'

output = re.split(pat, input_log_msg)

print(output)