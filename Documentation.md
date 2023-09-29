# API Documentation
This documentation provides an overview of the API endpoints, request and response formats, sample usage, and instructions for setting up and deploying the API.

### Base URL
```bash
https://chrome-extension-api-6tfw2.ondigitalocean.app
```

# API Endpoint: Upload Video

## Description:
This endpoint allows users to upload video files. It performs validation to ensure that only video files with certain extensions are accepted.

* URL: /api
* HTTP Method: POST
* Authentication: None (No authentication required)
* Request Body: A POST request should include a video file in the video_file field.

**Request Example:**

```http
POST /api HTTP/1.1
Host: example.com
Content-Type: multipart/form-data; boundary=---------------------------1234567890123456789012345678
Content-Length: 12345

-----------------------------1234567890123456789012345678
Content-Disposition: form-data; name="video_file"; filename="sample.mp4"
Content-Type: video/mp4

[Binary video data]
-----------------------------1234567890123456789012345678--
```

**Response Example:**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "Video uploaded successfully.",
    "video_url": "http://example.com/media/videos/sample.mp4"
}
```

**Error Responses:**

* *400 Bad Request:*
- If the request does not contain a valid video file.
- If the uploaded file is not a video or has an invalid format.
- If the video file format is not supported.

```json
{
    "error": "Invalid file type. Only video files are allowed."
}
```

* *500 Internal Server Error:*
- If there is an unexpected error during file upload or database operation

```json
{
    "error": "Internal Server Error"
}
```


# API Endpoint: List All Videos

## Description:
This endpoint retrieves a list of all uploaded videos.

* URL: /api/list
* HTTP Method: GET
* Authentication: None (No authentication required)

**Request Example:**

```http
GET /api/list HTTP/1.1
Host: example.com
```

**Response Example:**

```http
HTTP/1.1 200 OK
Content-Type: application/json

[
    {
        "id": 1,
        "video_file": "http://example.com/media/videos/sample1.mp4",
        "timestamp": "2023-09-28T12:00:00Z"
    },
    {
        "id": 2,
        "video_file": "http://example.com/media/videos/sample2.mp4",
        "timestamp": "2023-09-28T12:30:00Z"
    }
]
```

**Error Responses:**

* *500 Internal Server Error:*
- If there is an unexpected error while retrieving the list of videos.

```json
{
    "error": "Internal Server Error"
}
```