# YDownloader


## Contents

- [Dependecy](#dependency)
- [Usage](#usage)

## Dependency

1) Python 2/3

2) `pytube` module. To install pytube module run this command:
```shell
pip install pytube
```

## Usage

To download multiple video save all the video in a file and save it. Suppose our all videos links are in a file named `links.txt`. Then run the following command:

```shell
sh ydownload.sh links.txt
```
Then it will show the available download format. 
Enter the `itag`. It will download all the video in selected format.

### Warning

Please do not use `./ydownload.sh`. It will break the string formatting. Perhaps it will work smoothly.
___
# Thank You