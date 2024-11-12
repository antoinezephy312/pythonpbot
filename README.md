Here's the documentation for the command structure in your bot, including a guide for defining text and attachment commands.



---



## Command Structure Documentation



Each command in the bot is defined as a standalone Python file in the `commands` folder. Each command follows a consistent structure, which includes defining attributes and an `execute` function that performs the command's action. Commands can send either text responses or media attachments, such as images, audio, video, and documents.



### Basic Command Structure



Each command file should include the following components:



- **Attributes**:

  - `name`: A unique name that triggers the command, like `"hello"`.

  - `description`: A brief description of what the command does.

  - `admin_bot`: A boolean (`True` or `False`) indicating if the command requires admin privileges.



- **Function**:

  - `execute(sender_id, message_text)`: This function contains the logic for the command and is called when the command is triggered. `sender_id` is the user’s ID, and `message_text` is the text of the message sent by the user.



### Example Text Command: `hello.py`



This example shows a simple text command that greets the user.



```python

from api.sendMessage import send_message



name = "hello"

description = "Sends a greeting message to the user."

admin_bot = False  # Does not require admin privileges



def execute(sender_id, message_text):

    response_text = "Hello! How can I assist you today?"

    send_message(sender_id, {"text": response_text})

```



### Attachment Command Structure



For commands that send attachments, the `send_message` function in `sendMessage.py` supports various media types. Each attachment command should specify the type of attachment (`image`, `audio`, `video`, or `file`) and include the necessary data.



#### Sending an Attachment



The `send_message` function requires a dictionary format to specify attachments:



- `attachment` - A dictionary containing:

  - `type`: The type of attachment, such as `"image"`, `"audio"`, `"video"`, or `"file"`.

  - `payload`: Contains the `url` of the attachment or other necessary data.



#### Example: `image.py` Command



This example command sends an image to the user.



**`commands/image.py`**:

```python

from api.sendMessage import send_message



name = "image"

description = "Sends an example image to the user."

admin_bot = False  # Set to True if only admins should use it



def execute(sender_id, message_text):

    image_url = "https://example.com/path/to/image.jpg"

    message = {

        "attachment": {

            "type": "image",

            "payload": {

                "url": image_url,

                "is_reusable": True  # Set to True to reuse the image on the Facebook server

            }

        }

    }

    send_message(sender_id, message)

```



### Supported Attachment Commands



Here’s how to structure commands for each attachment type:



#### 1. **Audio Command** (`audio.py`)

   - **Usage**: Sends an audio file (e.g., MP3).

   - **Example**:

     ```python

     from api.sendMessage import send_message



     name = "audio"

     description = "Sends an audio file."

     admin_bot = False



     def execute(sender_id, message_text):

         audio_url = "https://example.com/path/to/audio.mp3"

         message = {

             "attachment": {

                 "type": "audio",

                 "payload": {

                     "url": audio_url,

                     "is_reusable": True

                 }

             }

         }

         send_message(sender_id, message)

     ```



#### 2. **Video Command** (`video.py`)

   - **Usage**: Sends a video file.

   - **Example**:

     ```python

     from api.sendMessage import send_message



     name = "video"

     description = "Sends a video file."

     admin_bot = False



     def execute(sender_id, message_text):

         video_url = "https://example.com/path/to/video.mp4"

         message = {

             "attachment": {

                 "type": "video",

                 "payload": {

                     "url": video_url,

                     "is_reusable": True

                 }

             }

         }

         send_message(sender_id, message)

     ```



#### 3. **Document Command** (`document.py`)

   - **Usage**: Sends a document file (e.g., PDF).

   - **Example**:

     ```python

     from api.sendMessage import send_message



     name = "document"

     description = "Sends a document file."

     admin_bot = False



     def execute(sender_id, message_text):

         document_url = "https://example.com/path/to/document.pdf"

         message = {

             "attachment": {

                 "type": "file",

                 "payload": {

                     "url": document_url,

                     "is_reusable": True

                 }

             }

         }

         send_message(sender_id, message)

     ```



---



### Handling Long Text Messages



If a text response exceeds the 2000-character limit, the `sendMessage.py` module should use the `split_message` function to divide the message into chunks and send each chunk separately.



### Error Handling



Commands should gracefully handle errors:

- If a command encounters an error (e.g., missing parameters or file not found), it should return an error message to the user, explaining the issue.



This command structure enables consistent, modular, and easily extendable functionality across your bot, allowing new commands to be added or modified with minimal effort.