
# Notification Service API Documentation

## Overview 

The Notification Service API allows clients to send notifications to a Microsoft Teams channel based on the type of notification. The API receives notifications via a POST interface and forwards them to the appropriate Microsoft Teams channel based on the notification type.

## Endpoints

### 1. Receive Notification

-   **URL:** `/receive_notification/`
-   **Method:** POST
-   **Description:** Receives a notification and forwards it to the appropriate Microsoft Teams channel based on the type of notification.
-   **Request Body:**
    -   `Type` (string, required): Type of notification (`Warning` or `Info`).
    -   `Name` (string, required): Name of the notification.
    -   `Description` (string, required): Description of the notification.
-   **Response:**
    -   Success (200 OK):
   json  `{  "message":  "Notification forwarded to Microsoft Teams"  }`
        
    -   Error (500 Internal Server Error):
       Json    `{  "error":  "Failed to forward notification to Microsoft Teams"  }`
        
-   **Example:**
   ** bash **
    `curl -X POST http://example.com/receive_notification/ -d  "Type=Warning&Name=Backup Failure&Description=The backup failed due to a database problem"`
    
## Example Usage

### 1. Sending a Warning Notification
**Request:**
http
`POST /receive_notification/ HTTP/1.1 Host: example.com Content-Type: application/x-www-form-urlencoded Type=Warning&Name=Backup Failure&Description=The backup failed due to a database problem`

**Response (200 OK):**
json
`{  "message":  "Notification forwarded to Microsoft Teams"  }`

### 2. Sending an Info Notification
**Request:**
http
`POST /receive_notification/ HTTP/1.1 Host: example.com Content-Type: application/x-www-form-urlencoded Type=Info&Name=Quota Exceeded&Description=Compute Quota exceeded`

**Response (200 OK):**

json
`{  "message":  "Notification not forwarded"  }`

## Error Handling

-   If the request is not a POST request, the API will return a 405 Method Not Allowed error.
-   If the required fields (`Type`, `Name`, `Description`) are missing from the request body, the API will return a 400 Bad Request error.
-   If there is an error while forwarding the notification to Microsoft Teams, the API will return a 500 Internal Server Error along with an error message.

**NB:** The microsoft teams webhook was hard to find even if I’ve subscribed for the premium one( the subscription bill is sent as proof). Instead, i use the incoming webhook of slack which is working properly. Once we get the microsoft webhook link we could easily replace it in the code.
