# :football: Sports Highlights Generator :cricket:

Whether it's cricket, or football, we always wish to watch the highlights of the match we missed or watch the highlights of our favorite matches again and again! 
What better way than to generate your own? :smile:

This project is aimed at obtaining highlights from the full match video, without using *computer vision and NLP!* Yes, you read that right. 

We always think that obtaining such videos would require deep learning and stuff to generate.  But what if we could do so, by applying some simple concepts of energy threshold in audio waves to get a basic highlights package, if not as good as state-of-the-art? :grin:

The main aim of doing this project was to get myself acquainted with audio and video processing libraries in Python3.6. 

### TODOs:

* [ ] Develop a GUI to upload a full video and press download for highlights.
* [ ] Automatically generate the audio file for the video file uploaded by user.
* [ ] Make the variable parameters like sample rate,filename,chunk size, threshold, etc. settable via Terminal/GUI.
* [ ] Reduce the latency time by splitting the video and then parallelizing the process of highlight extraction.
* [x] Automatically delete the highlight subclips being generated.


P.S.: For some sample  video and audio, kindly click [here](https://drive.google.com/open?id=1bWfQat17fmmpBo92w698C2sxRxBEztnk). This contains two match video and audio files and also the script generated highlights:

1. India vs Australia 2007 World Cup Indian Powerplay.
2. KKR vs RCB (RCB 49 All out).

## To run this project:
* [Fork](https://github.com/arghyadeep99/Sports-Highlights-Generator) this Repository.
* Open Terminal and enter the folder 'Sports-Highlights-Generator'.
* `pip3 install -r requirements.txt`
* Download the full match video and it's audio file in the present working directory.
* Set variables for input audio and video filenames and desired output filename in code. (This will soon be changed to arguments from terminal!)
* Run `python3 generator.py`
* Wait while the highlights file is cooking! :alarm_clock:
* Voila! You have your highlights package ready. :fire:

#### This project still has scope of development, so you can also contribute to this Project as follows:
* [Fork](https://github.com/arghyadeep99/Sports-Highlights-Generator) this Repository.
* Clone your Fork on a different branch:
	* `git clone -b <name-of-branch> https://github.com/arghyadeep99/Sports-Highlights-Generator.git`
* After adding any feature:
	* Goto your fork and create a pull request.
	* I will test your modifications and merge changes.
	
#### `This project was done under 4 hours with no pre-preparation.`
---
### **Developed with :heart: by [Arghyadeep Das](https://github.com/arghyadeep99)**
