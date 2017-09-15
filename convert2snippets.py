import json

with open('coins.json') as f:
    data = json.load(f)
    outputForTimeline = open('coins-with-time.json.txt', 'w')
    outputForMap = open('coins-with-coordinates.json.txt', 'w')

    # We're counting items and images (for geo and time dumps) for info
    geoItemCounter = 0
    geoImageCounter = 0

    timeItemCounter = 0
    timeImageCounter = 0

    for item in data['items']:
        geoItemCounter += 1
        geoImageCounter += len(item['depictions'])

        converted = {
          'title': item['title'],
          'provider': item['dataset_path'][0]['title'],
          'homepage': item['homepage'],
          'image_urls': item['depictions'],
          'geo_bounds': {
              'min_lon': item['geo_bounds']['min_lon'],
              'max_lon': item['geo_bounds']['max_lon'],
              'min_lat': item['geo_bounds']['min_lat'],
              'max_lat': item['geo_bounds']['max_lat']
          }
        }

        if 'temporal_bounds' in item:
            timeItemCounter += 1
            timeImageCounter += len(item['depictions'])

            converted['temporal_bounds'] = { 'from': item['temporal_bounds']['start'], 'to': item['temporal_bounds']['end'] }
            outputForTimeline.write(json.dumps(converted))
            outputForTimeline.write('\n')

        outputForMap.write(json.dumps(converted))
        outputForMap.write('\n')

    outputForTimeline.close()
    outputForMap.close()

    print('Converted:')
    print(str(geoItemCounter) + ' items with ' + str(geoImageCounter) + ' images')
    print('With date: ' + str(timeItemCounter) + ' items with ' + str(timeImageCounter) + ' images')
