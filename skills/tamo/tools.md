# Tools & Capabilities

This file defines the tools and API endpoints available for interacting with the TAMO e-diary portal.

## apistubs Declarations

The following stubs simulate the TAMO API for development and testing when the actual service is unavailable or to avoid sending real credentials.

### `tamo_login`
*   **Description:** Authenticates with the TAMO portal.
*   **Method:** POST
*   **Endpoint:** `https://dienynas.tamo.lt/api/login` (Simulated via `apistubs`)
*   **Request Body:** `{"username": "<username>", "password": "<password>"}`
*   **Mock Response (apistubs):**
    ```json
    {
      "status": "success",
      "token": "mock_tamo_auth_token_12345",
      "user_id": "parent_88"
    }
    ```

### `tamo_get_homework`
*   **Description:** Retrieves homework assignments for the specified date range.
*   **Method:** GET
*   **Endpoint:** `https://dienynas.tamo.lt/api/homeworks` (Simulated via `apistubs`)
*   **Headers:** `Authorization: Bearer <token>`
*   **Parameters:** `start_date` (YYYY-MM-DD), `end_date` (YYYY-MM-DD)
*   **Mock Response (apistubs):**
    ```json
    {
      "homeworks": [
        {
          "id": "hw_001",
          "subject": "Mathematics",
          "description": "Exercises 1-5 on page 42.",
          "due_date": "2023-10-26"
        },
        {
          "id": "hw_002",
          "subject": "History",
          "description": "Read chapter 4 and prepare for a quiz.",
          "due_date": "2023-10-27"
        }
      ]
    }
    ```

### `tamo_get_notifications`
*   **Description:** Retrieves new messages and notifications.
*   **Method:** GET
*   **Endpoint:** `https://dienynas.tamo.lt/api/notifications` (Simulated via `apistubs`)
*   **Headers:** `Authorization: Bearer <token>`
*   **Mock Response (apistubs):**
    ```json
    {
      "notifications": [
        {
          "id": "notif_101",
          "sender": "School Administration",
          "date": "2023-10-25",
          "message": "School will be closed on Friday due to a public holiday."
        }
      ]
    }
    ```

### `tamo_get_reports`
*   **Description:** Retrieves marks and progress reports.
*   **Method:** GET
*   **Endpoint:** `https://dienynas.tamo.lt/api/reports` (Simulated via `apistubs`)
*   **Headers:** `Authorization: Bearer <token>`
*   **Mock Response (apistubs):**
    ```json
    {
      "reports": [
        {
          "subject": "Mathematics",
          "mark": "9",
          "date": "2023-10-24",
          "comment": "Good job on the test."
        },
        {
          "subject": "English",
          "mark": "10",
          "date": "2023-10-25",
          "comment": "Excellent presentation."
        }
      ]
    }
    ```

## apicron Declarations

*   **Schedule:** `0 17 * * 1-5` (Every weekday at 17:00)
*   **Action:** Execute the "Check TAMO Updates" workflow (authenticate, fetch homework, notifications, and reports, compare with memories, and log track).