from pytube import YouTube
import sys

class YouTubeVideo:
    video = None
    def __init__(self, url):
        self.video = YouTube(url)
        # self.video.register_on_progress_callback(self.show_progress_bar)
        # print(self.video)
    def download(self):
        self.video.streams.first().download()
    def show_progress_bar(self, stream, chunk, file_handle, bytes_remaining):
        print(file_handle)
        print(bytes_remaining)



def main():
    if(len(sys.argv) < 2):
        fileName = 'download.txt'
    else:
        fileName = sys.argv[1]
    try:
        sourceFile = open(fileName, 'r')
        files = [line.rstrip('\n') for line in sourceFile]
        report('Total File ' + str(len(files)))
        i = 1
        for url in files:
            try:
                report( str(i) + ' Started')
                vid = YouTubeVideo(url)
                vid.download()
                report(str(i) + ' Ended')                
            except Exception as e:
                # print(e.message)
                report(str(i) + ' --------- Cannot Download The File')
                pass
            i += 1
    except Exception as e:
        print(e.message)

def report(stri):
    print('\n########################### ' + stri +' #######################\n')

if __name__ != 'main':
    main()