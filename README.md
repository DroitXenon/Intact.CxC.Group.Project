# CxC Group Project - Intact
Group Member: Bob Bao, Catherine Zhang, Tommy Pang, Justin Wang

![alt text](https://github.com/DroitInjuste/Intact.CxC.Group.Project/blob/main/UWDSC.png "UW DSC")


# Challenges faces: 
We are not familiar with data hackathons, so we spend quite a lot of time figuring out how each part works. The workshop and internet research helped us to solve the problems.

Sometimes the output does not behave as we expected, so we have to either debug or change a way to tackle the problems. For example, when we are trying to remove the stop words in the transcription, we first used a method that first tokenizes the transcription and then removes the stop words. However, the running time is extremally long and we did not get to see the output for that. So we instead directly filter the stop words when we are using the counter to find the frequently occurring words. 

# Overall outcomes:
We try to solve the problem by finding the frequently occurring words in all labels. And use the correlation of the occurrence of each word with the labels to predict the medical specialty. We filtered out the stop words so they will not affect the prediction. However unfortunately the outcomes are not very precise, but overall we think we are on the right track.
