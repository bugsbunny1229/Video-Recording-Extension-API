# API Documentation
This documentation provides an overview of the API endpoints, request and response formats, sample usage, and instructions for setting up and deploying the API.

### Base URL
```bash
https://chrome-extension-api-6tfw2.ondigitalocean.app/
```

# Create a Video Recording

## Description:
This endpoint creates a new video recording session and returns a unique identifier (UUID) that can be used for subsequent interactions.

* URL: /api/create/
* HTTP Method: POST
* Authentication: None (No authentication required)
* Request:
  * No request data is required.
* Response:
  * 200 OK: Video recording session created successfully.
  * 201 Created: Video recording session created successfully, and a UUID is provided in the response.

**Example Request:**

```http
POST /api/create/
```

**Example Response (201 Created):**

```json
{
    "uuid": "98b6f078-7b13-4f90-95a0-6f957d0f899e"
}
```

# Add Data to a Video Recording

## Description:
Use this endpoint to append binary data to an existing video recording session identified by its UUID. The binary data is streamed and added to the video file while recording is in progress.

* URL: /api/add-data/{uuid}/
* HTTP Method: PATCH
* Authentication: None (No authentication required)
* Request:
  * Path Parameters:
  * uuid (string, required): The UUID of the video recording session to update.
* Request Data:
  * binary_data (binary, required): The binary data to append to the video file.
* Response:
  * 200 OK: Data appended successfully.
  * 400 Bad Request: Data cannot be appended (e.g., recording is already complete).
  * 404 Not Found: The specified video recording session does not exist.

**Example Request:**

```http
PATCH /api/add-data/98b6f078-7b13-4f90-95a0-6f957d0f899e/
Content-Type: application/octet-stream
```

**Example Request Body:**
  * Binary data stream (e.g., video frames).

**Example Response (200 OK):**

```json
{
    "message": "Data appended successfully."
}
```

# Complete a Video Recording and Transcribe

## Description:
This endpoint marks a video recording session as complete, indicating that the recording process has finished. Once marked as complete, the video file is ready for use, and it is transcribed using OpenAI Whisper.

* URL: /api/complete/{uuid}/
* HTTP Method: PATCH
* Authentication: None (No authentication required)
* Request:
  * Path Parameters:
  * uuid (string, required): The UUID of the video recording session to mark as complete.
* Response:
  * 200 OK: Recording marked as complete. Transcription of the video is also provided if available.
  * 400 Bad Request: Recording cannot be marked as complete (e.g., no video file or already complete).
  * 404 Not Found: The specified video recording session does not exist.
  * 500 Internal Server Error: Transcription of the video failed.

**Example Request:**

```http
PATCH /api/complete/98b6f078-7b13-4f90-95a0-6f957d0f899e/
```

**Example Response (200 OK with Transcription):**
```json
{
    "message": "Recording marked as complete.",
    "video_url": "https://example.com/videos/98b6f078-7b13-4f90-95a0-6f957d0f899e.mp4",
    "transcription_text": "Transcribed text of the video."
}
```

**Example Response (200 OK without Transcription):**

```json
{
    "message": "Recording marked as complete."
}
```