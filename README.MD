# 25DaysOfServerless


## Day1 - Spin the Dreidel

- https://25daysofserverless.com/calendar/1

### Solution

Use Python's builtin **random** package to invoke *choose* from a list of unicode chars.


## Day3 - Secret Santa

- https://25daysofserverless.com/calendar/3

### Solution

The solution uses the BlobStorage output binding and webhook binding from the GitHub repository.

The incoming webhook has the **head_commit** information which exposes the added file names. Also, the solution checks that the added file names are only .png files before processing them.

The output blob storage binding can take a byte stream, so request package is used to hit the GitHub URL for the image and then the byte stream is passed to the outputBlob's generic set() method.

I couldn't figure out how to pass a blob name from the Python function.