# Plant.id API v2

**in progress**

## Request

POST or GET (if no data needed)

POST 
 - application/json
 - multipart/form-data
    - data as json string of field named `data`


## Authentication

- "api_key" in POSTed data

- [Basic authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
    - username = "client"
    - password = `your_api_key`
    
- přes header, "api_key"

## Endpoints


### /enqueue_identification

POST
- latitude
- longitude
- datetime - int, seconds timestamp, default = now
- custom_id
- callback_url
- modifiers
- images - as parameter or in files

### /get_identification_result/\<id\>
get identification data by `id` 

POST
 - plant_language - default `en`
 - plant_details - list of plant KB view names

### /get_identification_result/custom_id/\<custom_id\>
same as previous but for `custom_id`

### /get_identification_result/multiple
get multiple identifications

POST
 - ids
 - custom_ids

### /identify
Synchronous version of `/enqueue_identification`.
Wait for identification to complete and return completed identification.
It times out, return identification info without suggestions same as `/enqueue_identification`.

POST
- identification_timeout: seconds, default 20, max. 20
- plant_language - default `en`
- plant_details - same as `get_identification_result`


### /delete_identification/\<id\>
### /delete_identification/custom_id/\<custom_id\>

DELETE


### /confirm_suggestion/<id>
### /unconfirm_suggestion/<id>


### /usage_info
