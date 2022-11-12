def handle_webhook(request):
    req = request.get_json()

    tag = req["fulfillmentInfo"]["tag"]
    session_params = req['sessionInfo']['parameters']

    if tag == "Default Welcome Intent":
      text = "Hello from a GCF Webhook"
    elif tag == "Weather":
      get_weather_text(session_params)
      text = "My name is Flowhook"
    else:
        text = f"잘 모르겠어요."

    # You can also use the google.cloud.dialogflowcx_v3.types.WebhookRequest protos instead of manually writing the json object
    # Please see https://googleapis.dev/python/dialogflow/latest/dialogflow_v2/types.html?highlight=webhookresponse#google.cloud.dialogflow_v2.types.WebhookResponse for an overview
    res = {
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": [
                            text
                        ]
                    }
                }
            ]
        }
    }

    # Returns json
    return res


def get_weather_text(session_params):
  keys = session_params.keys()
  location = session_params['location'] if 'location' in keys else 'korea'
  datetime = session_params['date-time'] if 'date-time' in keys else 'today'

  if datetime != 'today':
    try:
      datetime_str = get_day(datetime)
    except:
      datetime_str = '오늘'
  else:
    datetime_str = '오늘'

  if location != 'korea':
    try:
      location_str = get_location(location)
    except Exception as e:
      location_str = f'서울 {str(e)[0:20]}'
  else:
    location_str = '서울'
  
  query_str = f'{datetime_str} {location_str} 날씨'

  #TODO
  result_str = f'{datetime_str} {location_str} 날씨는 맑음입니다.'
  return result_str


def get_location(loc):
  #TODO
  return '서울시'

def get_day(dt):
  import datetime
  from pytz import timezone
  KST = timezone('Asia/Seoul')
  now = datetime.datetime.now()
  year = now.year
  month = now.month
  day = now.day
  hour = now.hour
  minute = now.minute

  # check if iterable
  from collections.abc import Iterable
  if isinstance(dt, Iterable):
    dt = dt[0]

  dt_keys = dt.keys()
  def compare_and_assign(k, v):
    if k in dt_keys and dt[k] != v:
      return int(dt[k])
    return int(v)
  day = compare_and_assign('day', day)
  month = compare_and_assign('month', month)
  year = compare_and_assign('year', year)
  hour = compare_and_assign('hour', hour)
  minute = compare_and_assign('minute', minute)
  return f'{year}년 {month}월 {day}일 {hour}시 {minute}분'


def crawl_weather(query_str):
  uri = 'https://google.com/search?q=' + query_str
