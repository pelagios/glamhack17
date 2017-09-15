# GLAMhack17 Data Package

This dataset contains metada records of (mostly) historic coins. Each record includes a
geographical coordinate (or a bounding box), which represents the find spot. Most of the records
also include a time interval, which represents the dating of the coin.

## Data Format and Contents

The data files are .txt plaintext files. Each row of the file contains one JSON object. Each
JSON object contains:

* basic item metadata (item title, 'homepage' of the item, name of the providing institution)
* geographic bounds - this is always given as a bounding box, although it can be a point coordinate
  (in this case min_lon = max_lon, min_lat = max_lat)
* temporal bounds - this is always given as an interval of integer numbers ([proleptic Gregorian
  calendar](https://en.wikipedia.org/wiki/Proleptic_Gregorian_calendar) years, minus denotes BCE
  dates), although it can be a single year (in this case from = to)
* image URLs - always given as an array, with at least on URL

## Files

* For those interested in building a map-based visualization, the recommended dataset is:    [data/coins-with-coordinates.json.txt.zip](https://github.com/rsimon/mis-lva/blob/master/data/coins-with-coordinates.json.txt.zip?raw=true).

* Those interested in building (map and) timeline-based visualizations should check out:
  [data/coins-with-time.json.txt](https://github.com/rsimon/mis-lva/blob/master/data/coins-with-time.json.txt.zip?raw=true)

Both datasets are identical, except that the "timeline" dataset excludes all records that have no
date information. The "map" dataset contains 74.142 records with a total of 118.420 image URLs. The
"timeline" dataset contains 59.079 records with a total of 88.838 image URLs.

## Sample Record

```json
{  
   "geo_bounds":{  
      "min_lon":23.8404,
      "max_lat":40.8189,
      "min_lat":40.8189,
      "max_lon":23.8404
   },
   "title":"Tetradrachm of Antigonus II Gonatas, Amphipolis, 277 B.C.-239 B.C. 1990.18.6.",
   "temporal_bounds":{  
      "to":-239,
      "from":-277
   },
   "image_urls":[  
      "http://coins.lib.virginia.edu/images/coins/screen/n1990_18_6_obv.jpg",
      "http://coins.lib.virginia.edu/images/coins/screen/n1990_18_6_rev.jpg"
   ],
   "provider":"The Fralin | UVa Art Museum Numismatic Collection",
   "homepage":"http://coins.lib.virginia.edu/id/1990.18.6"
}
```

## Attribution and License

This dataset contains data provided through
[Pelagios Commons](http://commons.pelagios.org) from the following original sources:

* [American Numismatic Society](http://numismatics.org/search/). Data licensed under the
  [Open Data Commons Open Database License ODbL](http://opendatacommons.org/licenses/odbl/).

* [The Fralin | UVa Art Museum Numismatic Collection](http://coins.lib.virginia.edu/). Data
  licensed under the [Open Data Commons Open Database License ODbL](http://opendatacommons.org/licenses/odbl/).

* [finds.org.uk](https://finds.org.uk/). Data published by the The Trustees of the British Museum
  under the [Creative Commons Attribution 3.0 (CC BY 3.0) license](http://creativecommons.org/licenses/by/3.0/).
