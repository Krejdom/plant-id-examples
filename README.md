[Plant.id](https://plant.id) offers a plant identification service based on machine learning. Once you [obtain the API key](https://web.plant.id/plant-identification-api/), you can use these client's code to speed-up the development of your implementation.

# Plant.id API v2
## Synchronous identification
```https://api.plant.id/v2/identify```

Send plant photos to our backend, wait for identification, and return the result. If the identification takes more than the `identification_timeout`, return identification info without any suggestions.
_We do not recomend to use this in production (use asynchronous identification - `enqueue_identification` instead - see bellow)._

### Request
POST request with two required parameters:
- **`api_key`**- your [API key](https://web.plant.id/plant-identification-api/)
- **`images`** - one ore more images of the plant you want to identify (string - base64 or a file)

The list of optional parameters:
- `custom_id` - identifier you can set for your purpose
- `callback_url` - URL where we POST results after identification is completed
- `latitude` - geographic coordinate (float)
- `longitude` - geographic coordinate (float)
- `modifiers` - list of strings: 
    - `"crops_simple"`/`"crops_fast"` (default)/`"crops_medium"` - specify the speed & accuracy of the identification
    - `"similar_images"` - allow displaying of similar images -> **If you want to get similar images in the response, you must include item `similar_images` here.**
- `datetime` - time in seconds (int)
- `identification_timeout` - seconds (int, default `20`, max. `20`)
- `plant_language` - language code ([ISO 639-1](https://en.m.wikipedia.org/wiki/List_of_ISO_639-1_codes)) used for `plant_details` (default `"en"`)
- `plant_details` - list of strings, which determines which information about the plant will be included in the response (if the data is available)
    - `"common_names"` - list of common names of the plant in the language specified in `plant_language`
    - `"url"` - link to page with the plant profile (usually Wikipedia)
    - `"name_authority"` - scientific name of the plant
    - `"wiki_description"` - description of the plant from Wikipedia with source url and license
    - `"taxonomy"` - dictionary with the plant taxonomy

### Result
The result contains a list of suggestions of possible plant species (taxons). Each suggestion contains:
- `scientific_name` - the scientific name of the plant
- `common_names` - list of common names of the plant (if available)
- `url` - link to Wikipedia or Google
- `probability` - certainty level that suggested plant is the one from the photo
- `similar_images` - representative images of the identified species carefully selected by the model, so it resembles the input image (Similar images are includede in the result only if you add the value `similar_image` in the `parameters` list of the reques.)
- `confirmed` - confirmation status
- ...

Record example:
```json
{
   "id":1057230,
   "custom_id":"None",
   "callback_url":"None",
   "meta_data":{
      "latitude":"None",
      "longitude":"None",
      "datetime":"2020-02-25"
},
   "uploaded_datetime":1582657674.229304,
   "finished_datetime":1582657678.952631,
   "images":["..."],
   "suggestions":[
      {
         "plant_name":"Cissus",
         "plant_details":{
            "scientific_name":"Cissus",
            "structured_name":{
               "genus":"cissus"

},
            "common_names":"None",
            "url":"http://en.wikipedia.org/wiki/Cissus",
            "name_authority":"None",
            "wiki_description":{
               "value":"Cissus is a genus of approximately 350 species of lianas (woody vines) in the grape family (Vitaceae). They have a cosmopolitan distribution, though the majority are to be found in the tropics.",
               "citation":"http://en.wikipedia.org/wiki/Cissus",
               "license_name":"CC BY-SA 3.0",
               "license_url":"https://creativecommons.org/licenses/by-sa/3.0/"
            
},
            "taxonomy":{
               "kingdom":"Plantae",
               "phylum":"Tracheophyta",
               "class":"Magnoliopsida",
               "order":"Vitales",
               "family":"Vitaceae",
               "genus":"Cissus"           
}      
},
         "probability":0.44523655283089236,
         "confirmed":false,
         "similar_images":"..."
      
},
"..." 
],
   "modifiers":"...",
   "secret":"...",
   "fail_cause":"None",
   "countable":true
}
```

## Asynchronous identification
```https://api.plant.id/v2/enqueue_identification```
Send photos for identification (and retrieve the result later with anohter request).

### Request
Required parameters:
- **`api_key`**- your [API key](https://web.plant.id/plant-identification-api/)
- **`images`** - one ore more images of the plant you want to identify (string - base64 or a file)

Optional parameters:
- `custom_id` - identifier you can set for your purpose
- `callback_url` - URL where we POST results after identification is completed
- `latitude` - geographic coordinate (float)
- `longitude` - geographic coordinate (float)
- `modifiers` - list of strings: 
    - `"crops_simple"`/`"crops_fast"` (default)/`"crops_medium"` - specify the speed & accuracy of the identification
    - `"similar_images"` - allow displaying of similar images -> **If you want to get similar images in the response, you must include item `similar_images` here.**
- `datetime` - time in seconds (int)

### Response
`ID` of the identification. Use it to get the identification result with following request

## Get identification result
```https://api.plant.id/v2/get_identification_result/ID```
```https://api.plant.id/v2/get_identification_result/custom_id/CUSTOM_ID```
Check whether identification with given `ID` (or your `CUSTOM_ID`) has been already proceeded and returns its result.

Parameters:
- **`api_key`**- your [API key](https://web.plant.id/plant-identification-api/)
- `plant_language` - language code ([ISO 639-1](https://en.m.wikipedia.org/wiki/List_of_ISO_639-1_codes)) used for `plant_details` (default `"en"`)
- `plant_details` - list of strings, which determines which information about the plant will be included in the response (if the data is available)
    - `"common_names"` - list of common names of the plant in the language specified in `plant_language`
    - `"url"` - link to page with the plant profile (usually Wikipedia)
    - `"name_authority"` - scientific name of the plant
    - `"wiki_description"` - description of the plant from Wikipedia with source url and license
    - `"taxonomy"` - dictionary with the plant taxonomy

If you want to get the results of more indentifications, use following POST reques:
```https://api.plant.id/v2/get_identification_result/multiple```
and specify at least one of the following parameters:

- `ids` - list of ids provided by the identification response
- `custom_ids` - list of ids provided by you in the identification request

## Delete identification
```https://api.plant.id/v2/delete_identification/ID```
```https://api.plant.id/v2/delete_identification/custom_id/CUSTOM_ID```

Delete identification with `ID`, or with your `CUSTOM_ID`.

### Request
There is one required parameter:
- **`api_key`**- your [API key](https://web.plant.id/plant-identification-api/)

## Confirm
```https://api.plant.id/v2/confirm_suggestion/SUGGESTION_ID```

Confirm suggestion with `SUGGESTION_ID` and unconfirm all others. Use when your plant matches our identification.

### Request
There is one required parameter:
- **`api_key`**- your [API key](https://web.plant.id/plant-identification-api/)

## Unconfirm
```https://api.plant.id/v2/unconfirm_suggestion/SUGGESTION_ID```

Unconfirm previously confirmed suggestion with `SUGGESTION_ID`.

### Request
There is one required parameter:
- **`api_key`**- your [API key](https://web.plant.id/plant-identification-api/)

## Usage info
```https://api.plant.id/v2/usage_info```
Get stats about your API key limits and usage.

### Request
There is one required parameter:
- **`api_key`**- your [API key](https://web.plant.id/plant-identification-api/)

### Response
Example output:
```
{
  "active": True,
  "daily_limit": None,
  "weekly_limit": 200,
  "monthly_limit": None,
  "total_limit": None,
  "is_closed": False,
  "used_day": 5,
  "used_week": 5,
  "used_month": 11,
  "used_total": 11,
  "remaining_day": None,
  "remaining_week": 195,
  "remaining_month": None,
  "remaining_total": None
}
```
