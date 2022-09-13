from moviepy.editor import *
from moviepy.audio.fx.volumex import volumex
import sys
import os

    
def bait(P, P2, out=False):
    
    DURATION = 0.1

    #File fetch from arg or generate standard
    FILENAME = "".join([out if out is not False else "output"])
    if not FILENAME.endswith(".mp4") or not FILENAME.endswith(".webm"):
        FILENAME = FILENAME + ".webm"
    
    try:
        IMAGE = P
        VIDEO = P2

        assert os.path.exists(IMAGE), "Not a valid image path!"
        assert os.path.exists(VIDEO), "Not a valid video path!"


        videoclip = VideoFileClip(VIDEO)
        videoclip = volumex(videoclip, 2.0) #Attempt earrape! keep it 2.0 for safety
        
        imgclip = ImageClip(IMAGE).set_duration(DURATION)

        imag = imgclip.subclip(imgclip.start, imgclip.end)

        combine = concatenate_videoclips([imag, videoclip.resize(imag.size)])
        combine.write_videofile(FILENAME)
        print("Saved to - {}".format(os.path.join(os.getcwd(), FILENAME)))

        return
    except Exception as ex:
        os.system("color 4")
        print(f"{ex}")
        return
def main():
    if len(sys.argv) > 1:
        IGNORE = sys.argv[0] #Program's title
        ARG = sys.argv[1]
        
        #Help
        if ARG == "-h":
            os.system("color E")
            print("[USE] Type -b or --baitify and follow instructions!")
            return
        
        #Try to get -o and paths
        try:
            P = sys.argv[2]
            P2 = sys.argv[3]
        except:
            os.system("color 4")
            print("\nPlease pass in an image file and a video!\n")
            return

        try:
            OUTPUT = sys.argv[4]
            FILENAME = sys.argv[5]
        except:
            OUTPUT = None
        
        #Main func
        if ARG == "-b" or ARG == "--baitify":
            if OUTPUT == "-o" and FILENAME:
                bait(P, P2, FILENAME)
                return
            else:
                bait(P, P2)
                return
    else:
        os.system("color 4")
        print("Not a valid argument or no argument! [type -h]")

#BEGIN
if __name__ == "__main__":
    os.system("cls")
    os.system("color 3")
    print("""
.:| * - * DISCORD BAIT VIDEO CREATOR * - * |:.
""")
    main()
