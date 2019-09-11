import librosa 
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import IPython.display as ipd 
import os,shutil
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, concatenate_videoclips


#Load the audio file of the sports clip.
filename='M27 KKR vs RCB  – Match Highlights.mp3' #Enter your audio file name of match here. .wav,.mp3, etc. are supported.
vid, sample_rate = librosa.load(filename,sr=16000)
print(int(librosa.get_duration(vid, sample_rate)/60))

#Breaking down video into chunks of 5 seconds so that rise in energy can be found.
chunk_size=5 
window_length = chunk_size * sample_rate

#seeing an audio sample and it's time-amplitude graph
a=vid[5*window_length:6*window_length] 
ipd.Audio(a, rate=sample_rate)
energy = sum(abs(a**2))
print(energy)
fig = plt.figure(figsize=(14, 8)) 
ax1 = fig.add_subplot(211) 
ax1.set_xlabel('Time') 
ax1.set_ylabel('Amplitude') 
ax1.plot(a)

#Plotting short time energy distribution histogram of all chunks
energy = np.array([sum(abs(vid[i:i+window_length]**2)) for i in range(0, len(vid), window_length)])
plt.hist(energy) 
plt.show()
#Close graphs for progress of program

#Finding and setting threshold value of commentator and audience noise above which we want to include portion in highlights.
df=pd.DataFrame(columns=['energy','start','end'])
thresh=300
row_index=0
for i in range(len(energy)):
	value=energy[i]
	if(value>=thresh):
		i=np.where(energy == value)[0]
		df.loc[row_index,'energy']=value
		df.loc[row_index,'start']=i[0] * 5
		df.loc[row_index,'end']=(i[0]+1) * 5
		row_index= row_index + 1

#Merge consecutive time intervals of audio clips into one.
temp=[]
i,j,n=0,0,len(df) - 1
while(i<n):
	j=i+1
	while(j<=n):
		if(df['end'][i] == df['start'][j]):
			df.loc[i,'end'] = df.loc[j,'end']
			temp.append(j)
			j=j+1
		else:
			i=j
			break  
df.drop(temp,axis=0,inplace=True)


#Extracting subclips from the video file on the basis of energy profile obtained from audio file.
start=np.array(df['start'])
end=np.array(df['end'])

#Create temporary folder for storing subclips generated. This folder will be deleted later after highlights are generated. 
cwd=os.getcwd()
sub_folder=os.path.join(cwd,"Subclips")
if os.path.exists(sub_folder):
	shutil.rmtree(sub_folder)
	path=os.mkdir(sub_folder)
else:
	path=os.mkdir(sub_folder)
#print(sub_folder,type(sub_folder))

#Extract moments from videos to be added in highlight
print(df)
for i in range(len(df)):
	if(i!=0):
		start_lim = start[i] - 5  #Assuming that noise starts after the shot, so set start point as t-5 seconds to include the shot/wicket action.
	else:
		start_lim = start[i] 
	end_lim   = end[i]   
	filename="highlight" + str(i+1) + ".mp4"
	ffmpeg_extract_subclip("M27 KKR vs RCB  – Match Highlights.mp4",start_lim,end_lim,targetname=sub_folder+"/"+filename) #Enter your sports video clip name here.

files=os.listdir(sub_folder)
files=[sub_folder+"/highlight" + str(i+1) + ".mp4" for i in range(len(df))]
#print(files)
final_clip=concatenate_videoclips([VideoFileClip(i) for i in files])
final_clip.write_videofile("KKRvsRCB_Highlights.mp4") #Enter the desired output highlights filename.
shutil.rmtree(sub_folder) #Delete the temporary file.
